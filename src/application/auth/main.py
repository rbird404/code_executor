from src.application.auth.config import AuthSettings
from src.application.auth.jwt_manager import JWTBearerManager


def jwt_manager(config: AuthSettings, auto_error: bool) -> JWTBearerManager:
    """Создание инстанса jwt менеджера"""

    return JWTBearerManager(config=config, auto_error=auto_error)
