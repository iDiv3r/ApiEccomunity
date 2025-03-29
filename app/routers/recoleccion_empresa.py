from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.recoleccion_empresa import (
    RecoleccionEmpresaCreate, RecoleccionEmpresaUpdate, RecoleccionEmpresaOut
)
from app.crud import recoleccion_empresa as crud

router = APIRouter(prefix="/recolecciones-empresa", tags=["Recolecciones de Empresas"])

@router.get("/", response_model=list[RecoleccionEmpresaOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await crud.get_all(db)

@router.get("/{reco_id}", response_model=RecoleccionEmpresaOut)
async def obtener(reco_id: int, db: AsyncSession = Depends(get_db)):
    dato = await crud.get_by_id(db, reco_id)
    if not dato:
        raise HTTPException(status_code=404, detail="Recolección no encontrada")
    return dato

@router.post("/", response_model=RecoleccionEmpresaOut)
async def crear(data: RecoleccionEmpresaCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, data)

@router.put("/{reco_id}", response_model=RecoleccionEmpresaOut)
async def actualizar(reco_id: int, data: RecoleccionEmpresaUpdate, db: AsyncSession = Depends(get_db)):
    actualizado = await crud.update(db, reco_id, data)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return actualizado

@router.delete("/{reco_id}")
async def eliminar(reco_id: int, db: AsyncSession = Depends(get_db)):
    eliminado = await crud.delete(db, reco_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"ok": True, "mensaje": "Recolección eliminada correctamente"}
