from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.tipo_reciclaje import TipoReciclaje
from app.schemas.tipo_reciclaje import TipoReciclajeCreate, TipoReciclajeUpdate

async def get_all_tipos(db: AsyncSession):
    result = await db.execute(select(TipoReciclaje))
    return result.scalars().all()

async def get_tipo_by_id(db: AsyncSession, tipo_id: int):
    result = await db.execute(select(TipoReciclaje).where(TipoReciclaje.Id == tipo_id))
    return result.scalar_one_or_none()

async def create_tipo(db: AsyncSession, tipo: TipoReciclajeCreate):
    nuevo = TipoReciclaje(**tipo.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

async def update_tipo(db: AsyncSession, tipo_id: int, data: TipoReciclajeUpdate):
    tipo = await get_tipo_by_id(db, tipo_id)
    if tipo:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(tipo, key, value)
        await db.commit()
        await db.refresh(tipo)
    return tipo

async def delete_tipo(db: AsyncSession, tipo_id: int):
    tipo = await get_tipo_by_id(db, tipo_id)
    if tipo:
        await db.delete(tipo)
        await db.commit()
    return tipo
