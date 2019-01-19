import socket
import json

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
while True:
    conn, addr = sock.accept()

    print("connected: "+ str(addr))

    while True:
        try:
            data = conn.recv(1024)
            json_fromClient = json.loads(data.decode()) #json.loads(data.decode())
            print(json_fromClient["type"])
            if not data:
                break
            conn.send(("some key here!").encode()) #upper!
            conn.close()
        except Exception as e:
            print(str(e))
            break  