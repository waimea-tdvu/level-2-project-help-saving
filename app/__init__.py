#===========================================================
# PROJECT NAME HERE  Savings Tracker
# By YOUR NAME HERE  Trinh Vu
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from datetime import date, timedelta
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

    # Calculate current week's Monday and Sunday
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    with connect_db() as db:

        # Get savings information
        sql = """
            SELECT id, initial_budget, current_savings, weekly_target, date_week_start
            FROM savings
            ORDER BY id
        """
        savings = db.execute(sql).fetchall()

        # Get initial budget and weekly target
        if savings:
            initial_budget = savings[0]["initial_budget"] or 0
            target = savings[0]["weekly_target"] or 0
        else:
            initial_budget = 0
            target = 0

        # Calculate total weekly expense
        sql = """
            SELECT COALESCE(SUM(spend), 0) AS total_expense
            FROM expenses
            WHERE date BETWEEN ? AND ?
        """

        params = (week_start.isoformat(), week_end.isoformat())
        total_expense = db.execute(sql, params).fetchone()

        # Calculate current savings
        current_savings = initial_budget - total_expense["total_expense"]

        sql = """
            UPDATE savings
            SET current_savings = ?
            WHERE id = 1
        """

        params = (current_savings,)
        db.execute(sql, params)

        # Calculate savings progress
        if target > 0:
            saving_progress = min(max((current_savings / target) * 100, 0), 100)
        else:
            saving_progress = 0

    return render_template(
        "pages/savings_menu.jinja",
        savings=savings,
        week_start=week_start.isoformat(),
        week_end=week_end.isoformat(),
        saving_progress=saving_progress,
        total_expense=total_expense,
        current_savings=current_savings
    )


@app.get("/expense/list")
def show_expense_list():

    selected_date = request.args.get("date", date.today().isoformat())

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
            WHERE expenses.date = ?
            ORDER BY expenses.id
        """

        params = (selected_date,)
        expenses = db.execute(sql, params).fetchall()

        return render_template("pages/expense_list.jinja", expenses=expenses, selected_date=selected_date)



@app.get("/expense/<int:expense_id>/delete")
def delete_expense(expense_id):
    with connect_db() as db:
        sql = """
            DELETE FROM expenses
            WHERE id=?
        """
        params = (expense_id,)
        db.execute(sql, params)
    
        flash("Delete Successfuly")
        return redirect("/expense/list")

@app.post("/expense/new")
def get_expense():

        # Get expense information from the submitted form
        category_id = request.form.get("category_id", "").strip()  
        amount = request.form.get("amount", "").strip()
        spend = request.form.get("spend", "").strip()
        date_td = request.form.get("date", "").strip()
        
        try:
            amount = int(amount)
            spend = float(spend)

            # Check valid expense values0:
            if amount <= 0 or spend <= 0:
                flash("Amount and spend must be greater than 0!")
                return redirect("/expense/new")

            # Calculate total expense
            total_spend = round(amount * spend, 2)

        except ValueError:
            flash("Please enter valid expense information!")
            return redirect("/expense/new")

        with connect_db() as db:

            # Save the total expense into the database
            sql="""
                INSERT INTO expenses (category_id, amount, spend, date)
                VALUES (?, ?, ?, ?)
            """

            params = (category_id, amount, total_spend, date_td)
            
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

@app.get("/target")
def show_target():

    today = date.today().isoformat()

    return render_template(
        "pages/target_set.jinja",
        today=today
    )

@app.post("/target")
def add_target():

    weekly_target = request.form.get("weekly_target", "").strip()
    date_week_start = request.form.get("date_week_start", "").strip()

    with connect_db() as db:

        sql = """
            UPDATE savings
            SET weekly_target = ?,
                date_week_start = ?
            WHERE id = 1
        """

        params = (weekly_target, date_week_start)

        db.execute(sql, params)

    flash("Weekly target updated successfully!")

    return redirect("/")

@app.post("/budget/update")
def new_budget():

    initial_budget = request.form.get("initial_budget", "").strip()

    if not initial_budget.isdigit():
        flash("Please enter a valid budget!")
        return redirect("/")

    initial_budget = int(initial_budget)

    with connect_db() as db:
        sql = """
            UPDATE savings
            SET initial_budget = ?
            WHERE id = 1
        """

        db.execute(sql, (initial_budget,))

    flash("Budget updated successfully!")
    return redirect("/")


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
