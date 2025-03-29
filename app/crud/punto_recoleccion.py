from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.punto_recoleccion import PuntoRecoleccion
from app.schemas.punto_recoleccion import PuntoCreate, PuntoUpdate

async def get_all_puntos(db: AsyncSession):
    result = await db.execute(select(PuntoRecoleccion))
    return result.scalars().all()

async def get_punto_by_id(db: AsyncSession, punto_id: int):
    result = await db.execute(select(PuntoRecoleccion).where(PuntoRecoleccion.Id == punto_id))
    return result.scalar_one_or_none()

async def create_punto(db: AsyncSession, punto: PuntoCreate):
    nuevo_punto = PuntoRecoleccion(**punto.dict())
    db.add(nuevo_punto)
    await db.commit()
    await db.refresh(nuevo_punto)
    return nuevo_punto

async def update_punto(db: AsyncSession, punto_id: int, data: PuntoUpdate):
    punto = await get_punto_by_id(db, punto_id)
    if punto:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(punto, key, value)
        await db.commit()
        await db.refresh(punto)
    return punto

async def delete_punto(db: AsyncSession, punto_id: int):
    punto = await get_punto_by_id(db, punto_id)
    if punto:
        await db.delete(punto)
        await db.commit()
    return punto
