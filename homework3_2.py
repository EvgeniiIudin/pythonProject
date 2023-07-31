"Дан список повторяющихся элементов."
"Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов."

list_of_items = [1, 2, 2, 3, 5, 5, 2, 8, 9, 9, 3, 7]

for i in list_of_items:
    count = 0
    for j in list_of_items:
        if i == j:
            count += 1
    if count < 2:
        list_of_items.remove(i)

print(list_of_items)

unique_list = set(list_of_items)
result_list = list(unique_list)
print("Список уникальных дублирующихся элементов:", result_list)