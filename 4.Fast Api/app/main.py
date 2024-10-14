# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.database import create_tables  # Asegúrate de importar esta función

app = FastAPI(
    title="API de Gestión de Libros",
    description="Una API RESTful para gestionar libros utilizando FastAPI y MySQL",
    version="1.0.0",
)

# Crear las tablas al iniciar la aplicación
# create_tables()

# Configuración de CORS (opcional)
origins = [
    "http://localhost",
    "http://localhost:8000",
    # Agrega otros orígenes permitidos según sea necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


