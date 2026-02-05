def ordenador(diccionario):
    lista_inicial = [list(map(float, v)) for k, v in diccionario.items() if '[]' in k]
    
    lista_traspuesta = list(zip(*lista_inicial))
    columnas_revertidas = [list(c)[::-1] for c in lista_traspuesta]
    columnas_revertidas = add_zeros(columnas_revertidas)
    return columnas_revertidas

def add_zeros(matrix):
    max_length = len(matrix)
    matriz_nueva = matrix.copy()
    for i in range(max_length):
        if i == 0:
            matriz_nueva[i].append(0)
        else:
            
            matriz_nueva[i].insert(0, 0)
    
    return matriz_nueva