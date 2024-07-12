from datetime import UTC, datetime

from sqlalchemy import JSON, MetaData
from sqlalchemy.orm import Mapped, mapped_column, registry

from auth_azure.config.settings import SETTINGS as Settings
from auth_azure.data.database import engine

metadata = MetaData()
table_registry = registry(metadata=metadata)

@table_registry.mapped_as_dataclass
class AuthStorage:
    __tablename__ = f'{Settings.GCP_DATABASE}.{Settings.GCP_TABLE_AUTH_STORAGE}'
    
    id: Mapped[str] = mapped_column(primary_key=True)
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
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC), nullable=False)
    updated_by: Mapped[str]
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC), onupdate=datetime.now(UTC), nullable=False)


# table_registry.metadata.create_all(engine)
# table_registry.metadata.drop_all(engine)
