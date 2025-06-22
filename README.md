# CMDB API – API RESTful para Elementos de Configuración (CIs)

## Descripción

Esta API permite registrar, consultar, actualizar y eliminar elementos de configuración (CIs) dentro de una CMDB (Configuration Management Database), con relaciones entre componentes, etiquetado por ambiente y auditoría básica.

## Tecnologías Utilizadas

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- Uvicorn

## Instalación

1. Clonar el repositorio:

   git clone https://github.com/NeryJim21/SA-T3  
   cd SA-T3

2. Crear un entorno virtual:

   python3 -m venv venv  
   source venv/bin/activate

3. Instalar dependencias:

   pip install -r requirements.txt

4. Crear base de datos PostgreSQL:

   CREATE DATABASE cmdb;  
   ALTER USER postgres WITH PASSWORD 'postgres';

5. Editar el archivo de conexión en `app/database.py`:

   DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/cmdb"

## Ejecución del Servidor

1. Ejecutar el servidor con Uvicorn:

   uvicorn app.main:app --reload

2. Acceder a la documentación interactiva:

   Swagger: http://localhost:8000/docs  
   OpenAPI JSON: http://localhost:8000/openapi.json

## Cargar Datos Iniciales (Seed)

Ejecutar el script:

   python3 -m app.seed

## Pruebas Unitarias

Ejecutar pruebas con Pytest:

   pytest

## Endpoints Principales

| Método | Ruta            | Descripción                  |
|--------|------------------|------------------------------|
| GET    | /cis/            | Listar todos los CIs         |
| POST   | /cis/            | Crear un nuevo CI            |
| GET    | /cis/{id}        | Obtener un CI específico     |
| PUT    | /cis/{id}        | Actualizar un CI             |
| DELETE | /cis/{id}        | Eliminar un CI               |
| POST   | /relaciones/     | Crear relación entre CIs     |
| GET    | /relaciones/     | Listar relaciones entre CIs  |

## Diagrama ER

Incluye dos tablas principales:

- `configuration_items`: representa los elementos de configuración.
- `relaciones_ci`: permite definir dependencias o conexiones entre CIs (padre/hijo).


   ![Diagrama ER](./img/er.svg)

## Estado del Proyecto

- [x] CRUD de CIs
- [x] Relación entre CIs (padre/hijo)
- [x] Etiquetado por ambiente (DEV, QA, PROD)
- [x] Auditoría básica (fecha de cambio, descripción)
- [x] Documentación Swagger
- [x] Pruebas unitarias básicas
- [ ] Filtros avanzados por tipo, estado, ambiente
- [ ] Validación condicional por tipo de CI
- [ ] Exportación de CIs (CSV, Excel)
- [ ] Autenticación de usuarios
