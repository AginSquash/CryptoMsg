import client
import client_crypto
import json

def Register():
    sock = client.ConnectToServer()
    print("Connected to server\n\nPlease enter your Email: ")
    user_email = input()
    send_request = {"type": "Register", "email": user_email}
    encrypted_request = client_crypto.EncryptRSA(send_request)
    sock.send(json.dumps(encrypted_request).encode())