## Nombre del Proyecto : PipelineDatosFinancierosAPI

API REST desarrollada en Python para procesar y consultar datos financieros.

## Tecnologías
Python
FastAPI
SQLite
yfinancie(no se utiliza el as)
pandas(no se utiliza el as)
Git/Github
Entorno virtual (venv)
Visual estudio Code


## Estructura del proyecto

PipelineDatosFinancierosAPI/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── Basededatos.py
│   │
│   ├── extraccion/
│   │   └── yahoo.py
│   │
│   ├── transformacion/
│   │   └── limpieza.py
│   │
│   ├── carga/
│   │   └── guardar.py
│   │
│   ├── etl/
│   │   └── proceso.py
│   │
│   └── consultas/
│       └── consultas.py
│
├── test/
│   ├── test_transformacion.py
│   └── test_etl.py
│
├── venv/
│
├── .gitignore
├── README.md
├── TEORIA.md
├── pytest.ini
├── requirements.txt
└── datos_finanzas.db


## Funcionalidad actual
1. API REST básica.
2. Endpoint GET /health para verificar el estado del servicio.
3. Creación de una base de datos SQLite, con dos entidades (tickers y stockdailyprices)
4. Extracción de Datos históricos con yfinancie
5. limpieza de Datos 
6. Cálculo: Daily Return
7. Carga de Datos Sqllite 
8. Edpoint (POST /etl/sync) para ejecutar el ETL
9. Consulta de ticker (Histórico -Resumen)

## Estado

Proyecto en desarrollo como parte de una prueba técnica para desarrollador Python.

 
## Paso siguiente:

Pruebas integración proyecto

## Estado Pruebas

- check health ok
- check sync ok
- transformación ok
- Prueba ETL con mock ok
- Validar todos los endpoints ok
- Calculo media movil 
- Revisión final

## Entorno

Se crea entorno virtual denominado (venv), se activa con:

"""venv\Scripts\activate"""

ejecutar API:

"""uvicorn app.main:app --reload"""

Documentacion:

"""http://127.0.0.1:8000/docs"""

## Docker

Como configuración futura, el proyecto puede ejecutarse con Docker creando un `Dockerfile` y una imagen del proyecto.

Comandos básicos:

```bash
docker build -t pipeline-finanzas .
docker run -p 8000:8000 pipeline-finanzas