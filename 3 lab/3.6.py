import math
x = int(input('Введите x'))
s = int(input('Введите количество элементов'))
x1 = 5
kek = (x + (x ** (x1) / math.factorial(x1)))
llle = kek
if (s==1):
    print ('ответ = ',x)
elif (s==2):
    print (kek)
else:
    for i in range(3, s):
        x1 = x1 + 4
        gg = (x ** (x1) / math.factorial(x1))
        llle = (llle + gg)
    print (llle)

