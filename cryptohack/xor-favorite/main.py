cadena = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

string_ord = [o for o in bytes.fromhex(cadena)]

# Obtener el mayor elemento de la lista 
def get_mx_number(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max

max = get_mx_number(string_ord)
flas = ""

for order in range(max):
    flag_posible_ord = [order ^ o for o in string_ord]
    flag_posible = "".join(chr(o) for o in flag_posible_ord)
    if flag_posible.startswith("crypto"):
        flag = flag_posible
        break

print("Flag:", flag)