def get_matrix(n, m, value):
    m121atrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append([value])
    print(matrix)
    return matrix


n = int(input('Задайте количество строк матрицы :'))
m = int(input('Задайте количество столбцов матрицы :'))
value = input("Задайте значения матрицы : ")
print('-------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print("Матрица пуста, задано неверное количество строк:", n)
elif m <= 0:
    print("Матрица пуста, задано неверное количество столбцов:", m)
else:
    print("Матрица воплоти:")
    for i in matrix:
        print(*i)
