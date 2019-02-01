import socket
import json
import server_crypto
import time
import server_requestHandler
import ast

try:
    sock = socket.socket()
    isNotConnected = True

    #server_crypto.CreateServerRSA()

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
            #json_fromClient = json.loads(data.decode()) #json.loads(data.decode())

            print(str(server_crypto.DecryptRSA(data)) )

            dictionary = ast.literal_eval( str(server_crypto.DecryptRSA(data) ))

            _json_toClient = server_requestHandler.Handle( dictionary ) 
            if not data:
                break
            conn.send(_json_toClient)      #json.dumps(_json_toClient).encode())
            #print(str(_json_toClient.decode()))
            conn.close()
        except Exception as e:
            print(str(e))
            time.sleep(1)
            conn.close()
            print("Conn closed!")
            break  
except KeyboardInterrupt:
    print("GoodBye!")