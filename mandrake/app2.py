import json
import mandrakeService as mk

def defoe(event, context):
    print(event)
    a="Desde la A"
    return {
        "statusCode":200,
        "body ":json.dumps({"message":a})
    }