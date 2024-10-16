import json
from datetime import datetime
from models import Estudiante

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Estudiante):
            return {
                "nombre": obj.nombre,
                "edad": obj.edad,
                "carrera": obj.carrera
            }
        return super().default(obj)

def serializar_objeto(obj):
    return json.dumps(obj, cls=CustomEncoder, indent=4, ensure_ascii=False)
