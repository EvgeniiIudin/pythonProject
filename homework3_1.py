"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
        "Петя": ("Палатка", "Котелок", "Топор"),
        "Саша": ("Палатка", "Котелок", "Топор", "Спирт"),
        "Вика": ("Палатка", "Топор", "Спирт")
        }

lst = []
for k, v in data.items():
    lst.append(set(v))

for i in range(len(lst) - 2):
    res_all = lst[i].intersection(lst[i + 1])
    res_all = res_all.intersection(lst[i + 2])

print(f"{res_all} есть у всех")

res_unic = set()

for i in data:
    res_unic = set(data[i])
    for j in data:
        if i != j:
            res_unic = res_unic.difference(set(data[j]))
    if res_unic:
        print(f"Только {i} имеет {res_unic}")

for i in data:
    res_unic = set(data[i])
    res_unic_new = set()
    for j in data:
        if i != j:
            res_unic_new = res_unic_new.intersection(set(data[j])) if res_unic_new else set(data[j])
    if res_unic_new:
        without_item = res_unic_new.difference(res_unic)
        if without_item:
            print(f"Только {i} не имеет {without_item}")