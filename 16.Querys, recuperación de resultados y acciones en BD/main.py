from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error
from typing import List, Optional
from dotenv import load_dotenv
import os
from loguru import logger

# Cargar variables de entorno desde .env
load_dotenv()

app = FastAPI()

# Importar el logger configurado
from logger import logger

# Importar excepciones personalizadas
from exceptions import DatabaseConnectionError, ItemNotFoundError

# Modelos Pydantic
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

# Función para obtener la conexión a la base de datos
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_DATABASE', 'testdb'),
            user=os.getenv('DB_USER', 'tu_usuario'),
            password=os.getenv('DB_PASSWORD', 'tu_contraseña')
        )
        if connection.is_connected():
            logger.info("Conexión a la base de datos establecida")
            return connection
    except Error as e:
        logger.error(f"Error al conectar a la base de datos: {e}")
        raise DatabaseConnectionError(detail=str(e))

# Controlador de excepciones global para HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"HTTPException: {exc.detail} - Path: {request.url.path}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Controlador de excepciones global para excepciones no controladas
@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {exc} - Path: {request.url.path}")
    return JSONResponse(
        status_code=500,
        content={"message": "Ocurrió un error inesperado"},
    )

# Ruta para crear un nuevo ítem
@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        insert_query = "INSERT INTO items (name, description, price) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (item.name, item.description, item.price))
        connection.commit()
        item_id = cursor.lastrowid
        logger.info(f"Ítem creado con ID: {item_id}")
        return {**item.dict(), "id": item_id}
    except Error as e:
        logger.error(f"Error al crear ítem: {e}")
        raise HTTPException(status_code=500, detail="Error al crear el ítem")
    finally:
        cursor.close()
        connection.close()
        logger.info("Conexión a la base de datos cerrada tras crear ítem")

# Ruta para obtener todos los ítems
@app.get("/items/", response_model=List[Item])
def read_items():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        select_query = "SELECT * FROM items"
        cursor.execute(select_query)
        result = cursor.fetchall()
        logger.info(f"Recuperados {len(result)} ítems")
        return result
    except Error as e:
        logger.error(f"Error al obtener ítems: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener los ítems")
    finally:
        cursor.close()
        connection.close()
        logger.info("Conexión a la base de datos cerrada tras obtener ítems")

# Ruta para obtener un ítem por su ID
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        select_query = "SELECT * FROM items WHERE id = %s"
        cursor.execute(select_query, (item_id,))
        result = cursor.fetchone()
        if result:
            logger.info(f"Ítem encontrado: ID {item_id}")
            return result
        else:
            logger.warning(f"Ítem no encontrado: ID {item_id}")
            raise ItemNotFoundError(item_id=item_id)
    except Error as e:
        logger.error(f"Error al obtener ítem: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener el ítem")
    finally:
        cursor.close()
        connection.close()
        logger.info("Conexión a la base de datos cerrada tras obtener ítem")

# Ruta para actualizar un ítem por su ID
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        # Obtener el ítem existente
        select_query = "SELECT * FROM items WHERE id = %s"
        cursor.execute(select_query, (item_id,))
        existing_item = cursor.fetchone()
        if not existing_item:
            logger.warning(f"Ítem no encontrado para actualizar: ID {item_id}")
            raise ItemNotFoundError(item_id=item_id)
        
        # Actualizar los campos proporcionados
        updated_item = existing_item.copy()
        if item.name is not None:
            updated_item['name'] = item.name
        if item.description is not None:
            updated_item['description'] = item.description
        if item.price is not None:
            updated_item['price'] = item.price
        
        # Actualizar en la base de datos
        update_query = """
            UPDATE items 
            SET name = %s, description = %s, price = %s 
            WHERE id = %s
        """
        cursor.execute(update_query, (
            updated_item['name'],
            updated_item['description'],
            updated_item['price'],
            item_id
        ))
        connection.commit()
        logger.info(f"Ítem actualizado: ID {item_id}")
        return updated_item
    except Error as e:
        logger.error(f"Error al actualizar ítem: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar el ítem")
    finally:
        cursor.close()
        connection.close()
        logger.info("Conexión a la base de datos cerrada tras actualizar ítem")

# Ruta para eliminar un ítem por su ID
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        delete_query = "DELETE FROM items WHERE id = %s"
        cursor.execute(delete_query, (item_id,))
        connection.commit()
        affected_rows = cursor.rowcount
        if affected_rows == 0:
            logger.warning(f"Ítem no encontrado para eliminar: ID {item_id}")
            raise ItemNotFoundError(item_id=item_id)
        logger.info(f"Ítem eliminado: ID {item_id}")
        return {"message": "Ítem eliminado correctamente"}
    except Error as e:
        logger.error(f"Error al eliminar ítem: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar el ítem")
    finally:
        cursor.close()
        connection.close()
        logger.info("Conexión a la base de datos cerrada tras eliminar ítem")
