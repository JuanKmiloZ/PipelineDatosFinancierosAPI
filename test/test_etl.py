import pandas
from unittest.mock import patch
from app.etl.proceso import ejecutar_etl


def test_etl_con_datos_falsos():
  # Nombramos explícitamente la variable como 'datos_mock' para identificarla
  datos_mock = pandas.DataFrame({
      "Open": [100, 105],
      "High": [105, 110],
      "Low": [95, 100],
      "Close": [102, 108],
      "Volume": [1000, 2000],
  })

  datos_mock.index = pandas.to_datetime(["2025-01-01", "2025-01-02"])

  # Le pasamos nuestro mock al patch
  with patch("app.etl.proceso.obtener_datos", return_value=datos_mock):
    resultado = ejecutar_etl(["AAPL"], "2025-01-01", "2025-01-02")

    assert resultado is not None