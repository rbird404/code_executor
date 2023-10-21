from enum import Enum

from pydantic import BaseModel


class TokenPurpose(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


class AuthTokenPayload(BaseModel):
    account_id: int
    role: str
    purpose: TokenPurpose


class AuthTokenData(BaseModel):
    account_id: int
    account_role: str
