## Nombre del Proyecto : PipelineDatosFinancierosAPI

API REST desarrollada en Python para procesar y consultar datos financieros.

## Tecnologías
Visual estudio Code
Python
FastAPI
SQLite
yfinancie(no se utiliza el as)
pandas(no se utiliza el as)

## Funcionalidad actual
1. API REST básica.
2. Endpoint GET /health para verificar el estado del servicio.
3. Creación de una base de datos SQLite, con dos entidades (tickers y stockdailyprices)
4. Extracción de Datos históricos con yfinancie
5. limpieza de Datos 
6. Cálculo: Daily Return
7. Carga de Datos Sqllite 
8. Edpoint (POST /etl/sync) para ejecutar el ETL
9. Extracción ok, Transformación ok, Carga ok de datos financieros
10. Consulta de ticker (Histórico -Resumen)

## Estado

Proyecto en desarrollo como parte de una prueba técnica para desarrollador Python.

## Paso siguiente:
Pruebas integración proyecto