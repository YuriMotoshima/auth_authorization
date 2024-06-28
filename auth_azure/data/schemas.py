from pydantic import BaseModel
from typing import Annotated, Any, Literal, Optional, Union
from datetime import date, datetime


class TokenClaims(BaseModel):
    aud: str
    iss: str
    iat: int
    nbf: int
    exp: int
    idp: str
    name: str
    oid: str
    preferred_username: str
    rh: str
    sub: str
    tid: str
    uti: str
    ver: str


class TokenInfo(BaseModel):
    id: str
    created_by: str
    token_type: str
    scope: str
    expires_in: str
    ext_expires_in: str
    access_token: str
    refresh_token: str
    id_token: str
    client_info: str
    id_token_claims: dict[TokenClaims]
    token_source: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None