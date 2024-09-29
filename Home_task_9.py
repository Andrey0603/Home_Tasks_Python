# Задание 1. Как дела?
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# написал надоедливый декоратор, который при вызове декорируемой функции
# спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то
# вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после
# такой выходки Васю чуть не уволили с работы.
# Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.
# Пример кода:
# @how_are_you
# def test():
# print('<Тут что-то происходит...>')
# test()
# Результат:
# Как дела? Хорошо.
# А у меня не очень! Ладно, держи свою функцию.
# <Тут что-то происходит...>

from functools import wraps
from typing import Callable, Any
def how_are_you(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        input('Как дела? ') 
        print('А у меня не очень! Ладно, держи свою функцию.') 

        result = func(*args, **kwargs) 
        return result
    return wrapper
@how_are_you
def test() -> None:

    print('<Тут что-то происходит...>')
@how_are_you
def another_function() -> None:

    print('Еще один тестовый вывод.')
if __name__ == "__main__":
    test() 
    another_function()


# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно
# замедлить. Типичный пример — функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции
# ждёт несколько секунд.

from functools import wraps
from time import sleep
from typing import Callable, Any
def slowdown_2s(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        sleep(2) 
        result = func(*args, **kwargs) 
        return result
    return wrapper
@slowdown_2s
def test() -> None:

    print('<Тут что-то происходит...>')
@slowdown_2s
def another_function() -> None:

    print('Еще один тестовый вывод.')
if __name__ == "__main__":
    test() 


# Задача 3. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.
# Пример: Из файла products.json нужно создать products.csv.

from functools import wraps
from typing import Callable, Any, Optional
def counter(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        wrapper.count += 1 
        result = func(*args, **kwargs) 
        print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")

        return result 

    wrapper.count = 0 
    return wrapper 
@counter
def greeting(name: str, age: Optional[int] = None) -> str:

    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)
@counter
def greeting2(name: str) -> None:

    print(f'Привет, {name}!')
def main() -> None:

    greeting("Том") 
    greeting("Миша", age=100) 
    greeting2("Маша") 
    greeting(name="Катя", age=16) 

main() 


# Задача 4. Кэширование для ускорения вычислений
# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
# результаты вызова функции и, при повторном вызове с теми же аргументами,
# возвращает сохранённый результат.
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
# если такие аргументы уже использовались, должен вернуть сохранённый результат
# вместо запуска расчёта.

def cache_decorator(func):

    cache = {} 
    def wrapper(number):

        if number in cache:
            return cache[number] 
        result = func(number)
        cache[number] = result 
        return result
    return wrapper

@cache_decorator
def fibonacci(number):

    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(10)) 
print(fibonacci(10)) 
print(fibonacci(5)) 

