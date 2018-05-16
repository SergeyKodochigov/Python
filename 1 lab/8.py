a = [5, 2, 5, 8, 8, 9]
b = False
q = 0
l = 0

for i in range(0, len(a)):
    q = a[i]
    if q == l:
        b = True
    l = a[i]
print(b)
