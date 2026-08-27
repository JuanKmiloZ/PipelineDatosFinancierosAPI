from fastapi import FastAPI
from app.Basededatos import crear_tablas

# Create tables
crear_tablas()

# Create it the application
app=FastAPI()

# When some execute a GET in health, execute a funtion
@app.get("/health")
def health():
    return {"status": "ok"}