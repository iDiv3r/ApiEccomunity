from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.bitacora import Bitacora
from app.schemas.bitacora import BitacoraCreate

async def get_all(db: AsyncSession):
    result = await db.execute(select(Bitacora).order_by(Bitacora.Fecha.desc()))
    return result.scalars().all()

async def get_by_id(db: AsyncSession, bitacora_id: int):
    result = await db.execute(select(Bitacora).where(Bitacora.Id == bitacora_id))
    return result.scalar_one_or_none()

async def create(db: AsyncSession, data: BitacoraCreate):
    nuevo = Bitacora(**data.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo
