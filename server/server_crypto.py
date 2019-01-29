from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import NoEncryption

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def CreateServerRSA():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    try:
        os.mkdir(str(os.getcwd()) + "/RSA")
    except OSError:
        pass

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM, 
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("RSA/private_key.pem", 'wb') as private_pem_out:
        private_pem_out.write(private_pem)


    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
    )
    with open("RSA/public_key.pem", 'wb') as public_pem_out:
        public_pem_out.write(public_pem)
 

def DecryptRSA(dataFromClient):
    print("Data: " + str(dataFromClient))
    private_key = _LoadServer_Private_RSA()
    decrypted = private_key.decrypt(
        dataFromClient,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Decrypted ", str(decrypted))
    return decrypted.decode(errors='replace')   #decoded!



def _LoadServer_Private_RSA():
    if (not(os.path.exists("RSA/private_key.pem"))):
        CreateServerRSA()
    with open("RSA/private_key.pem", 'rb') as pem_in:
        pemlines = pem_in.read()
    private_key = serialization.load_pem_private_key(
        pemlines, 
        None, 
        default_backend()
    )
    return private_key
 
def LoadServerPublicRSA(private_key):
    return private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
        )