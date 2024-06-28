
from fastapi import FastAPI

from auth_azure.routers import auth

app = FastAPI()

app.include_router(auth.router)