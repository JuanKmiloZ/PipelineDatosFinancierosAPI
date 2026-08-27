from fastapi import FastAPI
from pydantic import BaseModel  # <-- Importamos BaseModel
from app.Basededatos import crear_tablas
from app.etl.proceso import ejecutar_etl
from app.consultas.consultas import (
    obtener_historial,
    obtener_resumen,
    obtener_media_movil
)

crear_tablas()            # Create tables
app=FastAPI()             # Create it the application


# ==========================================
# PYDANTIC MODEL FOR ETL PAYLOAD
# ==========================================
class EtlRequest(BaseModel):
  tickers: list[str]
  fecha_inicio: str
  fecha_fin: str

  

###########################################
# HEALTH CHECK
###########################################


@app.get("/health")       # When some execute a GET in health, execute a funtion

def health() -> dict:     # Specify that it returns a dictionary
    return {"status": "ok"}


###########################################
# SYNC ETL ENDPOINT
###########################################

@app.post("/etl/sync")
async def sincronizar(body: EtlRequest) -> dict:  # <-- Usamos el modelo aquí
  
  ejecutar_etl(body.tickers, body.fecha_inicio, body.fecha_fin)          # Ejecuta el ETL directamente extrayendo los datos validados del modelo
  return {"status": "ok", "message": "ETL ejecutado correctamente"}       # Return success response


###########################################
# STOCK HISTORY
###########################################

@app.get("/stocks/{ticker}/history")
def historial(
    ticker: str,
    start_date: str = None,
    end_date: str = None,
    limit: int = 100,
    offset: int = 0
):
    return obtener_historial(
        ticker,
        start_date,
        end_date,
        limit,
        offset
    )


###########################################
# ANALYTICS SUMMARY
###########################################

@app.get("/analytics/summary")
def resumen():
    return obtener_resumen()


###########################################
# MOVING AVERAGE
###########################################

@app.get("/analytics/moving_average")
def media_movil(ticker: str, window_size: int):
    return obtener_media_movil(ticker, window_size)