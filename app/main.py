from fastapi import FastAPI

# Create it the application
app=FastAPI()

# When some execute a GET in health, execute a funtion
@app.get("/health")
def health():
    return {"status": "ok"}