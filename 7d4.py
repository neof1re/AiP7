group1 = ["Иванов", "Гузликов", "Немощев", "Кизяков", "Жидов", "Дубов", "Газанов", "Багов", "Авдеев", "Жмышенко"]
group2 = ["Голубев", "Орлов", "Трущев", "Сорокин", "Савельев", "Лебедев", "Санюрик", "Бака", "Шмурдяк", "Роналдо"]
team = tuple(group1[:5] + group2[:5])
print("Группа 1:", group1)
print("Группа 2:", group2)
print("Команда:", team)
print("Длина кортежа:", len(team))
team_sorted = tuple(sorted(team))
print("Отсортированная команда:", team_sorted)
count_ivanov = team_sorted.count("Иванов")
print("Иванов в команде:", "Да" if count_ivanov > 0 else "Нет")
print("Иванов встречается", count_ivanov, "раз(а)")