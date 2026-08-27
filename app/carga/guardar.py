from app.Basededatos import obtener_conexion
import pandas


#######################################
# GUARDAR TICKER
#######################################


def guardar_ticker(simbolo):  # Open the conexion and the cursor for BD
  conexion = obtener_conexion()
  cursor = conexion.cursor()

  cursor.execute(  # Save the simbol
      """
        INSERT OR IGNORE INTO tickers (symbol)
        VALUES (?)
    """,
      (simbolo,),
  )
  conexion.commit()

  cursor.execute(  # Consult the ID the corresponding to each ticker
      """
        SELECT id
        FROM tickers
        WHERE symbol = ?
    """,
      (simbolo,),
  )
  ticker_id = cursor.fetchone()[0]

  conexion.close()  # Close the conexion and return id
  return ticker_id


#######################
# GUARDAR PRECIOS
#######################


def guardar_precios(datos, ticker_id):

  conexion = obtener_conexion()  # Open the conexion for save prices
  cursor = conexion.cursor()

  for fecha, fila in datos.iterrows():  # Iterate datafram file for file

    # Helper function to clean series/values and avoid TypeError
    def limpiar(valor):
      if hasattr(valor, "iloc"):
        valor = valor.iloc[0]
      return float(valor) if pandas.notna(valor) and str(valor).strip() != "" else None

    def limpiar_volumen(valor):
      if hasattr(valor, "iloc"):
        valor = valor.iloc[0]
      return (
          int(float(valor))
          if pandas.notna(valor) and str(valor).strip() != ""
          else None
      )

    cursor.execute(
        """
            INSERT OR REPLACE INTO stock_daily_prices
            (ticker_id, date, open, high, low, close, volume, daily_return)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ticker_id,
            str(fecha.date()),
            limpiar(fila["Open"]),
            limpiar(fila["High"]),
            limpiar(fila["Low"]),
            limpiar(fila["Close"]),
            limpiar_volumen(fila["Volume"]),
            limpiar(fila["Daily Return"]),
        ),
    )

  conexion.commit()  # Save and close conexion
  conexion.close()