# Задание 1. Матрицы
# Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам
# поручили разработать класс Matrix для обработки и анализа данных. Ваш класс
# должен предоставлять функциональность для выполнения основных операций
# с матрицами, таких как сложение, вычитание, умножение и транспонирование.
# Это будет полезно для обработки и структурирования больших объёмов
# данных, которые используются в обучении нейронных сетей.
# Задача
# 1. Создайте класс Matrix для работы с матрицами.
# Реализуйте методы:
# ○ сложения,
# ○ вычитания,
# ○ умножения,
# ○ транспонирования матрицы.
# 2. Создайте несколько экземпляров класса Matrix и протестируйте
# реализованные операции.
# Советы
# ● Методы сложения/вычитания/умножения должны получать параметром
# другую матрицу (объект класса Matrix) и выполнять указанное действие
# над своей и этой другой матрицей. Например, метод сложения должен
# получить параметром новую матрицу и сложить её со своей текущей.
# ● Метод транспонирования не должен ничего получать, он должен
# работать исключительно со своей матрицей.
# ● Транспонирование — это алгоритм, при котором строки матрицы
# меняются местами с её столбцами:



class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

def add(self, other):
    if self.rows != other.rows or self.cols != other.cols:
        raise ValueError("Размеры матриц не совпадают сложения")
    result = Matrix(self.rows, self.cols)
    for i in range(self.rows):
        for j in range(self.cols):
            result.data[i][j] = self.data[i][j] + other.data[i][j]
    return result

def subtract(self, other):
    if self.rows != other.rows or self.cols != other.cols:
        raise ValueError("Размеры матриц не совпадают вычитания")
    result = Matrix(self.rows, self.cols)
    for i in range(self.rows):
        for j in range(self.cols):
            result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

def multiply(self, other):
    if self.cols != other.rows:
        raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы")
    result = Matrix(self.rows, other.cols)
    for i in range(self.rows):
        for j in range(other.cols):
            for k in range(self.cols):
                result.data[i][j] += self.data[i][k] * other.data[k][j]
    return result

def transpose(self):
    result = Matrix(self.cols, self.rows)
    for i in range(self.rows):
        for j in range(self.cols):
            result.data[j][i] = self.data[i][j]
    return result

def __str__(self):

    res = "\n".join(["\t".join(map(str, row)) for row in self.data])
    return res

m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]
m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

print("Матрица 1:")
print(m1)
print("Матрица 2:")
print(m2)
print("Сложение матриц:")
print(m1.add(m2))
print("Вычитание матриц:")
print(m1.subtract(m2))
m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]
print("Умножение матриц:")
print(m1.multiply(m3))
print("Транспонирование матрицы 1:")
print(m1.transpose())



# Задача 2. Магия
# Для одной игры необходимо реализовать механику магии, где при соединении
# двух элементов получается новый. У нас есть четыре базовых элемента:
# «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм»,
# «Пар», «Грязь», «Молния», «Пыль», «Лава».
# Таблица преобразований:
# ● Вода + Воздух = Шторм;
# ● Вода + Огонь = Пар;
# ● Вода + Земля = Грязь;
# ● Воздух + Огонь = Молния;
# ● Воздух + Земля = Пыль;
# ● Огонь + Земля = Лава.
# Напишите программу, которая реализует все эти элементы. Каждый элемент
# необходимо организовать как отдельный класс. Если результат не определён,
# то возвращается None.
# Примечание: сложение объектов можно реализовывать через магический
# метод __add__, вот пример использования:
# class ExampleOne:
# def __add__(self, other):
# return ExampleTwo()
# class ExampleTwo:
# answer = 'сложили два класса и вывели'
# first_example = ExampleOne()
# second_example = ExampleTwo()
# result = first_example + second_example
# print(result.answer)
# Дополнительно: придумайте свой элемент (или элементы) и реализуйте его
# взаимодействие с остальными.

import random
TRIES = 10

class Storm:
    answer = "Вы сложили Воду и Воздух и получили класс Шторм"
