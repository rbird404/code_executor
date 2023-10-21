import os
import subprocess

from src.application.code_executors.executors.base import CodeCompileExecutor
from src.application.code_executors.schemas import ResultSchema


class GoExecutor(CodeCompileExecutor):
    def _write_code_to_file(self):
        with open(os.getcwd()[:-3] + str(self.path) + ".go", 'w') as file:
            file.write(self.code)

    def execute(self, input_data: str | None = None) -> ResultSchema:
        self._write_code_to_file()

        process = subprocess.run(
            ['go', 'run', os.getcwd()[:-3] + str(self.path) + ".go"],
            input=input_data,
            capture_output=True,
            text=True,
        )
        self.remove_static_files()
        return self.get_result(process.stdout, process.stderr)