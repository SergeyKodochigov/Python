import math
mas = []
mas1 = []
for i in range(0, 15):
    mas.append(int(input("Введите элемент")))
for j in mas:
   it = int(float(((math.cos(mas[j]) ** 2) + 2.97 * (math.log(10) ** 2) * (j ** 2))))
   mas1.append(it)
for q in range(0, 15):
    mas.append(mas1[q])
    mas.sort()
print(mas)
