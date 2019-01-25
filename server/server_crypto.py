from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import NoEncryption

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
 
 