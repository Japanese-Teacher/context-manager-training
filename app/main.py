from contextlib import contextmanager

@contextmanager
def simple_context():
    print("Вход в контекст")
    yield
    print("Выход из контекста")


with simple_context():
    print("Внезапный деп")


class MyContextManager:
    def __enter__(self):
        print("Вход в контекст")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выход из контекста")
        return False


with MyContextManager() as cm:
    print("Внезапный деп")