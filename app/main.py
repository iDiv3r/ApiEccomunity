from fastapi import FastAPI
from app.routers import (
    empresa, usuario, punto_recoleccion, horario_recoleccion,
    recoleccion_usuario, tipo_reciclaje, empresa_tiporeciclaje,
    recoleccion_empresa, publicacion, comentario, bitacora,medalla
)

app = FastAPI(title="API de Recolección")

# Registrar todos los routers
app.include_router(empresa.router)
app.include_router(usuario.router)
app.include_router(punto_recoleccion.router)
app.include_router(horario_recoleccion.router)
app.include_router(recoleccion_usuario.router)
app.include_router(tipo_reciclaje.router)
app.include_router(empresa_tiporeciclaje.router)
app.include_router(recoleccion_empresa.router)
app.include_router(publicacion.router)
app.include_router(comentario.router)
app.include_router(bitacora.router)
app.include_router(medalla.router)


@app.get("/")
async def root():
    return {"mensaje": "Bienvenido a la API de recolección"}
