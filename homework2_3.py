import fractions, math

"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions."""

fract_1 = str(input("Введите 1-ю дробь: "))
fract_2 = str(input("Введите 2-ю дробь: "))
list1 = fract_1.split('/')  # разделяю строку на числа инт
list2 = fract_2.split('/')
numenator1 = int(list1[0])  # из индексов списка беру числители и знаменатели
denominator1 = int(list1[1])
numenator2 = int(list2[0])
denominator2 = int(list2[1])
print(numenator1, denominator1, numenator2, denominator2)  # вывожу все числа для проверки

nok = math.lcm(denominator1, denominator2)  # вычисляю нок)
ratio_fract1 = nok / denominator1
new_numenator1 = ratio_fract1 * numenator1
ratio_fract2 = nok / denominator2
new_numenator2 = ratio_fract2 * numenator2
product_numenator = numenator1 * numenator2
summ_ratio = int(new_numenator1 + new_numenator2)
product_denominator = denominator1 * denominator2
nod1 = math.gcd(summ_ratio, nok)
nod2 = math.gcd(product_numenator, product_denominator)
print("Моё решение: ")
print(f'{(new_numenator1 + new_numenator2) / nod1}/{nok / nod1}')
print(f'{product_numenator / nod2}/{product_denominator / nod2}')

print("Проверочные методы с помощью функции 'fraction':")
print(f"{fract_1} + {fract_2} = {fractions.Fraction(fract_1) + fractions.Fraction(fract_2)}")
print(f"{fract_1} * {fract_2} = {fractions.Fraction(fract_1) * fractions.Fraction(fract_2)}")