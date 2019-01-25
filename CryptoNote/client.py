import socket
import json
import requests

def ConnectToServer():
        sock = socket.socket()
        sock.connect(('localhost', 9090))
        return sock

def test():
    try:
        sock = socket.socket()
        sock.connect(('localhost', 9090))

        send_request = {"type": "GetKey", "id": "dfs1"}
        sock.send(json.dumps(send_request).encode()) #"Hello, World!".encode()

        data = sock.recv(1024)
        sock.close()

        print("Msg in: " +  data.decode())
    except Exception as e:
        print("Error: ", str(e))

def GetServerKey():
    sock = ConnectToServer()
    send_request = {"type": "GetKey", "id": "dfs1"}
    sock.send(json.dumps(send_request).encode())  #, sort_keys=True
    #sock.send(json.loads('["type": "GetKey", "6": 7]').encode())
    key = sock.recv(1024)
    sock.close()
    return key