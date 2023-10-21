import os
import subprocess

from src.application.code_executors.executors.base import CodeCompileExecutor
from src.application.code_executors.exceptions.cpp import CppCompileError
from src.application.code_executors.schemas import ResultSchema


class CppExecutor(CodeCompileExecutor):
    def execute(self, input_data: str | None = None) -> ResultSchema:
        try:
            self._compile()
        except CppCompileError as error:
            return ResultSchema(errors=str(error))

        process = subprocess.run(
            [self.path],
            input=input_data,
            capture_output=True,
            text=True,
        )
        self.remove_static_files()

        return self.get_result(process.stdout, process.stderr)

    def _compile(self) -> None:
        with open(os.getcwd()[:-3] + str(self.path) + ".cc", "w") as file:
            file.write(self.code)

        process = subprocess.run(
            ["g++", "-o", self.path, str(self.path) + ".cc"],
            capture_output=True,
            text=True
        )

        if error := process.stderr:
            self.remove_static_files()
            raise CppCompileError(error)
