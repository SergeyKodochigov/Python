a = int(input('Введите число 1'))
b = int(input('Введите число 2'))
c = int(input('Введите число 3'))

if a > b and a > c:
    print(a, ' -наибольшее число')
elif b > a and b > c:
    print(b, ' -наибольшее число')
else:
    print(c, ' -наибольшее число')
