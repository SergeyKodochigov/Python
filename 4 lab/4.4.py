mas = ['', '']
for i in range(len(mas)):
    mas[i] = input('Напишите слово')
qq1 = len(mas[0])
qq2 = len(mas[1])
c = 0
for i in mas[0]:
    for j in mas[1]:
        if i == j:
            c = c + 1
ggg = c / ((qq1 + qq2) - c)
print(ggg)