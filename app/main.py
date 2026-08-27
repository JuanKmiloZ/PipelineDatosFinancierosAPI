from fastapi import FastAPI,Request
from app.Basededatos import crear_tablas
from app.etl.proceso import ejecutar_etl


###########################################
# HEALTH CHECK
###########################################

crear_tablas()            # Create tables

app=FastAPI()             # Create it the application

@app.get("/health")       # When some execute a GET in health, execute a funtion

def health():
    return {"status": "ok"}


###########################################
#  SYNC ETL ENDPOINT
###########################################

@app.post("/etl/sync")
async def sincronizar(request: Request):

  datos = await request.json()                 # Get request body data in JSON format
   
  tickers = datos["tickers"]                  # Extract parameters from the request payload
  fecha_inicio = datos["fecha_inicio"]
  fecha_fin = datos["fecha_fin"]

  ejecutar_etl(
     tickers,
       fecha_inicio,
         fecha_fin
         )                                         # Run the full ETL

  return {
     "status": "ok", 
     "message": "ETL ejecutado correctamente"
     }                                                  # Return success response