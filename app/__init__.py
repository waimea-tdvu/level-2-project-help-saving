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
        return render_template("pages/savings_menu.jinja")

@app.get("/expense/list")
def show_expense_list():
    with connect_db() as db:
        sql = """
            SELECT id, category_id, amount, spend, date
            FROM expenses
        """
        params = ()
        expenses = db.execute(sql,params).fetchall()

        return render_template("pages/expense_list.jinja", expenses=expenses)

@app.post("/expense/new")
def get_expense():
    id = request.form.get("id", "unknow").strip()
    category_id = request.form.get("category_id", "unknow").strip()  
    amount = request.form.get("amount", "unknow").strip()
    spend = request.form.get("spend", "unknow").strip()
    date = request.form.get("date", "unknow").strip()
            
    with connect_db() as db:
        sql="""
            INSERT INTO expenses (id, category_id, amount, spend, date)
            VALUE (?, ?, ?, ?, ?)
        """

        params = (id, category_id, amount, spend, date)
        db.execute(sql,params)

        flash(f"Expense {id} added succesfully")
        return redirect("/expense/list")
    print(request.form)


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

