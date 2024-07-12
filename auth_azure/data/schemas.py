from datetime import date, datetime
from typing import Annotated, Any, Dict, Literal, Optional, Union

from pydantic import BaseModel


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
    id: Optional[str] = None
    
    token_type: str
    scope: str
    expires_in: Optional[Union[str, int]]
    ext_expires_in: Optional[Union[str, int]]
    access_token: str
    refresh_token: str
    id_token: str
    client_info: str
    id_token_claims: TokenClaims
    token_source: str
    
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    