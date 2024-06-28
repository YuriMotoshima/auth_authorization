from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from auth_azure.config.settings import SETTINGS

settings = SETTINGS

if settings.TESTS:
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
else:
    engine = create_async_engine(f"bigquery+asyncio://{settings.GCP_PROJECT}", echo=True, credentials_info=settings.GCP_SA)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session