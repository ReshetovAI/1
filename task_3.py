# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int(input('Введите координату по оси x: '))
y = int(input('Введите координату по оси y: '))
if x > 0 and y > 0:
    print('Ваша точка находится в плоскости: 1')
if x < 0 and y > 0:
    print('Ваша точка находится в плоскости: 2')
if x < 0 and y < 0:
    print('Ваша точка находится в плоскости: 3')
if x > 0 and y < 0:
    print('Ваша точка находится в плоскости: 4')
if x == 0:
    print('Ваша точка лежит на оси х')
if y == 0:
    print('Ваша точка лежит на оси y')  

