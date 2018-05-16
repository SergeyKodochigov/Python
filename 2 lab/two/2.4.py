import math
a = int(input('введите сторону квадрата - A\n'))
r = float(input('введите радиус - R\n'))

pkv = a**2
pkr = math.pi*r**2

if pkv > pkr:
    print('площадь квадрата больше т.к ', pkv, '>', pkr)
else:
    print('площадь круга больше т.к ', ("%.2f" % pkr), '>', pkv)