import socket
import json
import server_crypto
import time
import server_requestHandler

try:
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
            server_requestHandler.Handle(json_fromClient)    
            if not data:
                break
            conn.send(("some key here!").encode()) #upper!
            conn.close()
        except Exception as e:
            print(str(e))
            conn.close()
            print("Conn closed!")
            break  
except KeyboardInterrupt:
    print("GoodBye!")
    #conn.close()