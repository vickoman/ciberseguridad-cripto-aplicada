from cryptography.hazmat.primitives.serialization import load_ssh_public_key

# Cargar clave pública SSH desde un archivo
with open('./bruce_rsa.pub', 'rb') as f:
    ssh_public_key = load_ssh_public_key(f.read())

# Extraer el módulo de la clave pública RSA
modulus = ssh_public_key.public_numbers().n
print(modulus)
