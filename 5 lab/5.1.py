n = []
qq = 0
for i in range(15):
    print('Введите элемент ', i+1, end=' - ')
    n.append(int(input()))
    qq = qq + n[i]
qq1 = qq / 15
n1 = []
for i in range(15):
    n1.append(n[1] * qq1)
print(qq1)