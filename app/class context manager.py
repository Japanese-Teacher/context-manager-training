class MyContextManager:
    def __enter__(self):
        print("Вход в контекст")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выход из контекста")
        return False


with MyContextManager() as cm:
    print("Внезапный деп")