from fastapi import FastAPI

from src.api.routers.code_executors import code_executor_routers
from src.api.routers.exception_handlers import setup_exception_handlers
from src.api.routers.healthcheck import health_check_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(health_check_router)
    app.include_router(code_executor_routers)
    setup_exception_handlers(app=app)
    return app
