mas = []
mas1 = []
for i in range(0, 7):
    mas.append(int(input('Введите 2 значное число')))
    if ((mas[i] > 9) and (mas[i] < 100)):
        u = mas[i]
        u = u // 10
        mas1.append(u)
    else:
        print('Не корректный ввод')
        break
print(mas1)
