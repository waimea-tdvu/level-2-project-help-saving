#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class ExpensesTable:

    NAME = "Expenses"

    SCHEMA = """
        CREATE TABLE Expenses (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            bank  INTERGER,
            current_savings    INTERGER,
            weekly_targer  INTERGER,
            date_week_start DATE
        )
    """

    SEED_DATA = """
        INSERT INTO Expenses (category_id, amount, spend)
        VALUES
            ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
            ("Bank", 0, "Milk\nBread\nEggs\nCheese"),
            ("Weekly Target", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
            ("Current Savings", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy"),
            ("Date",    1, "Remember to backup your database regularly.")
    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Expenses : The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    ExpensesTable,
    # Add more tables here...
]

