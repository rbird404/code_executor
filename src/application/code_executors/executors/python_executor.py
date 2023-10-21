import subprocess

from src.application.code_executors.executors.base import CodeExecutor
from src.application.code_executors.schemas import ResultSchema


class PythonExecutor(CodeExecutor):
    def execute(self, input_data: str | None = None) -> ResultSchema:
        process = subprocess.run(
            ["python3", "-c", self.code],
            input=input_data,
            capture_output=True,
            text=True,
        )

        return self.get_result(process.stdout, process.stderr)