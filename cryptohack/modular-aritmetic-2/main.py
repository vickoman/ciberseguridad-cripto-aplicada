a = 273246787654
p = 65537

# Funcion obtener el modulo siguiendo el teorema de Fermat
def fermat(p, a):
    if a % p == 0:
        return 0
    else:
        return pow(a, p-1, p)

print(fermat(p, a))
