from datetime import date, datetime, UTC
from sqlalchemy import Column, String, Integer, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy import MetaData

from auth_azure.config.settings import SETTINGS as Settings
from auth_azure.data.database import engine

metadata = MetaData()
table_registry = registry(metadata=metadata)

@table_registry.mapped_as_dataclass
class AuthStorage:
    __tablename__ = f'{Settings.GCP_DATABASE}.{Settings.GCP_TABLE_AUTH_STORAGE}'
    
    id: Mapped[str] = mapped_column(unique=True, primary_key=True)
    token_type: Mapped[str]
    scope: Mapped[str]
    expires_in: Mapped[str]
    ext_expires_in: Mapped[str]
    access_token: Mapped[str]
    refresh_token: Mapped[str]
    access_to_user: Mapped[str]
    user_email: Mapped[str]
    id_token: Mapped[str]
    client_info: Mapped[str]
    id_token_claims: Mapped[JSON]
    token_source: Mapped[str]
    created_by: Mapped[str]
    created_at: Mapped[datetime]
    updated_by: Mapped[str]
    updated_at: Mapped[datetime]


# table_registry.metadata.create_all(engine)
# table_registry.metadata.drop_all(engine)


# Execute apenas uma vez para criar as tabelas:
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)