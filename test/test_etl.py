from unittest.mock import patch
from app.etl.proceso import ejecutar_etl


def test_etl_con_datos_falsos():
  # Mock dataset with valid fake records to test the full ETL flow
  datos_falsos = [{
      "Date": "2026-08-01",
      "Open": 100,
      "High": 110,
      "Low": 90,
      "Close": 105,
      "Volume": 1000,
  }, {
      "Date": "2026-08-02",
      "Open": 105,
      "High": 115,
      "Low": 100,
      "Close": 110,
      "Volume": 1200,
  }]

  # Patch the data extraction function to return mock data instead of calling Yahoo Finance
  with patch("app.etl.proceso.obtener_datos", return_value=datos_falsos):

    resultado = ejecutar_etl(["AAPL"], "2026-08-01", "2026-08-02")

    # Verify that the ETL pipeline executes successfully and returns a result
    assert resultado is not None