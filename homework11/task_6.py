"""Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения"""

class Rectangle:

    """Класс позволяет складывать и вычитать периметры треугольников,
        а также поддерживает операции сравнения треугольников"""
    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
    def get_area(self):
        return self.side_a * self.side_b
    def __add__(self, other):
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)
    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)
    def __eq__(self, other):  # равно ==
        return self.get_area() == other.get_area()
    def __ne__(self, other):  # неравно !=
        return self.get_area() != other.get_area()
    def __gt__(self, other):  # больше >
        return self.get_area() > other.get_area()
    def __ge__(self, other):  # больше или равно >=
        return self.get_area() >= other.get_area()
    def __lt__(self, other):  # метод меньше <
        return self.get_area() < other.get_area()
    def __le__(self, other):  # меньше или равно <=
        return self.get_area() <= other.get_area()
rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)