from fastapi import HTTPException

class DatabaseConnectionError(HTTPException):
    def __init__(self, detail: str = "Error de conexion a la base de datos"):
        super().__init__(status_code=500, detail=detail)


class ItemNotFoundError(HTTPException): 
    def __init__(self, item_id: int):
        detail = f"Item con id {item_id} no encontrado"
        super().__init__(status_code=404, detail=detail)