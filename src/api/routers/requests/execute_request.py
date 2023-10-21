from typing import Any

from pydantic import BaseModel


class ExecuteCodeRequest(BaseModel):
    language: str
    code: str
    input: str
