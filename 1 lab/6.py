n = int(input('Введите число'))

j = 0
for i in range(1, n+1):
    j = i*i
    if i*i <= n:
        print(j)
