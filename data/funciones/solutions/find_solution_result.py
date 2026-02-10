
from data.funciones.solutions.is_optimal_multiple import is_optimal_multiple
from data.funciones.solutions.find_no_factible import no_factible


def find_solution_result(matriz,pivot_col,var_standard,variable_names):
    if (no_factible(var_standard)):
        return 'No Factible'
    elif (is_optimal_multiple(matriz,variable_names,var_standard)):
        return 'Optima Multiple'
    else:
        return 'Optima Unica'
    
    
    
            