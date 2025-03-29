from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.medalla import Medalla

router = APIRouter(prefix="/medallas", tags=["Medallas"])

@router.get("/")
async def listar_medallas(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Medalla.__table__.select())
    return result.fetchall()
