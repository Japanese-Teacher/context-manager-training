from typing_extensions import ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

def make_calls (max_calls=1):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                print('Вы достигли максимум')
                return None
            calls += 1
            print(f'Вызов {calls}/{max_calls}')
            return func(*args, **kwargs)
        return wrapper
    return decorator
@make_calls(max_calls=5)
def say_hello(name):
    print(f'Привет {name}!')
say_hello("Жора")
say_hello("Петя")