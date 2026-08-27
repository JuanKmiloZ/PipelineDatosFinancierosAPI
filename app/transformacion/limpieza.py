def limpiar_datos(datos):

    datos = datos.dropna()

    datos = datos[
        (datos["Open"] > 0) &
        (datos["High"] > 0) &
        (datos["Low"] > 0) &
        (datos["Close"] > 0) &
        (datos["Volume"] >= 0)
    ]

    datos = datos[datos["Low"] <= datos["High"]]

    return datos


