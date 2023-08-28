"""Программа загадывает число от 0 до 1000. Необходимо угадать число
за 10 попыток. Программа должна подсказывать “больше” или “меньше”
после каждой попытки."""

from random import randint


class Games:
    MIN_NUM = 0
    MAX_NUM = 1000
    num = randint(MIN_NUM, MAX_NUM)
    LIMIT = 4

    def guess_game(self):
        while self.LIMIT > 0:
            entered_number = int(input("Введите число больше 0, но меньше "
                                       "1000: "))
            self.LIMIT -= 1
            if self.num == entered_number:
                rez = "Ура!!! Вы угадали!!!"
                return rez
            elif entered_number > self.num:
                print(f"Число меньше введённого!!! Осталось попыток: {self.LIMIT}")
            elif entered_number < self.num:
                print(f"Число больше введённого!!! Осталось попыток: {self.LIMIT}")
        return "Попытки кончились"


test = Games()
print(test.guess_game())