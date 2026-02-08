from data.metodos.simplex.SimplexMethod import SimplexMethod,SimplexMethodTwoFases,add_holgura_or_artifical_val

def Twofases(old_matrix,old_name_variable,igualidades,old_variable_standard,isMin):
    name_variable = old_name_variable
    name_variable_Second_fase = []
    #primero se normaliza la funcion colocando las variables de holgura y artificiales
    #esta funcion devuelve las variables de holgura y artificiales
    matrix,var_names = add_holgura_or_artifical_val(old_matrix,igualidades)
    #coloca las variables S y R junto con las demas
    name_variable.extend(var_names)
    #este coloca unicamente las R y S necesarias para la parte inicial de la primera fase
    old_variable_standard.extend(put_inicial_standard(len(matrix),var_names))
    #luego reemplaza la primera columna con el r=R+R
    matrix_first_fase,fila_borrada = add_artifical_row(matrix,name_variable)
    #funcion para multiplicar la funcion principal para estandarizar las "R"
    matrix_first_fase = definir_fila_artificial(matrix_first_fase,name_variable)
    
    matrix,name_variable,variable_standard = SimplexMethodTwoFases(matrix_first_fase,name_variable,old_variable_standard,isMin=True)
    name_variable_Second_fase.extend(name_variable)
    print(name_variable)
    print(name_variable_Second_fase)
    matrix_secondfase,name_variable_Second_fase = delete_artificial_vars(matrix,name_variable_Second_fase,fila_borrada)
    print(name_variable)
    print(name_variable_Second_fase)
    matrix_secondfase,name_variable_Second_fase,variable_standard = SimplexMethodTwoFases(matrix_secondfase,name_variable_Second_fase,variable_standard,isMin=isMin)
    print("Resultado Final:")
    for e in matrix_secondfase:
        for i in e:
            print(i)
    print(name_variable_Second_fase)
    print(name_variable_Second_fase)
    return matrix,matrix_secondfase,name_variable,name_variable_Second_fase,variable_standard

#funcion que devuelve la lista de variables iniciales para la primera fase
def put_inicial_standard(max_standard,variable_names):
    #primero las ordena y las junta R con R y S con S
    arregladas = sorted(variable_names)
    #crea una lista vacia para guardar las variables
    lista_extendida = []
    #itera con el maximo necesario -1 debido a la Z
    for e in range(max_standard-1):
        lista_extendida.append(arregladas[e])
    return lista_extendida

#funcion para multiplicar la funcion principal para estandarizar las "R"
def definir_fila_artificial(matrix,name_variable):
    fila_artificial = 0
    total_matrix = len(matrix[0])
    suma_artificial = 0
    matriz_nueva = []
    for i in range(len(name_variable)):
        if "R" in name_variable[i]:
            fila_artificial += 1
    for e in range(total_matrix):
        suma_artificial = 0
        for i in range(fila_artificial+1):
            suma_artificial += matrix[i][e]
        matriz_nueva.append(suma_artificial)
    matrix[0] = matriz_nueva
    return matrix
    

def delete_artificial_vars(matrix,name_variable,fila_borrada):
    indices_a_borrar = []
    last_matrix = [row[:] for row in matrix[-1]]
    del last_matrix[0]
    last_matrix.insert(0,fila_borrada)
    for i in range(len(name_variable)):
        if "R" in name_variable[i]:
            indices_a_borrar.append(i)
    
    for index in sorted(indices_a_borrar,reverse=True):
        for row in last_matrix:
            print(row)
            del row[index]
        del name_variable[index]
    
    return last_matrix,name_variable

def add_artifical_row(old_matrix,var_names):
    matrix = old_matrix.copy()
    indices_a_cambiar = [1]
    fila_borrada = []
    
    for i in range(1,len(var_names)):
        if "R" in var_names[i]:
            indices_a_cambiar.append(-1)
        else:
            indices_a_cambiar.append(0)
    indices_a_cambiar.append(matrix[0][-1])
    fila_borrada = matrix[0]
    del matrix[0]
    matrix.insert(0,indices_a_cambiar)
    return matrix,fila_borrada

matrix=[
    [1, -4, -1, 0],  # Z, x1, x2, RHS
    [0, 3, 1, 3],  # Restricción 1
    [0, 4, 3, 6],  # Restricción 2
    [0, 1, 2, 4]  # Restricción 3
]

igualidades = ["=","=", ">=", "<="]

variable_standard = ['Z']

name_variable = ["Z","X1","X2"]


