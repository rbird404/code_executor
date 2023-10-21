import uvicorn

from src.common.config import server_settings

if __name__ == "__main__":
    uvicorn.run("src.api:app", **server_settings.model_dump())