class Steam:
    answer = "Вы сложили Воду и Огонь и получили класс Пар"
class Mud:
    answer = "Вы сложили Воду и Землю и получили класс Грязь"
class Bolt:
    answer = "Вы сложили Воздух и Огонь и получили класс Молния"
class Dust:
    answer = "Вы сложили Воздух и Землю и получили класс Пыль"
class Lava:
    answer = "Вы сложили Огонь и Землю и получили класс Лава"

class Fog:
    answer = "Вы сложили Воду и Пыль и получили класс Туман"

class Water:
    def __add__(self, other):
        if isinstance(other, Soil):
            return Mud()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Dust):
            return Fog() 
class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Bolt()
        elif isinstance(other, Soil):
            return Lava()
class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Bolt()
        elif isinstance(other, Soil):
            return Dust()
class Soil:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()

def main():
    elements = [Water(), Fire(), Air(), Soil(), Dust()] 

    try_count = 0
    while try_count < TRIES:
        element_a = random.choice(elements)
        element_b = random.choice(elements)
        result = element_a + element_b
    if result is None:
        continue
    try_count += 1
    print(result.answer)
    print()
main()



# Задача 3. Класс Rectangle - работа с прямоугольниками
# Разработайте программу для работы с прямоугольниками. Необходимо создать класс
# Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
# Атрибуты класса:
# width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
# Методы класса:
# __init__(self, width, height=None): Конструктор класса. Принимает ширину и
# высоту прямоугольника. Если высота не указана (по умолчанию None), то считается, что
# прямоугольник является квадратом, и высота устанавливается равной ширине.
# perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое
# число - значение периметра.
# area(self): Метод для вычисления площади прямоугольника. Возвращает целое число -
# значение площади.
# __add__(self, other): Магический метод, который определяет операцию сложения (+)
# для двух прямоугольников. Принимает другой прямоугольник other. Создает новый
# прямоугольник, который представляет собой объединение исходных прямоугольников по
# периметру. Новая ширина и высота вычисляются также на основе объединения.
# Возвращает новый прямоугольник.
# __sub__(self, other): Магический метод, который определяет операцию вычитания (-)
# одного прямоугольника из другого. Принимает вычитаемый прямоугольник other. Создает
# новый прямоугольник, представляющий разницу периметров исходных прямоугольников, и
# вычисляет высоту на основе этой разницы. Новая ширина вычисляется также на основе
# разницы. Возвращает новый прямоугольник.
# __lt__(self, other): Магический метод, который определяет операцию "меньше" (<)
# для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если
# площадь первого прямоугольника меньше площади второго, иначе False.
# __eq__(self, other): Магический метод, который определяет операцию "равно" (==)
# для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если
# площади равны, иначе False.
# __le__(self, other): Магический метод, который определяет операцию "меньше или
# равно" (<=) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает
# True, если площадь первого прямоугольника меньше или равна площади второго, иначе
# False.
# __str__(self): Магический метод, возвращающий строковое представление
# прямоугольника. Возвращает строку, описывающую ширину и высоту прямоугольника в
# виде:
# Прямоугольник со сторонами 2 и 3,
# где первое число - это ширина, а второе - высота.
# __repr__(self): Магический метод, возвращающий строковое представление
# прямоугольника, которое может быть использовано для создания нового объекта такого же
# класса с теми же атрибутами.
# Пояснение:
# Метод __add__ объединяет два прямоугольника по периметру и создает новый
# прямоугольник.
# Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров
# исходных прямоугольников, и создает новый прямоугольник.
# Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
# Методы __str__ и __repr__ предоставляют строковое представление объекта класса
# Rectangle.


class Rectangle:
    def __init__(self, width, height=None):

        self.width = width
        self.height = height if height is not None else width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):

        new_perimeter = self.perimeter() + other.perimeter()

        new_width = new_perimeter // 4
        new_height = new_width
        return Rectangle(new_width, new_height)

    def __sub__(self, other):

        new_perimeter = abs(self.perimeter() - other.perimeter())

        new_width = new_perimeter // 4
        new_height = new_width
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}") 
print(f"Площадь rect2: {rect2.area()}") 

