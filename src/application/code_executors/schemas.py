from pydantic import BaseModel


class ResultSchema(BaseModel):
    output: str | None = None
    errors: str | None = None
