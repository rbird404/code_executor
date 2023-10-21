from src.application.auth.config import auth_settings
from src.application.auth.main import jwt_manager

token_decode = jwt_manager(config=auth_settings, auto_error=True)
