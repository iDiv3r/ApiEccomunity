from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate

async def get_all_usuarios(db: AsyncSession):
    result = await db.execute(select(Usuario))
    return result.scalars().all()

async def get_usuario_by_id(db: AsyncSession, usuario_id: int):
    result = await db.execute(select(Usuario).where(Usuario.Id == usuario_id))
    return result.scalar_one_or_none()

async def create_usuario(db: AsyncSession, usuario: UsuarioCreate):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    await db.commit()
    await db.refresh(nuevo_usuario)
    return nuevo_usuario

async def update_usuario(db: AsyncSession, usuario_id: int, usuario_data: UsuarioUpdate):
    usuario = await get_usuario_by_id(db, usuario_id)
    if usuario:
        for key, value in usuario_data.dict(exclude_unset=True).items():
            setattr(usuario, key, value)
        await db.commit()
        await db.refresh(usuario)
    return usuario

async def delete_usuario(db: AsyncSession, usuario_id: int):
    usuario = await get_usuario_by_id(db, usuario_id)
    if usuario:
        await db.delete(usuario)
        await db.commit()
    return usuario
