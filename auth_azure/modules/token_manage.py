from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from auth_azure.data.database import get_session
from auth_azure.data.models import AuthStorage
from auth_azure.data.schemas import TokenInfo

session_dependency = Annotated[Session, Depends(get_session)]

class TokenStorage:
    
    def __init__(self, token_info: dict):
        self.token_info = TokenInfo(**token_info)

    async def save_token(self, session: session_dependency):
        data = AuthStorage(
            id=self.token_info.id_token_claims.oid,
            token_type=self.token_info.token_type,
            scope=self.token_info.scope,
            expires_in=self.token_info.expires_in,
            ext_expires_in=self.token_info.ext_expires_in,
            access_token=self.token_info.access_token,
            refresh_token=self.token_info.refresh_token,
            id_token=self.token_info.id_token,
            client_info=self.token_info.client_info,
            id_token_claims=self.token_info.id_token_claims.model_dump(),
            token_source=self.token_info.token_source
        )
        session.add(data)
        await session.commit()

    def get_token(self, user_id: str):
        return self.token_store.get(user_id)

    def delete_token(self, user_id: str):
        if user_id in self.token_store:
            del self.token_store[user_id]

    def get_user_id_by_token(self, token: str):
        for user_id, stored_token in self.token_store.items():
            if stored_token == token:
                return user_id
        return None
