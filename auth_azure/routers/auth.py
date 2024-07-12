import logging
from typing import Annotated


from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session

from auth_azure import msal_app
from auth_azure.config.settings import SETTINGS as Settings
from auth_azure.data.database import get_session
from auth_azure.modules.token_manage import TokenStorage

router = APIRouter(prefix='/auth', tags=['auth'])

@router.get("/")
async def index(request: Request):
    return JSONResponse(content={"message": "Olá, esta é a página inicial. Vá para /login para iniciar o fluxo de autenticação."})


@router.get("/login")
async def login():
    auth_url = msal_app.get_authorization_request_url(Settings.SCOPE, redirect_uri=Settings.REDIRECT_URI)
    return RedirectResponse(url=auth_url)


@router.get("/redirect")
async def authorized(request: Request, session: Annotated[Session, Depends(get_session)]):
    code = request.query_params.get('code')
    if not code:
        logging.error("Código de autorização ausente")
        raise HTTPException(status_code=400, detail="Código de autorização ausente")

    result = msal_app.acquire_token_by_authorization_code(code, scopes=Settings.SCOPE, redirect_uri=Settings.REDIRECT_URI)

    if 'access_token' in result:
        storage_data = TokenStorage(token_info=result)
        await storage_data.save_token(session)
                
        token = result['access_token']
        redirect_url = f'{Settings.OUTSYSTEMS_REDIRECT_URI}?token={token}'
        return RedirectResponse(url=redirect_url)
    logging.error("Falha na autenticação")
    return JSONResponse(content={"error": "Autenticação falhou"}, status_code=400)


@router.get("/AuthCallback")
async def test_callback(request: Request):
    token = request.query_params.get('token')
    if not token:
        raise HTTPException(status_code=400, detail="Token ausente")
    return JSONResponse(content={"message": "Autenticação bem-sucedida", "token": token})


@router.get("/logout")
async def logout(request: Request):
    token = request.query_params.get('token')
    if not token:
        raise HTTPException(status_code=400, detail="Token ausente")
    
    user_id = token_storage.get_user_id_by_token(token)
    if not user_id:
        raise HTTPException(status_code=400, detail="Usuário não encontrado para o token fornecido")

    token_storage.delete_token(user_id)  # Remove o token específico do usuário
    logout_url = f"https://login.microsoftonline.com/{Settings.AZURE_SA['TENANT_ID']}/oauth2/v2.0/logout?post_logout_redirect_uri={Settings.POST_LOGOUT_REDIRECT_URI}"
    return RedirectResponse(url=logout_url)

@router.get("/logged_out")
async def logged_out(request: Request):
    return JSONResponse(content={"message": "Você saiu com sucesso."})
