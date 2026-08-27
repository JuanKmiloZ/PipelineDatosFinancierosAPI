import pandas as pd
from app.Basededatos import obtener_conexion


################################
# GET HISTORY
################################

def obtener_historial(ticker, start_date=None, end_date=None, limit=100, offset=0):
  # What it does: Fetches paginated and filtered daily historical prices for a specific ticker.
  # Open database connection
  conexion = obtener_conexion()

  # Base SQL query to fetch ticker prices
  consulta = """
        SELECT date, open, high, low, close, volume, daily_return
        FROM stock_daily_prices
        INNER JOIN tickers
        ON stock_daily_prices.ticker_id = tickers.id
        WHERE tickers.symbol = ?
    """

  # Initialize parameters list with the ticker
  parametros = [ticker]

  # Add start date filter if provided
  if start_date:
    consulta += " AND date >= ?"
    parametros.append(start_date)

  # Add end date filter if provided
  if end_date:
    consulta += " AND date <= ?"
    parametros.append(end_date)

  # Add date sorting and pagination limits
  consulta += " ORDER BY date LIMIT ? OFFSET ?"
  parametros.extend([limit, offset])

  # Execute query and load results into a Pandas DataFrame
  datos = pd.read_sql_query(consulta, conexion, params=parametros)

  # Close database connection
  conexion.close()

  # Convert DataFrame to a list of dictionaries for the API
  return datos.to_dict(orient="records")


################################
# GET SUMMARY
################################

def obtener_resumen():
  # What it does: Calculates global financial metrics (min/max price, average volume, cumulative return) for all tickers.
  # Open database connection
  conexion = obtener_conexion()

  # Query to fetch all prices and volumes for all tickers
  consulta = """
        SELECT
            tickers.symbol,
            stock_daily_prices.close,
            stock_daily_prices.volume
        FROM stock_daily_prices
        INNER JOIN tickers
        ON stock_daily_prices.ticker_id = tickers.id
        ORDER BY tickers.symbol, stock_daily_prices.date
    """

  # Load all price data into a DataFrame
  datos = pd.read_sql_query(consulta, conexion)

  # Close database connection
  conexion.close()

  # Initialize list to store summaries
  resumen = []

  # Group data by ticker symbol to compute metrics
  for ticker, grupo in datos.groupby("symbol"):
    # Get initial and final prices to calculate return
    precio_inicial = grupo["close"].iloc[0]
    precio_final = grupo["close"].iloc[-1]

    # Append calculated metrics dictionary to the summary list
    resumen.append({
        "ticker": ticker,
        "minimum_price": grupo["close"].min(),
        "maximum_price": grupo["close"].max(),
        "average_volume": grupo["volume"].mean(),
        "cumulative_return": (
            (precio_final - precio_inicial) / precio_inicial
        ),
    })

  return resumen




##################################
# GET MOVING AVERAGE
##################################

def obtener_media_movil(ticker, window_size):
  # What it does: Computes a rolling moving average on closing prices for a given ticker and window size.
  # Open database connection
  conexion = obtener_conexion()

  # Query dates and closing prices for a specific ticker
  consulta = """
        SELECT date, close
        FROM stock_daily_prices
        INNER JOIN tickers
        ON stock_daily_prices.ticker_id = tickers.id
        WHERE tickers.symbol = ?
        ORDER BY date
    """

  # Load data into a DataFrame
  datos = pd.read_sql_query(consulta, conexion, params=[ticker])

  # Close database connection
  conexion.close()

  
  datos["moving_average"] = datos["close"].rolling(window_size).mean()       # Calculate rolling moving average using the window size

  datos["moving_average"] = datos["moving_average"].fillna(0)    # Convert resulting DataFrame to a list of dictionaries
  
  return datos.to_dict(orient="records")
