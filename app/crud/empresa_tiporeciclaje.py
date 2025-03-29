from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.empresa_tiporeciclaje import EmpresaTipoReciclaje
from app.schemas.empresa_tiporeciclaje import AsignacionTipo

async def asignar_tipo(db: AsyncSession, asignacion: AsignacionTipo):
    nueva = EmpresaTipoReciclaje(**asignacion.dict())
    db.add(nueva)
    await db.commit()
    await db.refresh(nueva)
    return nueva

async def desasignar_tipo(db: AsyncSession, empresa_id: int, tipo_id: int):
    result = await db.execute(
        select(EmpresaTipoReciclaje).where(
            EmpresaTipoReciclaje.id_Empresa == empresa_id,
            EmpresaTipoReciclaje.id_TipoReciclaje == tipo_id
        )
    )
    registro = result.scalar_one_or_none()
    if registro:
        await db.delete(registro)
        await db.commit()
    return registro

async def obtener_asignaciones_por_empresa(db: AsyncSession, empresa_id: int):
    result = await db.execute(
        select(EmpresaTipoReciclaje).where(EmpresaTipoReciclaje.id_Empresa == empresa_id)
    )
    return result.scalars().all()
