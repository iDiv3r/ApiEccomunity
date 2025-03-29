from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.recoleccion_usuario import RecoleccionCreate, RecoleccionUpdate, RecoleccionOut
from app.crud import recoleccion_usuario as crud

router = APIRouter(prefix="/recolecciones", tags=["Recolecciones de Usuarios"])

@router.get("/", response_model=list[RecoleccionOut])
async def listar_recolecciones(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_recolecciones(db)

@router.get("/{reco_id}", response_model=RecoleccionOut)
async def obtener_recoleccion(reco_id: int, db: AsyncSession = Depends(get_db)):
    reco = await crud.get_recoleccion_by_id(db, reco_id)
    if not reco:
        raise HTTPException(status_code=404, detail="Recolección no encontrada")
    return reco

@router.post("/", response_model=RecoleccionOut)
async def crear_recoleccion(reco: RecoleccionCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_recoleccion(db, reco)

@router.put("/{reco_id}", response_model=RecoleccionOut)
async def actualizar_recoleccion(reco_id: int, reco: RecoleccionUpdate, db: AsyncSession = Depends(get_db)):
    actualizado = await crud.update_recoleccion(db, reco_id, reco)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Recolección no encontrada")
    return actualizado

@router.delete("/{reco_id}")
async def eliminar_recoleccion(reco_id: int, db: AsyncSession = Depends(get_db)):
    eliminado = await crud.delete_recoleccion(db, reco_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Recolección no encontrada")
    return {"ok": True, "mensaje": "Recolección eliminada correctamente"}
