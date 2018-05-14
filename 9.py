n = int(input('Введите кол-во элементов в массиве'))
a = [int(input()) for x in range(n)]
q = 0
l = 0
b = 0
for i in range(0, len(a)):
    q = a[i]
    if q > l and q > b:
        b = q
        l = a[i]
    elif l > q:
        b = l

print(b)
