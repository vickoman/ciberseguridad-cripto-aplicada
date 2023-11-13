# Import base64
import base64

# Value del hex
hex_value = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Obtener los bytes
bytes = bytes.fromhex(hex_value)

# Decodificar a legible por humanos
result = base64.b64encode(bytes).decode('utf-8')

# Imprimir el valor Hexadecimal
print(result)