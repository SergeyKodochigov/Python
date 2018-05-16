k = int(input('введите число k'))
l = int(input('введите число l'))
n = int(input('введите число n'))
m = int(input('введите число m'))

if (k == 0) and (l > m):
    print('true')
elif (k < 0) and ((2*l - 3*n) < m):
    print('true')
else:
    print('false')
