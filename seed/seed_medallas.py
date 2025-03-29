import asyncio
from app.database import engine, SessionLocal
from app.models.medalla import Medalla

medallas_default = [
    {"nombre": "Semilla Verde", "color": "#6DBE45"},
    {"nombre": "Recolector Activo", "color": "#4BAFBD"},
    {"nombre": "EcoHéroe", "color": "#347474"},
    {"nombre": "Guardabosques Urbano", "color": "#1D8348"},
    {"nombre": "Embajador Verde", "color": "#2ECC71"},
    {"nombre": "Zero Waste Warrior", "color": "#5D6D7E"},
    {"nombre": "Leyenda del Reciclaje", "color": "#9B59B6"},
    {"nombre": "EcoInfluencer", "color": "#F4D03F"},
    {"nombre": "EcoAmigo del Mes", "color": "#3498DB"},
]

async def seed_medallas():
    async with SessionLocal() as session:
        for m in medallas_default:
            existe = await session.execute(
                Medalla.__table__.select().where(Medalla.nombre == m["nombre"])
            )
            if not existe.first():
                session.add(Medalla(nombre=m["nombre"], color=m["color"], id_usuario=1))  
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed_medallas())
