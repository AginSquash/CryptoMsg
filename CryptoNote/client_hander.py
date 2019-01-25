import client_crypto

def Handler(json_fromServer):
    type_msg = json_fromServer["type"] 
    {
        type_msg == "ServerRSAKey": client_crypto.SetServerRSAKey(json_fromServer["key"])
        
    }
