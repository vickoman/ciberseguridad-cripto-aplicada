
from Crypto.PublicKey import RSA

def read_rsa_key():
    with open('privacy_enhanced_mail.pem', 'r') as f:
        key = RSA.import_key(f.read())
    return key
print(read_rsa_key().d)
