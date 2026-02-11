def create_variable_names(cant_var):
    var_names = ['Z']
    for i in range(int(cant_var)):
        var_names.append(f'X{i+1}')
    print(var_names)
    return var_names
    