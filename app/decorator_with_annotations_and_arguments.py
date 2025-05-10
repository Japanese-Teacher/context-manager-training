from typing_extensions import ParamSpec, TypeVar, Callable

P = ParamSpec('P')
R = TypeVar('R')

def make_calls (max_calls: int = 1) -> Callable[[Callable[P, R]], Callable[P,R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        calls = 0

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
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
def say_hello(name: str) -> None:
    print(f'Привет {name}!')
say_hello("Жора")
say_hello("Петя")