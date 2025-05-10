from typing import Any


class MyContextManager:
    def __enter__(self) -> Any:
        print('Вход в контекст')
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        print('Выход из контекста')
        return False


with MyContextManager() as cm:
    print('Внезапный деп')