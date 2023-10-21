from pydantic import BaseModel


class ExecuteCodeRequest(BaseModel):
    language: str
    code: str
