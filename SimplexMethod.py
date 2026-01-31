


def SimplexMethod(restricciones_valores = [[1,2],[3,2],[5,2]],restricciones_solucion = [80,160,200],funcion_objetivo = [2000,2000],igualidades = ['>=','>=','>='],isMin = True):
    print(len(restricciones_valores))
    matrix_x = []
    matrix_y = []
    
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

SimplexMethod()