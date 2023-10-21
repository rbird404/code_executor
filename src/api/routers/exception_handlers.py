from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from src.common.exceptions import UnsupportedLanguage


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, unsupported_handler)
    app.add_exception_handler(UnsupportedLanguage, unsupported_language)


async def unsupported_language(request: Request, err: UnsupportedLanguage) -> ORJSONResponse:
    return ORJSONResponse(
        "Unsupported language!",
        status_code=status.HTTP_404_NOT_FOUND
    )


async def unsupported_handler(request: Request, err: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        '\n'.join(err.args),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
