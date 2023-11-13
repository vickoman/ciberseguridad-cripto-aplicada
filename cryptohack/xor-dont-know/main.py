cadena = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
mensaje_encriptado = bytes.fromhex(cadena)

flag_format = b"crypto{"
# Get the key
key = [o1 ^ o2 for (o1, o2) in zip(mensaje_encriptado, flag_format)] + [ord("y")]

flag = []

for i in range(len(mensaje_encriptado)):
    flag.append(
        mensaje_encriptado[i] ^ key[i % len(key)]
    )
flag = "".join(chr(o) for o in flag)
print("Flag:", flag)