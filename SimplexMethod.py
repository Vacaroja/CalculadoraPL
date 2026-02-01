


def SimplexMethod(restricciones_valores = [[1,2],[3,2],[5,2]],restricciones_solucion = [80,160,200],funcion_objetivo = [2000,2000],igualidades = ['>=','>=','>='],isMin = True):
    print(len(restricciones_valores))
    matrix_y = [[1,-30,-40,0,0,0]
                [0,1,3,1,0,120]
                [0,3,4,0,1,180]]
    
    var_h= 0
    for i in range(len(restricciones_valores)):
        for e in range(len(restricciones_valores)):
            if e == var_h:
                matrix_x.append(1)
            else:
                matrix_x.append(0)
        var_h+= 1
        matrix_y.append(matrix_x)
        matrix_x = []
    print(matrix_y)
    matrix_h = []

#encontrar fila y columna pivote
def encontrar_pivote(matrix):
    pivot_col = 0
    pivot_row = 0
    val_solucion = len(matrix[0])
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

#crea nueva matriz pivoteada
def pivotear(matrix, pivot_row, pivot_col):
    pivot_value = matrix[pivot_row][pivot_col]
    matrix[pivot_row] = [x / pivot_value for x in matrix[pivot_row]]

    for i in range(len(matrix)):
        if i != pivot_row:
            row_factor = matrix[i][pivot_col]
            matrix[i] = [matrix[i][j] - row_factor * matrix[pivot_row][j] for j in range(len(matrix[i]))]

    return matrix

SimplexMethod()