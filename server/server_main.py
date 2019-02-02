import socket
import json
import server_crypto
import time
import server_requestHandler
import ast
import base64

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


            json_fromClient = json.loads(data.decode()) 
            
            print("Data len: %s" % len(data) )
            print("Str json_fromClient[header] " + json_fromClient["header"])
            
            header = base64.b64decode( json_fromClient["header"] )

            print("Header len: %s" % len(header))

            print(str(server_crypto.DecryptRSA( header ) ) )

            try:        #TODO Test this 
                dec =  server_crypto.DecryptRSA(header)
                dictionary = ast.literal_eval( str( dec ))
            except Exception as e:
                dictionary  = {
                    "type": "Error",
                    "name_Error": str(e)
                }


            print(dictionary["type"])
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