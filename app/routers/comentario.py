from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.comentario import ComentarioCreate, ComentarioUpdate, ComentarioOut
from app.crud import comentario as crud

router = APIRouter(prefix="/comentarios", tags=["Comentarios"])

@router.get("/", response_model=list[ComentarioOut])
async def listar(db: AsyncSession = Depends(get_db)):
    return await crud.get_all(db)

@router.get("/{comentario_id}", response_model=ComentarioOut)
async def obtener(comentario_id: int, db: AsyncSession = Depends(get_db)):
    dato = await crud.get_by_id(db, comentario_id)
    if not dato:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return dato

@router.post("/", response_model=ComentarioOut)
async def crear(data: ComentarioCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, data)

@router.put("/{comentario_id}", response_model=ComentarioOut)
async def actualizar(comentario_id: int, data: ComentarioUpdate, db: AsyncSession = Depends(get_db)):
    actualizado = await crud.update(db, comentario_id, data)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return actualizado

@router.delete("/{comentario_id}")
async def eliminar(comentario_id: int, db: AsyncSession = Depends(get_db)):
    eliminado = await crud.delete(db, comentario_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return {"ok": True, "mensaje": "Comentario eliminado correctamente"}
