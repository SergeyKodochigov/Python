import  random
n = int(input('Ведите размерность матрицы'))
max = 0
sw = 0
Matrix = [[0 for x in range(n)] for y in range(n)]
for i in range(0,n):
    for j in range(0,n):
        Matrix[i][j] = random.randint(0,9)

for i in range(0,n):
    print(Matrix[i])

for i in range(0,n):
    for j in range(0,n):
        if Matrix[i][j] > max:
            max = Matrix[i][j]
    sw = Matrix[i][i]
    Matrix[i][i] = max
    Matrix[i][j] = sw
    index = 0
    max = 0

print()
for i in range(0,n):
    print(Matrix[i])