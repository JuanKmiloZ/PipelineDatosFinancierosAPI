from app.transformacion.limpieza import limpiar_datos


def test_elimina_datos_incorrectos():
  # Test dataset with one valid row and one invalid row (High < Low)
  datos = [{
      "Date": "2026-08-01",
      "Open": 100,
      "High": 110,
      "Low": 90,
      "Close": 105,
      "Volume": 1000,
  }, {
      "Date": "2026-08-02",
      "Open": 100,
      "High": 90,
      "Low": 100,
      "Close": 95,
      "Volume": 1000,
  }]

  resultado = limpiar_datos(datos)

  # Validate that the incorrect row is removed and only the valid one remains
  assert len(resultado) == 1
  assert resultado[0]["Date"] == "2026-08-01"