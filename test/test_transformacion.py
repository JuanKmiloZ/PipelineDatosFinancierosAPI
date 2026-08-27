import pandas
from app.transformacion.limpieza import limpiar_datos


def test_elimina_datos_incorrectos():
  # DataFrame with valid rows and one invalid row (negative Open price)
  datos = pandas.DataFrame({
      "Open": [100, -20, 110],
      "High": [105, 100, 115],
      "Low": [95, 90, 105],
      "Close": [102, 95, 112],
      "Volume": [1000, 2000, 3000],
  })

  resultado = limpiar_datos(datos)

  # Verify that the invalid row is dropped, leaving 2 valid records
  assert len(resultado) == 2