days_of_week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
weekend_count = int(input("Сколько выходных дней на неделе вы хотите? "))
if 0 <= weekend_count <= 7:
    weekend_days = list(days_of_week[-weekend_count:])
    work_days = list(days_of_week[:-weekend_count])
    print(f"Ваши выходные дни: {weekend_days}")
    print(f"Ваши рабочие дни: {work_days}")
else:
    print("Ошибка, введите число от 0 до 7")
