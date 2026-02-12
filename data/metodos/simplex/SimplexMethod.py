import copy
from data.funciones.solutions.find_solution_result import find_solution_result
from data.funciones.solutions.no_acotada import no_acotada 


def SimplexMethod(old_matrix,name_variable,igualidades,variable_standard,isMin):   
    matrix = old_matrix.copy()
    matrix,holgura_and_artificial = add_holgura_or_artifical_val(old_matrix,igualidades)
    variable_standard.extend(holgura_and_artificial)
    name_variable.extend(holgura_and_artificial)
    return SimplexMethodTwoFases(matrix,name_variable,variable_standard,isMin)

def SimplexMethodTwoFases(old_matrix,name_variable,old_variable_standard,isMin):
    matriz_historica = []
    historico_standard = []
    variable_standard = []
    variable_standard.extend(old_variable_standard)
    solucion = '' #la solucion por defecto es optima unica
    acotada = False #variable para determinar si la solucion es acotada o no, se inicializa en False y se cambia a True si se encuentra que no es acotada

    matrix = old_matrix.copy()
    matriz_historica.append(copy.deepcopy(matrix))
    historico_standard.append(copy.deepcopy(variable_standard))
    while True:
        pivote_row, pivote_col,acotada = encontrar_pivote(matrix,isMin)
        if pivote_col is not None:
            try:
                variable_standard[pivote_row] = name_variable[pivote_col]
                historico_standard.append(copy.deepcopy(variable_standard))
            except Exception:
                variable_standard.append(name_variable[pivote_col])
        if (pivote_col == None and pivote_row == None):
            if acotada:
                solucion = 'no acotada'
            break
        matriz_nueva = pivotear(matrix, pivote_row, pivote_col)
        
        matrix = matriz_nueva
        matriz_historica.append(copy.deepcopy(matrix))
    if not acotada:
        solucion = find_solution_result(matriz_historica[-1],pivote_col,variable_standard,name_variable)
    print(historico_standard)
    return matriz_historica,name_variable,historico_standard,solucion

def convert_min_to_max(matrix):
    matrix[0] = [matrix[0][0]] + [-1 * x for x in matrix[0][1:-1]] + [matrix[0][-1]]
    return matrix

def convert_equalities(igualidades):
    new_igualidades = []
    for equal in igualidades:
        if equal == "<=":
            new_igualidades.append(">=")
        elif equal == ">=":
            new_igualidades.append("<=")
        else:
            new_igualidades.append("=")
    return new_igualidades


# encontrar fila y columna pivote
def encontrar_pivote(matrix,is_min):
    pivot_col = 0
    pivot_row = 0
    old_ratio = 0
    val_solucion = len(matrix[0]) - 1
    fila_z_interes = matrix[0][1:val_solucion]
    # determinar si es minimizacion o maximizacion para encontrar el mayor negativo o mayor positivo
    if is_min:
        min_var = max(matrix[0][1:-1])
        if min_var <= 0:
            return None, None, False
    else:
        min_var = min(matrix[0][1:-1])
        if min_var >= 0:
            return None, None, False
        

    

    pivot_col = fila_z_interes.index(min_var)+1
    if no_acotada(matrix,pivot_col):
        return None, None, True

    for j in range(1,len(matrix)):
        if matrix[j][pivot_col] > 0:
            ratio = matrix[j][val_solucion] / matrix[j][pivot_col]
            if ratio < old_ratio or pivot_row == 0:
                old_ratio = ratio
                pivot_row = j

    return pivot_row, pivot_col,False


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


def add_holgura_or_artifical_val(matrix, igualdades):
    num_rows = len(matrix)
    valor = 0
    var_names = []
    

    for i in range(num_rows):
        if i != 0:
            valor += 1 
            equal = igualdades[i]
            if equal == ">=":
                var_names.append(f"S{i}")
                matrix[i].insert(-1, -1)
                var_names.append(f"R{i}")
                matrix[i].insert(-1, 1)
                for other_row in range(num_rows):
                    if other_row != i:
                        matrix[other_row].insert(-1, 0)
                        matrix[other_row].insert(-1, 0)
            else:
                if (equal == "="):
                    var_names.append(f"R{i}")
                else:
                    var_names.append(f"S{i}")
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
igualidades = ["=","<=", "<=", "<="]

variable_standard = ['Z']

name_variable = ["Z","X1","X2"]



"""for i in range(len(variable_standard)):
    print(f"{variable_standard[i]} = {matrix[i][-1]}")"""