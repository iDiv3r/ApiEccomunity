from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.horario_recoleccion import HorarioRecoleccion
from app.schemas.horario_recoleccion import HorarioCreate, HorarioUpdate

async def get_all_horarios(db: AsyncSession):
    result = await db.execute(select(HorarioRecoleccion))
    return result.scalars().all()

async def get_horario_by_id(db: AsyncSession, horario_id: int):
    result = await db.execute(select(HorarioRecoleccion).where(HorarioRecoleccion.Id == horario_id))
    return result.scalar_one_or_none()

async def create_horario(db: AsyncSession, horario: HorarioCreate):
    nuevo = HorarioRecoleccion(**horario.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

async def update_horario(db: AsyncSession, horario_id: int, data: HorarioUpdate):
    horario = await get_horario_by_id(db, horario_id)
    if horario:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(horario, key, value)
        await db.commit()
        await db.refresh(horario)
    return horario

async def delete_horario(db: AsyncSession, horario_id: int):
    horario = await get_horario_by_id(db, horario_id)
    if horario:
        await db.delete(horario)
        await db.commit()
    return horario
