import json

def Create(header, data):
    _json = {
        "header": str( header ) ,
        "data"  : str( data   )
    }
    return json.dumps(_json).encode()