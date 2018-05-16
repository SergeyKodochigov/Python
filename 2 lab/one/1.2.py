import math
y = int(input('введите число y'))
w = int(input('введите число w'))

v = (((y+2*w)**3) / (math.log(y+0.75)))

print(str(v))
