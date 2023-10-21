from fastapi import Request
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from jose import jwt

from src.application.auth.schemas import AuthTokenPayload
from src.application.auth.config import AuthSettings


class JWTBearerManager(HTTPBearer):
    def __init__(
        self,
        config: AuthSettings,
        auto_error: bool,
    ) -> None:
        self._config = config

        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> AuthTokenPayload:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        return self._decode_token(token=credentials.credentials)

    def _decode_token(self, token: str) -> AuthTokenPayload:
        """Расшифровка JWT токена"""

        payload = jwt.decode(
            token, self._config.AUTH_PUBLIC_KEY, algorithms=[jwt.ALGORITHMS.RS256]
        )
        return AuthTokenPayload(**payload)
