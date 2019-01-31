import client
import json
import datetime 

import client_crypto
import crypto_fernet
import database

def Register():
    sock = client.ConnectToServer()
    print("Connected to server\n\nPlease enter your Email: ")
    user_email = "email here" #input()
    key = crypto_fernet.RandomKey()
    #print("Key: %s Data: %s" % (str(key), str(datetime.date.today()) ) )

    database.InsertKey("ServerKey", str(key), str(datetime.date.today()) )

    send_request = {"type": "Register", "email": user_email, "key": database.GetData("ServerKey")} #str(key)
    encrypted_request = client_crypto.EncryptRSA(send_request)
    #sock.send(json.dumps(encrypted_request).encode())
    print("From DataBase: %s" % database.GetData("ServerKey"))
    sock.send(encrypted_request)