from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.bitacora import BitacoraCreate, BitacoraOut
from app.crud import bitacora as crud

router = APIRouter(prefix="/bitacora", tags=["Bitácora"])

@router.get("/", response_model=list[BitacoraOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await crud.get_all(db)

@router.get("/{bitacora_id}", response_model=BitacoraOut)
async def obtener(bitacora_id: int, db: AsyncSession = Depends(get_db)):
    dato = await crud.get_by_id(db, bitacora_id)
    if not dato:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return dato

@router.post("/", response_model=BitacoraOut)
async def registrar(data: BitacoraCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, data)
