import numpy as np
import logging

FORMAT = '{levelname} - {asctime} {msg}'
logging.basicConfig(filename='logs.log', level=logging.INFO, filemode="w", format=FORMAT, style='{')
log = logging.getLogger(__name__)


class Matrix:

    def __init__(self, martix1: list, matrix2: list):

        CORRECT_TYPE = type(np.array([]))
        if type(martix1) == CORRECT_TYPE and type(matrix2) == CORRECT_TYPE:
            self.matrix1 = martix1
            self.matrix2 = matrix2
        else:
            log.error(f'Аргументом в конструкторе экземпляра класса "Matrix" может быть "numpy.ndarray",'
                      f' но на самом деле "martix1" - это {type(martix1)}, "matrix2" это {type(matrix2)}')

    def __repr__(self):
        return print(f'{self.matrix1, self.matrix2}')

    def summ_matrixs(self) -> list:
        """Метод возвращает сумму двух матриц, созданных с помощью библиотеки numpy"""
        sum_of_matrices = self.matrix1 + self.matrix2
        log.info(f'Результатом работы функции "summ_matrixs" будет {sum_of_matrices}:')
        return sum_of_matrices

    def equal_matrixs(self) -> bool:
        """Метод сравнивает две матрицы, созданных с помощью библиотеки numpy"""
        is_equal_matrix = np.array_equal(self.matrix1, self.matrix2)
        log.info(f'Результатом работы функции "equal_matrixs" будет "{is_equal_matrix}"')
        return is_equal_matrix


if __name__ == '__main__':
    MAT1 = np.array([[3, 9, 6], [13, 33, 42]])
    MAT2 = np.array([[8, 7, 42], [7, -4, 20]])
    exemplar = Matrix(MAT1, MAT2)
    result_matrix = exemplar.summ_matrixs()
    is_equal = exemplar.equal_matrixs()
    print(result_matrix)
    print(is_equal)

