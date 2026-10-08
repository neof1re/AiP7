List = [1, 2, 3, 2, 3, 1, 7, 8]
seen = set()
duplicates = set()
for item in List:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print("Исходный список:", List)
if duplicates:
    print(f"Повторяющиеся элементы: {list(duplicates)}")
else:
    print("Повторяющихся элементов нет")