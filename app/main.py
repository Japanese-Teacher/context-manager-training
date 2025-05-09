from contextlib import contextmanager

@contextmanager
def simple_context():
    print("Вход в контекст")
    yield
    print("Выход из контекста")


with simple_context():
    print("Внезапный деп")