import json
from models import Estudiante
from datetime import datetime

def crear_persona():
    persona = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Barcelona",
        "intereses": ["leer", "cocinar", "arte"]
    }
    return persona

def guardar_json(obj, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)
        print(f"Datos guardados en '{nombre_archivo}'")


def crear_lista_personas():
    personas = [
        crear_persona(),
        {
            "nombre": "Carlos",
            "edad": 30,
            "ciudad": "Madrid",
            "intereses": ["fútbol", "música", "viajar"]
        },
        {
            "nombre": "Lucía",
            "edad": 22,
            "ciudad": "Valencia",
            "intereses": ["fotografía", "bailar", "cine"]
        }
    ]
    return personas

def crear_evento():
    evento = {
        "titulo": "Concierto de Música",
        "fecha": datetime(2024, 5, 20, 19, 30),
        "ubicacion": "Palacio de Congresos",
        "organizador": Estudiante("Lucía", 22, "Ingeniería")
    }
    return evento