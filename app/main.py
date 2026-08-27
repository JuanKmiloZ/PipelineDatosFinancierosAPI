from fastapi import FastAPI
from pydantic import BaseModel  # <-- Importamos BaseModel
from app.Basededatos import crear_tablas
from app.etl.proceso import ejecutar_etl



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