# librery incluide in python, no update
import sqlite3

# Name BD
BASE_DATOS="datos_finanzas.db"

# Function for open conexion
def obtener_conexion():
    conexion=sqlite3.connect(BASE_DATOS)
    return conexion


# Create tables
def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

#save the tags
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT UNIQUE
        )
    """)

# Save the prices
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_daily_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker_id INTEGER,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL,
            daily_return REAL,
            UNIQUE(ticker_id, date),
            FOREIGN KEY (ticker_id) REFERENCES tickers(id)
        )
    """)

    conexion.commit()
    conexion.close()