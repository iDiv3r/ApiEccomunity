from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.empresa_tiporeciclaje import AsignacionTipo, AsignacionOut
from app.crud import empresa_tiporeciclaje as crud

router = APIRouter(prefix="/empresa-tipo", tags=["Empresa - Tipos de Reciclaje"])

@router.post("/", response_model=AsignacionOut)
async def asignar_tipo_reciclaje(asignacion: AsignacionTipo, db: AsyncSession = Depends(get_db)):
    return await crud.asignar_tipo(db, asignacion)

@router.delete("/")
async def desasignar_tipo(id_Empresa: int, id_TipoReciclaje: int, db: AsyncSession = Depends(get_db)):
    eliminado = await crud.desasignar_tipo(db, id_Empresa, id_TipoReciclaje)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return {"ok": True, "mensaje": "Asignación eliminada correctamente"}

@router.get("/empresa/{empresa_id}", response_model=list[AsignacionOut])
async def obtener_asignaciones(empresa_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.obtener_asignaciones_por_empresa(db, empresa_id)
