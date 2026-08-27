import pandas

def limpiar_datos(datos):

    df = datos.copy()            # Copy data original
    df = df.dropna()             # Delete data empty

    datos = datos[               # filter prices
        (datos["Low"] <= datos["High"]) &
        (datos["Volume"] >= 0) &
        (datos["Open"] > 0) &
        (datos["High"] > 0) &
        (datos["Low"] > 0) &
        (datos["Close"] > 0)

    ]

    df["Daily Return"] = df["Close"].pct_change()           # Dialy performance

    return df
    


