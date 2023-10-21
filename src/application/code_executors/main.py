from src.application.code_executors.executor_chosen import chose_executor
from src.application.code_executors.schemas import ResultSchema


class ExecutorService:
    def __init__(self, language: str, code: str) -> None:
        self._language = language
        self._code = code

    def start_test(self) -> ResultSchema:
        """Выбор компилятора кода и исполнение кода"""

        executor = chose_executor(language=self._language)

        result = executor(code=self._code).execute()

        return result
