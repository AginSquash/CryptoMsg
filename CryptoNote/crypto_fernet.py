from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os.path

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

def encrypt(cipher_key, text_to_encypt):
    cipher = Fernet(cipher_key)
    encrypted_text = cipher.encrypt(text_to_encypt.encode()) 
    return encrypted_text

def decrypt(cipher_key, encrypted_text):
    cipher = Fernet(cipher_key)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text.decode()

def get_key():
    
    if (not(os.path.exists("myprivate.key"))):
        print("Input your super secret pass: ")
        password = input()
        key_file = open("myprivate.key", "w")
        key = GenerationPassToKey(password.encode())
        key_file.write(key.decode())
        key_file.close()
        return key
    else: 
        key_file = open("myprivate.key", "r")
        key = key_file.read()
        key_file.close()
        return key.encode()