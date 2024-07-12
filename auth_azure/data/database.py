from google.cloud import bigquery
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from auth_azure.config.settings import SETTINGS as Settings

if Settings.TESTS:
    engine = create_async_engine(Settings.DATABASE_URL, echo=True)
    AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
else:
    AsyncSessionLocal = bigquery.Client().from_service_account_info(Settings.GCP_SA)

async def get_session():
    async with AsyncSessionLocal() as session:
      yield session
