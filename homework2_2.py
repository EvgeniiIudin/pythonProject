"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

decimal_number = int(input("Введите десятичное число: "))
print(f'Проверка через функцию "hex": {hex(decimal_number)}')
hexadecimal_digits = "0123456789ABCDEF"
hexadecimal_number = ""

while decimal_number > 0:
    remainder = decimal_number % 16
    hexadecimal_digit = hexadecimal_digits[remainder]
    hexadecimal_number = hexadecimal_digit + hexadecimal_number
    decimal_number //= 16

print("Шестнадцатеричное число:", hexadecimal_number)