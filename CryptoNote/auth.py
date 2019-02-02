import client
import json
import datetime 

import client_crypto
import crypto_fernet
import database
import Util.json_creator as jc
#import base64

def Register():
    sock = client.ConnectToServer()
    print("Connected to server\n\nPlease enter your Email: ")
    user_email = "as.weiss@ya.ru" #input()
    key = crypto_fernet.RandomKey()
    #print("Key: %s Data: %s" % (str(key), str(datetime.date.today()) ) )

    newKey = key.decode("utf-8")
    

    database.InsertKey("ServerKey", str(newKey), str(datetime.date.today()) )

    send_request = {"type": "Register", "email": user_email, "key": database.GetData("ServerKey")} #str(key)
    encrypted_request = client_crypto.EncryptRSA(send_request)
    #sock.send(json.dumps(encrypted_request).encode())
    print("From DataBase: %s" % database.GetData("ServerKey"))

    to_send =  jc.Create(encrypted_request, "")
    
    print("Json look like: " + str(to_send) )

    sock.send(to_send)
    status = sock.recv(1024)
    key = database.GetData("ServerKey").encode() 
    print("key: " + str(key) )
    dec = crypto_fernet.Decrypt(key, status)
    print(dec)