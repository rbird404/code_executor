from fastapi import APIRouter

from src.api.routers.requests.execute_request import ExecuteCodeRequest
from src.api.routers.responses.execute_result import ExecuteResultResponse
from src.application.code_executors.main import ExecutorService

code_executor_routers = APIRouter(prefix="/code_executor", tags=["Code Executors"])


@code_executor_routers.post(
    "/execute",
    response_model=ExecuteResultResponse
)
async def execute_code(
        execute_data: ExecuteCodeRequest,
):
    run_code_result = ExecutorService(
        code=execute_data.code, language=execute_data.language
    ).start_test()

    return run_code_result
