from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.punto_recoleccion import PuntoCreate, PuntoUpdate, PuntoOut
from app.crud import punto_recoleccion as crud

router = APIRouter(prefix="/puntos", tags=["Puntos de Recolección"])

@router.get("/", response_model=list[PuntoOut])
async def listar_puntos(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_puntos(db)

@router.get("/{punto_id}", response_model=PuntoOut)
async def obtener_punto(punto_id: int, db: AsyncSession = Depends(get_db)):
    punto = await crud.get_punto_by_id(db, punto_id)
    if not punto:
        raise HTTPException(status_code=404, detail="Punto no encontrado")
    return punto

@router.post("/", response_model=PuntoOut)
async def crear_punto(punto: PuntoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_punto(db, punto)

@router.put("/{punto_id}", response_model=PuntoOut)
async def actualizar_punto(punto_id: int, punto: PuntoUpdate, db: AsyncSession = Depends(get_db)):
    actualizado = await crud.update_punto(db, punto_id, punto)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Punto no encontrado")
    return actualizado

@router.delete("/{punto_id}")
async def eliminar_punto(punto_id: int, db: AsyncSession = Depends(get_db)):
    punto = await crud.delete_punto(db, punto_id)
    if not punto:
        raise HTTPException(status_code=404, detail="Punto no encontrado")
    return {"ok": True, "mensaje": "Punto eliminado correctamente"}
