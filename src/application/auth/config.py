from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="JWT_"
    )

    public_key: str = Field(validation_alias="JWT_PUBLIC_KEY", default="rsa_public_key")


auth_settings = AuthSettings()
