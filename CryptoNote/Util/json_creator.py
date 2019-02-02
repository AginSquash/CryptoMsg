import json
import base64
#import asn1tools TODO Del


def Create(header, data):

    print("Creator len in header: %s" % len(header))
    print("Creator len in base64.b64encode (header): %s" % len(base64.b64encode (header)))


    _json = {
        "header": base64.b64encode (header).decode() ,
        "data"  : str( data   )
    }
    return json.dumps(_json).encode()  #json.dumps(