import pandas
from unittest.mock import patch

from app.etl.proceso import ejecutar_etl


def test_etl_con_datos_falsos():

    datos = pandas.DataFrame({
        "Open": [100, 105],
        "High": [105, 110],
        "Low": [95, 100],
        "Close": [102, 108],
        "Volume": [1000, 2000],
        "Daily Return": [0, 0.0588]
    })

    datos.index = pandas.to_datetime([
        "2025-01-01",
        "2025-01-02"
    ])

    with patch("app.etl.proceso.obtener_datos", return_value=datos):

        ejecutar_etl(
    ["AAPL"],
    "2025-01-01",
    "2025-01-02"
)