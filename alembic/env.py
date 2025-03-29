import asyncio
import os
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool
from alembic import context

from dotenv import load_dotenv
load_dotenv()

from app.database import Base
from app import models  # asegúrate de que __init__.py importe todos los modelos

# Configuración de Alembic
config = context.config

# Cargar configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Usar la metadata de tus modelos
target_metadata = Base.metadata

# Obtener la URL de la base de datos desde el .env
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no definida en el archivo .env")

# Agregar la URL al config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# FUNCIONES PARA MIGRACIONES

def run_migrations_offline():
    """Usar contexto 'offline' (sin conexión directa)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Conectar y correr migraciones en línea."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
