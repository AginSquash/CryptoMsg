import server_crypto
import Service.send_email as send_email
import database_Handler
import Util.GetRandom as Rand
import datetime
import json
import base64

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
        type_msg == "Register": Register(json_fromClient) #send_email.RegisterEmail(json_fromClient["email"])

        
    }
    return CJ.Get()

def GetServerKey():
    public_key = server_crypto.LoadServerPublicRSA(server_crypto._LoadServer_Private_RSA())
    _json_toClient = {
        "type": "ServerRSAKey",
        "key": str(public_key.decode())
    }

    CJ.Set(_json_toClient)

def Register(json_fromClient):
    newId = Rand.GetRandomCode(12)
    while database_Handler.GetUserId(newId)!=None:
        newId = Rand.GetRandomCode(12)

    database_Handler.InsertData(newId, json_fromClient["email"], json_fromClient["key"], "not verifed" ,str(datetime.date.today()))

    _json_toClient = {
        "type": "Register",
        "status": "Ok"
    }

    key = database_Handler.GetKey(newId)
    print("Key: %s" % str(key))

    #keyN = base64.urlsafe_b64decode(str(key))

    b = bytes(key, 'utf-8')
    print(str( b ))
    key = b.decode("utf-8")
    enc = server_crypto.FernetEncrypt( key.encode() , json.dumps(_json_toClient))
    
    CJ.Set(enc)
