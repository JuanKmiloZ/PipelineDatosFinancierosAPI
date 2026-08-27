from app.Basededatos import obtener_conexion


# ==========================================
# GUARDAR TICKER
# ==========================================

def guardar_ticker(simbolo):                     # Open the conexion and the cursor for BD
  conexion = obtener_conexion()
  cursor = conexion.cursor()

  cursor.execute(                                # Save the simbol

      """
        INSERT OR IGNORE INTO tickers (symbol)
        VALUES (?)
    """,
      (simbolo,),
  )
  conexion.commit()



  cursor.execute(                          # Consult the ID the corresponding to each ticker
      """
        SELECT id
        FROM tickers
        WHERE symbol = ?
    """,
      (simbolo,),
  )
  ticker_id = cursor.fetchone()[0]


  conexion.close()              #Close the conexion and return id
  return ticker_id



# ==========================================
# GUARDAR PRECIOS
# ==========================================

def guardar_precios(datos, ticker_id):
  
  conexion = obtener_conexion()           # Open the conexion for save prices
  cursor = conexion.cursor()

  for fecha, fila in datos.iterrows():      # Iterate datafram file for file
    cursor.execute(
        """
            INSERT OR REPLACE INTO stock_daily_prices
            (ticker_id, date, open, high, low, close, volume, daily_return)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ticker_id,
            str(fecha.date()),
            float(fila["Open"]),
            float(fila["High"]),
            float(fila["Low"]),
            float(fila["Close"]),
            float(fila["Volume"]),
            (
                float(fila["Daily Return"])
                if fila["Daily Return"] == fila["Daily Return"]
                else None
            ),
        ),
    )

  
  conexion.commit()       # Save and close conexion
  conexion.close()


