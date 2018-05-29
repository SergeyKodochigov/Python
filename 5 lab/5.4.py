from random import randint

matrix = [[randint(1, 9) for _ in range(5)] for _ in range(6)]
print('исходная матрица\n')
for i in matrix:
    print(i)
blok_min = []
blok_max = []
print('\nсреднее арифметическое , максимум и минимум в каждом столбце\n')
for row, el in enumerate(matrix[0]):
    min_elem = el
    max_elem = el
    average = 0
    average1 = 0
    for i, x in enumerate(matrix):
        average += x[row]
        average1 += x[row]
        if x[row] < min_elem:
            min_elem = x[row]
        if x[row] > max_elem:
            max_elem = x[row]
    blok_min.append(min_elem)
    blok_max.append(max_elem)
    print(row+1, 'Столб =', average / (i + 1), ': min-', blok_min[row], ': max-', blok_max[row])

