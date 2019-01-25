import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

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

def ServerKey_toText(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
        )