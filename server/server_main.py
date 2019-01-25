import socket
import json
import server_crypto
import time

sock = socket.socket()
isNotConnected = True

while isNotConnected: 
    try:
        sock.bind(('', 4090))
        isNotConnected = False
        print("Connected")
    except Exception as e:
        print(str(e))
        time.sleep(5)

sock.listen(1)

while True:
    try:

        conn, addr = sock.accept()

        print("connected: "+ str(addr))
        data = conn.recv(1024)
        json_fromClient = json.loads(data.decode()) #json.loads(data.decode())
        print(json_fromClient["type"])
        if (json_fromClient["type"]=="GetKey"):
            server_crypto.CreateServerRSA()
            #print(server_crypto.LoadServerPublicRSA(server_crypto._LoadServer_Private_RSA()))
        if not data:
            break
        conn.send(("some key here!").encode()) #upper!
        conn.close()
    except Exception as e:
        print(str(e))
        break  