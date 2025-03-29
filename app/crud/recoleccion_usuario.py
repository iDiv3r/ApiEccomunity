from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.recoleccion_usuario import RecoleccionUsuario
from app.schemas.recoleccion_usuario import RecoleccionCreate, RecoleccionUpdate

async def get_all_recolecciones(db: AsyncSession):
    result = await db.execute(select(RecoleccionUsuario))
    return result.scalars().all()

async def get_recoleccion_by_id(db: AsyncSession, reco_id: int):
    result = await db.execute(select(RecoleccionUsuario).where(RecoleccionUsuario.Id == reco_id))
    return result.scalar_one_or_none()

async def create_recoleccion(db: AsyncSession, reco: RecoleccionCreate):
    nueva = RecoleccionUsuario(**reco.dict())
    db.add(nueva)
    await db.commit()
    await db.refresh(nueva)
    return nueva

async def update_recoleccion(db: AsyncSession, reco_id: int, data: RecoleccionUpdate):
    reco = await get_recoleccion_by_id(db, reco_id)
    if reco:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(reco, key, value)
        await db.commit()
        await db.refresh(reco)
    return reco

async def delete_recoleccion(db: AsyncSession, reco_id: int):
    reco = await get_recoleccion_by_id(db, reco_id)
    if reco:
        await db.delete(reco)
        await db.commit()
    return reco
