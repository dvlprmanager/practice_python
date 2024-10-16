from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo!"}

@app.get("/saludo/{nombre}")
def read_item(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}
