from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.empresa import EmpresaOut, EmpresaCreate, EmpresaUpdate
from app.crud import empresa as crud

router = APIRouter(prefix="/empresas", tags=["Empresas"])

@router.get("/", response_model=list[EmpresaOut])
async def listar_empresas(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_empresas(db)

@router.get("/{empresa_id}", response_model=EmpresaOut)
async def obtener_empresa(empresa_id: int, db: AsyncSession = Depends(get_db)):
    empresa = await crud.get_empresa_by_id(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa

@router.post("/", response_model=EmpresaOut)
async def crear_empresa(empresa: EmpresaCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_empresa(db, empresa)

@router.put("/{empresa_id}", response_model=EmpresaOut)
async def actualizar_empresa(empresa_id: int, empresa: EmpresaUpdate, db: AsyncSession = Depends(get_db)):
    empresa_actualizada = await crud.update_empresa(db, empresa_id, empresa)
    if not empresa_actualizada:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa_actualizada

@router.delete("/{empresa_id}")
async def eliminar_empresa(empresa_id: int, db: AsyncSession = Depends(get_db)):
    empresa = await crud.delete_empresa(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return {"ok": True, "mensaje": "Empresa eliminada correctamente"}
