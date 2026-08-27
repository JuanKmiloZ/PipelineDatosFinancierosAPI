from app.carga.guardar import guardar_ticker, guardar_precios
from app.extraccion.yahoo import obtener_datos
from app.transformacion.limpieza import limpiar_datos


#####################################################
# EJECUTAR ETL
#####################################################

def ejecutar_etl(tickers, fecha_inicio, fecha_fin):

  
  
  for simbolo in tickers:    # Iterate each simbol of the list the ticters, one for one

    
    datos = obtener_datos(       #Extracción: Dowload the data financial of the web
        simbolo,
        fecha_inicio,
        fecha_fin
        )     

   
    datos = limpiar_datos(datos)                     # Transformación: Clean value empty, filter errors and especific calculate

    ticker_id = guardar_ticker(simbolo)              # Carga: Save the ticket in the BD and get your ID

    guardar_precios(datos, ticker_id)                  # Save all the prices cleaned in the table