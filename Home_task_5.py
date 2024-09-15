# Задание 1. 
# Квадраты чисел
# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение.

from typing import Iterator


def generator_function(n: int) -> Iterator[int]:

    for number in range(1, n + 1):

        yield number ** 2
    
def main() -> None:

    n = int(input('Введите число N: '))

    print('Вывод квадратов. Функция-генератор')

    for square in generator_function(n):
        print(square, end=' ')
    print('\n')

    print('Вывод квадратов. Генераторное выражение')

    generator_expr = (i ** 2 for i in range(1, n + 1))

    for square in generator_expr:
        print(square, end=' ')
    print() 
main()


# Задача 2. 
# Однострочный генератор словаря
# Напишите однострочный генератор словаря, который принимает на вход три
# списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

def calculate_bonus(names, salary, bonus):


    result = {names[i]: round(salary[i] * float(bonus[i].strip('%'))/ 100, 2) for i in range(len(names))}
    return result

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
result = calculate_bonus(names, salary, bonus)
print(result)


# Задача 3. 
# Генератор последовательности чисел Фибоначчи
# Напишите генераторную функцию fibonacci(n), которая принимает на вход
# одно целое число n и возвращает последовательность первых n чисел
# Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
# число является суммой двух предыдущих, начиная с 0 и 1.

def fibonacci(n):

    a, b = 0, 1

    for _ in range(n):
        yield a 
    a, b = b, a + b 
for number in fibonacci(10):
    print(number)



# Задача 4. 
# Генератор подстрок
# Напишите генераторную функцию substrings(s), которая принимает строку
# s и возвращает генератор всех возможных подстрок этой строки.
# На вход подается строка abc

def substrings(s):

    length = len(s)

    for start in range(length):

        for end in range(start + 1, length + 1):
            yield s[start:end]

for substring in substrings('abc'):
    print(substring)