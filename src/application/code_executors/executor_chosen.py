from src.application.code_executors.executors import *
from src.common.exceptions import UnsupportedLanguage

executor_mapping = {
    "cpp": CppExecutor,
    "golang": GoExecutor,
    "java": JavaExecutor,
    "python": PythonExecutor
}


def chose_executor(language: str) -> type[CodeExecutor]:
    """Выдает нужный нам исполнитель кода"""

    executor = executor_mapping.get(language)
    if executor:
        return executor
    raise UnsupportedLanguage()
