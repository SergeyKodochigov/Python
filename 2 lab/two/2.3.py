import math
x = float(input('Введите x'))
y = float(input('Введите y'))

if (x == 1) and (y == 0):
    print('Точка в зоне')
elif (x >= -1) and (x <= 1) and (y <= math.cos(x)) and (y >= 0.5):
    print('Точка в зоне')
else:
    print('Точка не в зоне')