import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def SetServerRSAKey(key):
    try:
        os.mkdir(str(os.getcwd()) + "/RSA")
    except OSError:
        pass
    with open("RSA/public_key.pem", 'wb') as pem_toWrite:
        pem_toWrite.write(key.encode())

def GetServerRSAKey():
    with open("RSA/public_key.pem", 'rb') as pem_toRead:
        key_fromFile = pem_toRead.read()
    key = serialization.load_pem_public_key(
        key_fromFile,
        default_backend()
        )
    return key


def EncryptRSA(text_to_encrypt):
    public_key = GetServerRSAKey()
    return public_key.encrypt(
        text_to_encrypt,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def ServerKey_toText(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
        )


