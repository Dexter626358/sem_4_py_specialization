# напишите функцию для транспонирования марицы


def creat_2d_matrix(x: int, y: int) -> list:
    """Функция создает новую 2D матрицу и заполняет ее элементами"""
    maxtrix = [[] for i in range(0, x)]
    for elm in maxtrix:
        for j in range(1, y+1):
            elm.append(j)
    return maxtrix


def traspond_2d_matric(matrix: list)-> list:
    """Функция осуществляет переворот матрицы на 90 градусов"""
    x = len(matrix)
    y = len(matrix[0])
    new_matrix = [[0] * x for i in range(0, y)]
    for i in range(0, x):
        for j in range(0, y):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def print_2d_matrix(matrix: list) -> None:
    """Функция печати матрицы"""
    for elm in matrix:
        print(elm)


cre_matrix = creat_2d_matrix(5, 5)
print_2d_matrix(cre_matrix)
print()
print_2d_matrix(traspond_2d_matric(cre_matrix))
