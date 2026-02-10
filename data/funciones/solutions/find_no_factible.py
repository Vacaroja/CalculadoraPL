def no_factible(var_standard):
    for var in var_standard:
        if var.startswith("R"):
            return True
    return False
    