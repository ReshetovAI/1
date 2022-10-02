# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример: - 6 -> да - 7 -> да - 1 -> нет


day_number = int(input("Введите число дня недели:   "))

def WeekEnd(number):
    if number > 0 and number <= 7:
        if number > 0 and number <= 5:
            print(f"{number} Будний день.")
        else:
            print(f"{number} Выходной день.")
    else:
        print("число не является днём недели")

WeekEnd (day_number)


