def normalizar_matriz(matrix,igualdades):
    # Asumimos que tienes una lista que indica el tipo de restricción
    # tipos = ['<=', '>=', '<=']
    for i in range(len(igualdades)):
        if igualdades[i] == '>=':
            # Multiplicamos toda la fila por -1
            matrix[i] = [val * -1 for val in matrix[i]]
    return matrix