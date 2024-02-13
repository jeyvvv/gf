#Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т. е. такой матрицей,
# в которой суммы элементов во всех строках и столбцах одинаковы.
# Запрещено использовать словари и множества.
# Запрещено использовать сторонние библиотеки.

def is_magic_square(matrix):
    n = len(matrix)

    # Проверяем суммы элементов в строках
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False

    # Проверяем суммы элементов в столбцах
    col_sums = [sum(column) for column in zip(*matrix)]
    if len(set(col_sums)) != 1:
        return False

    # Проверяем суммы элементов по диагоналям
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n - i - 1] for i in range(n))
    if diag1_sum != diag2_sum or diag1_sum != row_sums[0]:
        return False

    return True


# Пример использования
matrix = [
    [9, 10, 5],
    [4, 8, 12],
    [11, 6, 7]
]
if is_magic_square(matrix):
    print("Данная матрица - магический квадрат")
else:
    print("Данная матрица не является магическим квадратом")