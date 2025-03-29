from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.publicacion import Publicacion
from app.schemas.publicacion import PublicacionCreate, PublicacionUpdate

async def get_all(db: AsyncSession):
    result = await db.execute(select(Publicacion))
    return result.scalars().all()

async def get_by_id(db: AsyncSession, pub_id: int):
    result = await db.execute(select(Publicacion).where(Publicacion.Id == pub_id))
    return result.scalar_one_or_none()

async def create(db: AsyncSession, data: PublicacionCreate):
    nueva = Publicacion(**data.dict())
    db.add(nueva)
    await db.commit()
    await db.refresh(nueva)
    return nueva

async def update(db: AsyncSession, pub_id: int, data: PublicacionUpdate):
    pub = await get_by_id(db, pub_id)
    if pub:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(pub, key, value)
        await db.commit()
        await db.refresh(pub)
    return pub

async def delete(db: AsyncSession, pub_id: int):
    pub = await get_by_id(db, pub_id)
    if pub:
        await db.delete(pub)
        await db.commit()
    return pub