print(f"rect1 < rect2: {rect1 < rect2}") 
print(f"rect1 == rect2: {rect1 == rect2}") 
print(f"rect1 <= rect2: {rect1 <= rect2}") #
rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}") 
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}") 
print(rect3) 
print(repr(rect4)) 



# Задача 4. Стек
# В программировании нередко необходимо создавать свои собственные
# структуры данных на основе уже существующих. Одной из таких базовых
# структур является стек.
# Стек — это абстрактный тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл —
# первым вышел»).
# Простой пример: стек из книг на столе. Единственной книгой, обложка которой
# видна, является самая верхняя. Чтобы получить доступ, например, к третьей
# снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.
# Напишите класс, который реализует стек и его возможности (достаточно будет
# добавления и удаления элемента).
# После этого напишите ещё один класс — «Менеджер задач». В менеджере задач
# можно выполнить команду «новая задача», в которую передаётся сама задача
# (str) и её приоритет (int). Сам менеджер работает на основе стека (не
# наследование). При выводе менеджера в консоль все задачи должны быть
# отсортированы по следующему приоритету: чем меньше число, тем выше задача.
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с
# дубликатами.


class Stack:
    def __init__(self):

        self.__stack = list()
    def pop(self):

        if self.is_empty():
            return None
        return self.__stack.pop()
    def push(self, item):

        self.__stack.append(item)
    def is_empty(self):

        return len(self.__stack) == 0
    def top(self):

        if self.is_empty():
            return None
        return self.__stack[-1]
class TaskManager:
    def __init__(self):

        self.tasks = dict()
    def new_task(self, text, priority):

        if priority not in self.tasks:
        self.tasks[priority] = Stack()

        self.tasks[priority].push(text)
    def remove_task(self, text):

        for stack in self.tasks.values():

            temp_stack = Stack()
        while not stack.is_empty():
            task = stack.pop()
        if task != text:
            temp_stack.push(task)

        while not temp_stack.is_empty():
            stack.push(temp_stack.pop())
    def __str__(self):

        sorted_keys = sorted(self.tasks.keys())
        out = []
        for key in sorted_keys:
            task_line = [str(key)] 
            temp_stack = Stack()
        while not self.tasks[key].is_empty():
            task = self.tasks[key].pop()
            temp_stack.push(task)
        while not temp_stack.is_empty():
            task_line.append(temp_stack.pop())
    
            out.append(' '.join(task_line))
            return '\n'.join(out)
    def main():
        manager = TaskManager()
        manager.new_task("сделать уборку", 4)
        manager.new_task("помыть посуду", 4)
        manager.new_task("отдохнуть", 1)
        manager.new_task("поесть", 2)
        manager.new_task("сдать дз", 2)

    print(manager)

manager.remove_task("поесть")
print("\nПосле удаления задачи:")
print(manager)
main()




# Задача 5. Абстрактный класс
# Вы работаете в компании, занимающейся разработкой программного обеспечения
# для архитектурных проектов. Вам необходимо разработать программу для расчёта
# площади различных геометрических фигур, таких как круги, прямоугольники и
# треугольники.
# Задача
# Создайте:
# ● класс Shape, который будет базовым классом для всех фигур и будет
# хранить пустой метод area, который наследники должны переопределить;
# ● класс Circle;
# ● класс Rectangle;
# ● класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод
# для вычисления площади фигуры.



import math
from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):

        pass
class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius
    def area(self):

        return math.pi * self.radius ** 2
class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width
        self.height = height
        def area(self):

            return self.width * self.height
class Triangle(Shape):

    def __init__(self, base, height):

    self.base = base
    self.height = height
    def area(self):

        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)

try:
    shape = Shape() 
    except TypeError as e:
print(f"Ошибка: {e}")
