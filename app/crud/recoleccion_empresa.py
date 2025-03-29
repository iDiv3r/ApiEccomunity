from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.recoleccion_empresa import RecoleccionEmpresa
from app.schemas.recoleccion_empresa import RecoleccionEmpresaCreate, RecoleccionEmpresaUpdate

async def get_all(db: AsyncSession):
    result = await db.execute(select(RecoleccionEmpresa))
    return result.scalars().all()

async def get_by_id(db: AsyncSession, reco_id: int):
    result = await db.execute(select(RecoleccionEmpresa).where(RecoleccionEmpresa.Id == reco_id))
    return result.scalar_one_or_none()

async def create(db: AsyncSession, data: RecoleccionEmpresaCreate):
    nueva = RecoleccionEmpresa(**data.dict())
    db.add(nueva)
    await db.commit()
    await db.refresh(nueva)
    return nueva

async def update(db: AsyncSession, reco_id: int, data: RecoleccionEmpresaUpdate):
    registro = await get_by_id(db, reco_id)
    if registro:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(registro, key, value)
        await db.commit()
        await db.refresh(registro)
    return registro

async def delete(db: AsyncSession, reco_id: int):
    registro = await get_by_id(db, reco_id)
    if registro:
        await db.delete(registro)
        await db.commit()
    return registro
