""" Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя."""

class Archive:
    """Класс сохраняет в архиве атрибуты созданных эксземпляров класса (Переопределены методы __str__ и __repr__)"""
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None
    def __init__(self, num, new_str):
        self.num = num
        self.new_str = new_str
        if Archive.last_num is not None:
            self.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            self.strs_archive.append(Archive.last_str)
        Archive.last_num = num
        Archive.last_str = new_str
    def __str__(self):
        res = f'номер: {self.num}, строка: {self.new_str}, архив: {list(zip(self.nums_archive, self.strs_archive))} '
        return res
    def __repr__(self):
        return f'Archive({self.num = },{self.new_str = })'
if __name__ == '__main__':
    arc1 = Archive(1, "Строка 1")
    print(arc1)
    print(arc1.__repr__())
    arc2 = Archive(2, "Текст 2")
    arc3 = Archive(3, "Symbols 3")
    print(arc3)