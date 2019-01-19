from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def GenerationPassToKey(password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt(cipher_key):
    cipher = Fernet(cipher_key)
    text = b'My super secret message'
    encrypted_text = cipher.encrypt(text) 
    return encrypted_text

def decrypt(cipher_key, encrypted_text):
    cipher = Fernet(cipher_key)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text

if __name__ == "__main__":
    
    #cipher_key = Fernet.generate_key()
    cipher_key = GenerationPassToKey("testpass1234".encode())
    print(cipher_key)
    enc_text = encrypt(cipher_key)
    print(str(enc_text))
    original = decrypt(cipher_key, enc_text)
    print("\n\n" + original.decode())
    
    txt = "Hello World."