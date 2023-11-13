from cryptography.hazmat.primitives import serialization
import base64

def get_subdomain_from_pem():
    with open('./transparency.pem', 'rb') as pem_file:
        pem_data = pem_file.read()
        cert = serialization.load_pem_public_key(pem_data)
        modulus = cert.public_numbers().n
        hex_value = hex(modulus)[2:]
        bytes_value = bytes.fromhex(hex_value)
        print(bytes_value)
        # string = bytes_value.decode('utf-8')
        print(bytes_value.decode('utf-8'))
        # Decodificar a legible por humanos
        # result = base64.b64encode(bytes_value).decode('utf-8')
        # result = bytes_value.decode('utf-8')
        return modulus

get_subdomain_from_pem()

# Este codigo no funciona no puedo leer el public key y obtener el subdominio sin embargo lo encontre con: https://crt.sh/?q=cryptohack.org
