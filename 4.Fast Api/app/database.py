from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

DATABASE_URL = os.getenv("DATABASE_URL")  # Ejemplo: "mysql+pymysql://usuario_api:contraseña_segura@localhost/libros_db"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # Ayuda a manejar conexiones inactivas
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Función para crear las tablas
def create_tables():
    from app.models import book  # Importar modelos
    Base.metadata.create_all(bind=engine)
