from fastapi import APIRouter

health_check_router = APIRouter(prefix="/healthcheck", tags=["Healthcheck"])


@health_check_router.get('', response_model=str)
async def health_check():
    return "OK"
