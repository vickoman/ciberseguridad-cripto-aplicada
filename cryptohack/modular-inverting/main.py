
# Funcion para invertir el modulo siguiendo el teorema de Fermat
def inverse_modulo(a, p):
    return pow(a, p-2, p)

d = inverse_modulo(3, 13)
print(d)
