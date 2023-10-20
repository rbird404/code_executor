import os
import glob
import uuid
import subprocess

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

from config import STATIC
from exceptions import CppCompileError


@dataclass
class Result:
    output: str | None = None
    errors: str | None = None

    def to_dict(self) -> dict:
        return {"output": self.output, "errors": self.errors}


class CodeExecutor(ABC):
    allowed_version = []

    def __init__(self, code: str, version: str | None = None):
        self.code = code
        self.version = version

    @abstractmethod
    def execute(self, input: str | None = None) -> Result:
        pass

    def get_result(self, output=None, errors=None) -> Result:
        data = {}
        if output:
            data["output"] = output
        if errors:
            data['errors'] = errors
        return Result(**data)


class PythonExecutor(CodeExecutor):
    def execute(self, input: str | None = None) -> Result:
        process = subprocess.run(
            ["python3", "-c", self.code],
            input=input,
            capture_output=True,
            text=True,
        )

        return self.get_result(process.stdout, process.stderr)


class CodeCompileExecutor(CodeExecutor, ABC):
    def __init__(self, code: str, version: str | None = None):
        super().__init__(code, version)
        self._code_id = uuid.uuid4().hex
        self._path = STATIC / self._code_id

    @property
    def path(self) -> Path:
        return self._path

    @property
    def code_id(self) -> str:
        return self._code_id

    def remove_static_files(self) -> None:
        files = glob.glob(str(self.path) + "*")
        for file in files:
            os.remove(file)


class CppExecutor(CodeCompileExecutor):
    def execute(self, input: str | None = None) -> Result:
        try:
            self._compile()
        except CppCompileError as error:
            return Result(errors=str(error))

        process = subprocess.run(
            [self.path],
            input=input,
            capture_output=True,
            text=True,
        )
        self.remove_static_files()

        return self.get_result(process.stdout, process.stderr)

    def _compile(self) -> None:
        with open(str(self.path) + ".cc", "w") as file:
            file.write(self.code)

        process = subprocess.run(
            ["g++", "-o", self.path, str(self.path) + ".cc"],
            capture_output=True,
            text=True
        )

        if error := process.stderr:
            self.remove_static_files()
            raise CppCompileError(error)


class GoExecutor(CodeCompileExecutor):
    def _write_code_to_file(self):
        with open(str(self.path) + ".go", 'w') as file:
            file.write(self.code)

    def execute(self, input: str | None = None) -> Result:
        self._write_code_to_file()

        process = subprocess.run(
            ['go', 'run', str(self.path) + ".go"],
            input=input,
            capture_output=True,
            text=True,
        )
        self.remove_static_files()
        return self.get_result(process.stdout, process.stderr)


class JavaExecutor(CodeCompileExecutor):
    _java_main_class_name = "TestMain"

    def __init__(self, code: str, version: str | None = None):
        super().__init__(code, version)
        self._code_id = self._java_main_class_name
        self._path = STATIC / self._code_id

    def _write_code_to_file(self):
        with open(str(self.path) + ".java", 'w') as file:
            file.write(self.code)

    def execute(self, input: str | None = None) -> Result:
        self._write_code_to_file()
        subprocess.check_call(['javac', str(self.path) + ".java"])
        process = subprocess.run(
            ['java', str(self.path) + ".java"],
            input=input,
            capture_output=True,
            text=True,
        )
        self.remove_static_files()
        return self.get_result(process.stdout, process.stderr)
