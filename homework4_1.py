"""Напишите функцию для транспонирования матрицы"""

def matrix(list_: list[list]) -> list[list]:
    return list(map(list, zip(*list_)))
print(matrix([[1, 2, 3], [4, 5, 6]]))