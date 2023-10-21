import glob
import os
import uuid
from abc import ABC, abstractmethod
from pathlib import Path

from src.common.constants import STATIC
from src.application.code_executors.schemas import ResultSchema


class CodeExecutor(ABC):
    allowed_version: list = list()

    def __init__(self, code: str, version: str | None = None):
        self.code = code
        self.version = version

    @abstractmethod
    def execute(self, input_data: str | None = None) -> ResultSchema:
        pass

    @staticmethod
    def get_result(output=None, errors=None) -> ResultSchema:
        data = {}
        if output:
            data["output"] = output
        if errors:
            data['errors'] = errors
        return ResultSchema(**data)


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
