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

class MenuTable:

    NAME = "menu"

    SCHEMA = """
        CREATE TABLE menu (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            bank  INTEGER,
            current_savings    INTEGER,
            weekly_target  INTEGER,
            date_week_start TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO menu ( id, bank, current_savings, weekly_target, date_week_start)
        VALUES
            (1, 1000, 200, 250, "30-08-2026")
    """

# Add more table classes here...
class CategoryTable:

    NAME = "categories"

    SCHEMA = """
        CREATE TABLE categories (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT,
            icon    TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO categories (id, name, icon)
        VALUES
            (1, "Food",  "🍔"),
            (2, "Movie", "🎬")
    """

class ExpensesTable:

    NAME = "expenses"

    SCHEMA = """
        CREATE TABLE expenses (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id  INTEGER,
            amount INTEGER,
            spend DECIMAL,
            date TEXT,
            FOREIGN KEY (category_id) REFERENCES Category(id)
        )
    """

    SEED_DATA = """
        INSERT INTO expenses (id, category_id, amount, spend, date )
        VALUES
            (1, 1, 2, 10, "2026-08-31"),
            (2, 2, 1, 8,  "2026-08-31"),
            (3, 2, 1, 5,  "2026-08-31"),
            (4, 1, 4, 2,  "2026-08-31")
    """

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
    MenuTable,
    CategoryTable,
    ExpensesTable

    # Add more tables here...
]

