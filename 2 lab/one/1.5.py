import math

k = 1
m = 1.8

c = math.cos(m+k**2)**2
x = math.e**(m*k)
y = math.sqrt((x**2 + c**2)*(1/3))
print(str(y))
