import math
k = int(input('Введите значение'))
w = 0
for i in range(1,k):
    w = w + ((((-1)^i)*(i-3)^2)/(math.factorial(i)))
print (w)