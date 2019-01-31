import server_crypto

class CreateJson:
    new = {
    "type": "Error"
    }
    def Set(self, data):
        self.new = data
    def Get(self):
        return self.new

CJ = CreateJson()

def Handle(json_fromClient):
    type_msg = json_fromClient["type"] 
    {
        type_msg == "GetKey": GetServerKey(),
        type_msg == "Register": Register(json_fromClient["email"])
        
    }
    return CJ.Get()

def GetServerKey():
    public_key = server_crypto.LoadServerPublicRSA(server_crypto._LoadServer_Private_RSA())
    _json_toClient = {
        "type": "ServerRSAKey",
        "key": str(public_key.decode())
    }

    CJ.Set(_json_toClient)


def Register(email):
    
