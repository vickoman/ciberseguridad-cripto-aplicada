
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa

# Certificado DER codificado en base64
cert_b64_file = "./2048b-rsa-example-cert.der"

# read .der from directory
with open(cert_b64_file, "rb") as cert_file:
    cert_b64 = cert_file.read()

    # # Decodificar el certificado DER
    cert = x509.load_der_x509_certificate(cert_b64)

    # Obtener la clave pública RSA del certificado
    public_key = cert.public_key()

    if not isinstance(public_key, rsa.RSAPublicKey):
        raise TypeError("La clave pública no es RSA")

    # Obtener el módulo de la clave pública RSA
    modulus = public_key.public_numbers().n

    # Imprimir el módulo como un número decimal
    print(modulus)
