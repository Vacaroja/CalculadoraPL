def indices_basicos(variable_names,variable_standard):
    indices = []
    for i in range(len(variable_names)):
        if variable_names[i] in variable_standard:
            indices.append(i)
    return indices

def is_optimal_multiple(matrix,variable_names,variable_standard):
    indices = indices_basicos(variable_names,variable_standard)
    first_row = matrix[0]
    for i in range(len(first_row)-1):
        if i not in indices and abs(first_row[i]) < 1e-9:
            return True
    return False