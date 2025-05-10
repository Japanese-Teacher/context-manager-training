from typing import Callable

from typing_extensions import ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

def outer_function(func: Callable[P,R]) -> Callable[P,R]:
    def wrapper (*args: P.args, **kwargs: P.kwargs) -> R:
        print(f'Вызываем функцию {func.__name__}')
        print(f'Аргументы: позиционные {args}, именованные {kwargs}')

        result = func(*args, **kwargs)

        print(f'Функция {func.__name__} вернула: {result}')
        return result

    return wrapper

@outer_function
def count(numbers: list[int]) -> int:
    return sum(numbers)

count([1, 2, 3, 4, 5])