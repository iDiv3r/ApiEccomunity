from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.empresa import Empresa
from app.schemas.empresa import EmpresaCreate, EmpresaUpdate

async def get_all_empresas(db: AsyncSession):
    result = await db.execute(select(Empresa))
    return result.scalars().all()

async def get_empresa_by_id(db: AsyncSession, empresa_id: int):
    result = await db.execute(select(Empresa).where(Empresa.Id == empresa_id))
    return result.scalar_one_or_none()

async def create_empresa(db: AsyncSession, empresa: EmpresaCreate):
    nueva_empresa = Empresa(**empresa.dict())
    db.add(nueva_empresa)
    await db.commit()
    await db.refresh(nueva_empresa)
    return nueva_empresa

async def update_empresa(db: AsyncSession, empresa_id: int, empresa_data: EmpresaUpdate):
    empresa = await get_empresa_by_id(db, empresa_id)
    if empresa:
        for key, value in empresa_data.dict(exclude_unset=True).items():
            setattr(empresa, key, value)
        await db.commit()
        await db.refresh(empresa)
    return empresa

async def delete_empresa(db: AsyncSession, empresa_id: int):
    empresa = await get_empresa_by_id(db, empresa_id)
    if empresa:
        await db.delete(empresa)
        await db.commit()
    return empresa
