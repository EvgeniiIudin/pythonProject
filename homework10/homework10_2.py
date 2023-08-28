"""Треугольник существует только тогда, когда сумма любых двух его сторон
больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует. Отдельно сообщить
является ли треугольник разносторонним, равнобедренным или равносторонним."""

class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def check(self):
        if self.a > self.b + self.c or self.b > self.a + self.c \
                or self.c > self.a + self.b:
            return f"С такими сторонами треугольника не существует"
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return f"Разносторонний треугольник"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return f"Равнобедренный треугольник "


test = Triangle(1, 2, 3)
print(test.check())