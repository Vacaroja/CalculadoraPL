def ordenador(diccionario):
    lista_inicial = []
    lista_inicial = [list(map(float, v)) for k, v in diccionario.items() if '[]' in k]
    
    lista_traspuesta = list(zip(*lista_inicial))
    columnas_revertidas = [list(c)[::-1] for c in lista_traspuesta]
    columnas_revertidas = add_zeros(columnas_revertidas)
    return columnas_revertidas

def add_zeros(matrix):
    max_length = len(matrix)
    
    for i in range(max_length):
        if i == 0:
            matrix[i].append(0)
        else:
            matrix[i].insert(0, 0)
    return matrix