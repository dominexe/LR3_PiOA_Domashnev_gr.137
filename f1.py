import numpy as np

# Преобразует ввод пользователя в число

def parse_value(val):
    if "/" in val:
        num, den = val.split("/")
        return float(num) / float(den)
    return float(val)

# Создаёт матрицу попарных сравнений

def input_matrix(names):
    n = len(names)
    matrix = np.ones((n, n))
    print("\nВведите попарные сравнения (шкала Саати):")
    print("Пример: 3 или 1/3\n")
    for i in range(n):
        for j in range(i + 1, n):
            val = input(f"{names[i]} vs {names[j]}: ")
            value = parse_value(val)
            matrix[i][j] = value
            matrix[j][i] = 1 / value
    return matrix

# Нормализует матрицу (делит каждый столбец на его сумму)

def normalize_matrix(matrix):
    col_sum = np.sum(matrix, axis=0)
    return matrix / col_sum

#Находит веса (приоритеты)

def priority_vector(matrix):
    norm = normalize_matrix(matrix)
    return np.mean(norm, axis=1)