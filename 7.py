x = int(input('Введите расстояние, которое пробежал спортсмен'))
y = int(input('Введите значение'))

day = 0
raz = 0
while x < y:
    x = x*1.1
    day += 1
print(day)