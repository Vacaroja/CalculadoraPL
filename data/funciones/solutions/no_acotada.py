def no_acotada(matriz,pivot_col):
    for i in range(1,len(matriz)):
        if matriz[i][pivot_col] > 0:
            return False
    return True