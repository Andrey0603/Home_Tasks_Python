# Задача 1. 
# Нахождение наибольшего общего делителя (НОД) двух
# чисел.
# Программа принимает два целых числа и находит их наибольший общий
# делитель (НОД).



a = int(input("Введите первое число: "))

b = int(input("Введите второе число: "))

while b:
    a, b = b, a % b 
print("НОД:", a)


# Задание 2. 
# Преобразование числа в шестнадцатеричное
# представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

numbers = [255, 16, 0, -42]

hex_digits = '0123456789ABCDEF'
for number in numbers:

    if number == 0:
        hex_string = '0'
    else:

        is_negative = number < 0
        if is_negative:
            number = -number

        hex_string = ''
        while number > 0:
            remainder = number % 16
            hex_string = hex_digits[remainder] + hex_string
            number //= 16

            if is_negative:
                hex_string = '-' + hex_string
    print(hex_string)



# Задача 3. 
# Перевод целого числа в римское число
# Программа принимает целое число и возвращает его римское представление в
# виде строки.


num = int(input("Введите целое число: "))

val = [
1000, 900, 500, 400,
100, 90, 50, 40,
10, 9, 5, 4,
1
]

syb = [
"M", "CM", "D", "CD",
"C", "XC", "L", "XL",
"X", "IX", "V", "IV",
"I"
]

roman_num = ''

i = 0

while num > 0:

    for _ in range(num // val[i]): 

        roman_num += syb[i] 
    
        num -= val[i] 
    i += 1 

print("Результат:", roman_num)


# Задача 4. 
# Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fractions.


from fractions import Fraction

frac1 = input("Введите первую дробь (a/b): ")

frac2 = input("Введите вторую дробь (a/b): ")


numerator1, denominator1 = map(int, frac1.split('/'))

numerator2, denominator2 = map(int, frac2.split('/'))

f1 = Fraction(numerator1, denominator1)
f2 = Fraction(numerator2, denominator2)

sum_frac = f1 + f2

product_frac = f1 * f2

print("Сумма:", sum_frac)

print("Произведение:", product_frac)