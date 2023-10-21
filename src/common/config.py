from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="SERVER_"
    )

    host: str = Field(validation_alias="SERVER_HOST", default="localhost")
    port: int = Field(validation_alias="SERVER_PORT", default=9000)
    reload: bool = Field(validation_alias="SERVER_RELOAD", default=False)
    proxy_headers: bool = Field(validation_alias="SERVER_PROXY_HEADERS", default=False)


server_settings = ServerSettings()
