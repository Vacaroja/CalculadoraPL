def SimplexMethod(
    restricciones_valores=[[1, 2], [3, 2], [5, 2]],
    restricciones_solucion=[80, 160, 200],
    funcion_objetivo=[2000, 2000],
    igualidades=[">=", ">=", ">="],
    isMin=True,
):
    pass


# encontrar fila y columna pivote
def encontrar_pivote(matrix):
    pivot_col = 0
    pivot_row = 0
    val_solucion = len(matrix[0]) - 1
    min_var = min(matrix[0][:-1])

    if min_var >= 0:
        return None, None

    pivot_col = matrix[0].index(min_var)

    for j in range(len(matrix)):
        if matrix[j][pivot_col] > 0:
            ratio = matrix[j][val_solucion] / matrix[j][pivot_col]
            if ratio < pivot_row or pivot_row == 0:
                pivot_row = j

    return pivot_row, pivot_col


# crea nueva matriz pivoteada
def pivotear(matrix, pivot_row, pivot_col):
    pivot_value = matrix[pivot_row][pivot_col]
    matrix[pivot_row] = [x / pivot_value for x in matrix[pivot_row]]

    for i in range(len(matrix)):
        if i != pivot_row:
            row_factor = matrix[i][pivot_col]
            matrix[i] = [
                matrix[i][j] - row_factor * matrix[pivot_row][j]
                for j in range(len(matrix[i]))
            ]

    return matrix


def add_holgura_or_artifical_val(matrix, igualdades,var_names):
    num_rows = len(matrix)
    valor = 0

    for i in range(num_rows):
        if i != 0:
            valor += 1 
            equal = igualdades[i]
            if equal == ">=":
                var_names.append(f"s{i}")
                matrix[i].insert(-1, -1)
                var_names.append(f"a{i}")
                matrix[i].insert(-1, 1)
                for other_row in range(num_rows):
                    if other_row != i:
                        matrix[other_row].insert(-1, 0)
                        matrix[other_row].insert(-1, 0)
            else:
                if (equal == "="):
                    var_names.append(f"a{i}")
                else:
                    var_names.append(f"a{i}")
                matrix[i].insert(-1, 1)
                for other_row in range(num_rows):
                    if other_row != i:
                        matrix[other_row].insert(-1, 0)

    return matrix,var_names


def test_add_holgura_or_artifical_val(matrix, igualidades):
    print(matrix)
    igualidades = [">=", ">=", ">="]
    matriz_nueva = add_holgura_or_artifical_val(matrix, igualidades)
    print(matriz_nueva)


def test_encontrar_pivote(matrix):
    print(matrix)
    pivote_row, pivote_col = encontrar_pivote(matrix)
    print("fila")
    print(pivote_row + 1)
    print("columna")
    print(pivote_col + 1)


def test_pivotear(matrix):
    print(matrix)
    pivote_row, pivote_col = encontrar_pivote(matrix)
    matriz_nueva = pivotear(matrix, pivote_row, pivote_col)
    print(matrix)


matrix = [
    [1, -3, -5, 0],  # Z, x1, x2, RHS
    [0, 1, 0, 4],  # Restricción 1
    [0, 0, 2, 12],  # Restricción 2
    [0, 3, 2, 18],  # Restricción 3
]
igualidades = ["=","<=", "<=", "="]

name_variable = ["Z","X1","X2"]

valor = 0
matrix,name_variable = add_holgura_or_artifical_val(matrix,igualidades,name_variable)
while True:
    valor += 1
    pivote_row, pivote_col = encontrar_pivote(matrix)
    if (pivote_col == None and pivote_row == None) or (valor == 10):
        print(matrix)
        break
    matriz_nueva = pivotear(matrix, pivote_row, pivote_col)
    matrix = matriz_nueva
    print(matrix)
