from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.horario_recoleccion import HorarioCreate, HorarioUpdate, HorarioOut
from app.crud import horario_recoleccion as crud

router = APIRouter(prefix="/horarios", tags=["Horarios de Recolección"])

@router.get("/", response_model=list[HorarioOut])
async def listar_horarios(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_horarios(db)

@router.get("/{horario_id}", response_model=HorarioOut)
async def obtener_horario(horario_id: int, db: AsyncSession = Depends(get_db)):
    horario = await crud.get_horario_by_id(db, horario_id)
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return horario

@router.post("/", response_model=HorarioOut)
async def crear_horario(horario: HorarioCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_horario(db, horario)

@router.put("/{horario_id}", response_model=HorarioOut)
async def actualizar_horario(horario_id: int, horario: HorarioUpdate, db: AsyncSession = Depends(get_db)):
    actualizado = await crud.update_horario(db, horario_id, horario)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return actualizado

@router.delete("/{horario_id}")
async def eliminar_horario(horario_id: int, db: AsyncSession = Depends(get_db)):
    eliminado = await crud.delete_horario(db, horario_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return {"ok": True, "mensaje": "Horario eliminado correctamente"}
