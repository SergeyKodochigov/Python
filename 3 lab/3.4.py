n = int(input('Введите число: '))
summa = 0
while n>0:
    n = n // 10
    summa = summa + 1

print ('Сумма чисел равна = ', (summa))
