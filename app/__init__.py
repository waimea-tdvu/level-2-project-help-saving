#===========================================================
# PROJECT NAME HERE  Savings Tracker
# By YOUR NAME HERE  Trinh Vu
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/")
def show_menu(): 
    flash("Welcome to Savings Tracker")
        # flash("Test SUCCESS message", "success")
        # flash("Test INFO message", "info")
        # flash("Test WARNING message", "warning")
        # flash("Test ERROR message", "error")
    with connect_db() as db:
        sql = """
            SELECT id, bank, current_savings, weekly_target,date_week_start
            FROM savings
            ORDER BY id
        """
        savings = db.execute(sql).fetchall()

    return render_template("pages/savings_menu.jinja", savings=savings)



@app.get("/expense/list")
def show_expense_list():
    with connect_db() as db:
        sql = """
            SELECT expenses.id,
                   expenses.category_id,
                   categories.name AS category_name,
                   categories.icon AS category_icon,
                   expenses.amount,
                   expenses.spend,
                   expenses.date
            FROM expenses
            JOIN categories
                ON expenses.category_id = categories.id
            ORDER BY expenses.id
        """
        expenses = db.execute(sql).fetchall()

        return render_template("pages/expense_list.jinja", expenses=expenses)

from datetime import date

@app.get("/expense/<int:expense_id>/delete")
def delete_expense(expense_id):
    with connect_db() as db:
        sql = """
            DELETE FROM expenses
            WHERE id=?
        """
        params = (expense_id),
        db.execute(sql, params)
    
        flash("Delete Successfuly")
        return redirect("/expense/list")

@app.post("/expense/new")
def get_expense():
    category_id = request.form.get("category_id", "").strip()  
    amount = request.form.get("amount", "").strip()
    spend = request.form.get("spend", "").strip()
    date_td = request.form.get("date", "").strip()
            
    with connect_db() as db:
        sql="""
            INSERT INTO expenses (category_id, amount, spend, date)
            VALUES (?, ?, ?, ?)
        """

        params = (category_id, amount, spend, date_td)
        
        db.execute(sql,params)

        flash("Expense added succesfully")
        return redirect("/expense/list")

@app.get("/expense/new")
def show_new_expense():
    today = date.today().isoformat()

    with connect_db() as db:
        sql = """
            SELECT id,name, icon
            FROM categories
        """

        categories = db.execute(sql).fetchall()

    return render_template("pages/expense_form.jinja", today=today, categories=categories)


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

