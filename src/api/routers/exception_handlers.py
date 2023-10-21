from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from src.common.exceptions import UnsupportedLanguage
from src.common.schemas.errors import ErrorMessage


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, unsupported_handler)
    app.add_exception_handler(UnsupportedLanguage, unsupported_language)


async def unsupported_language(request: Request, err: UnsupportedLanguage) -> ORJSONResponse:
    return await handle_app_error(
        status_code=status.HTTP_404_NOT_FOUND,
        message="Unsupported language!",
        err=err,
        request=request
    )


async def unsupported_handler(request: Request, err: Exception) -> ORJSONResponse:
    return await handle_app_error(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        err_args=err.args,
        err=err,
        request=request
    )


async def handle_app_error(
    *,
    request: Request,
    status_code: int,
    err: Exception,
    message: str | None = None,
    err_args: tuple | None = None
) -> ORJSONResponse:
    if message:
        message = message
    else:
        message = "\n".join(err_args)
    return ORJSONResponse(
        ErrorMessage(message=message), status_code=status_code
    )
