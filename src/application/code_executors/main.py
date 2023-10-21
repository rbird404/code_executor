import time

from src.application.code_executors.executor_chosen import chose_executor
from src.application.code_executors.schemas import ResultSchema


class ExecutorService:
    def __init__(self, language: str, code: str, input_data: str) -> None:
        self._language = language
        self._code = code
        self._input_data = input_data

    def start_test(self) -> ResultSchema:
        """Выбор компилятора кода и исполнение кода"""

        executor = chose_executor(language=self._language)
        start_time = time.time()
        result = executor(code=self._code).execute(input_data=self._input_data)
        time_result = time.time() - start_time
        result.time = time_result

        return result
