import yfinance


def obtener_datos(ticker, fecha_inicio, fecha_fin): #Dowload the prices based on the date range 
    datos=yfinance.download(
        ticker,
            start=fecha_inicio,
            end=fecha_fin,
            auto_adjust=False # Without transformation, generic data
    )

    return datos # Return Dataframe with information
