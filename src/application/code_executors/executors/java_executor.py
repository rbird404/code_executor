import os
import subprocess

from src.application.code_executors.executors.base import CodeCompileExecutor
from src.common.constants import STATIC
from src.application.code_executors.schemas import ResultSchema


class JavaExecutor(CodeCompileExecutor):
    _java_main_class_name = "TestMain"

    def __init__(self, code: str, version: str | None = None):
        super().__init__(code, version)
        self._code_id = self._java_main_class_name
        self._path = STATIC / self._code_id

    def _write_code_to_file(self):
        with open(os.getcwd()[:-3] + str(self.path) + ".java", 'w') as file:
            file.write(self.code)

    def execute(self, input_data: str | None = None) -> ResultSchema:
        self._write_code_to_file()
        subprocess.check_call(['javac', os.getcwd()[:-3] + str(self.path) + ".java"])
        process = subprocess.run(
            ['java', os.getcwd()[:-3] + str(self.path) + ".java"],
            input=input_data,
            capture_output=True,
            text=True,
        )
        self.remove_static_files()
        return self.get_result(process.stdout, process.stderr)
