from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PGStorageSettings(BaseSettings):
    host: str = Field(validation_alias="PG_STORAGE_HOST", default="localhost")
    port: int = Field(validation_alias="PG_STORAGE_PORT", default=5432)
    username: str = Field(validation_alias="PG_STORAGE_USERNAME", default="postgres")
    password: str = Field(validation_alias="PG_STORAGE_PASSWORD", default="postgres")
    database: str = Field(validation_alias="PG_STORAGE_DATABASE", default="postgres")

    def get_url(self, *, async_: bool = False) -> str:
        if async_:
            return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        return (
            f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="PG_STORAGE_"
    )
