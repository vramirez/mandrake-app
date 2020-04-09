import json
import mandrakeService as mk


def lambda_main(event, context):
    obj=mk.getAllEvents() 
    print("loaaaaading2...")
    print(obj)
    print(type(obj))
    print(json.dumps(obj))
    print(type(json.dumps(obj)))
    
    return obj
        
    


def write_event(event, context):
    #obj=mk.getAllEvents() 
    print("INSERTIIIING...")
    mk.put    
    return {
        "statusCode": 200,
        "body": json.dumps({"message":"inserted"})
        
        #json.dumps({
        # "location": ip.text.replace("\n", "")
        #}),
    }

def defoe(event, context):
    #print(event)
    
    return {
        "statusCode":200,
        "body":json.dumps({"message":"Todo en orden por aca"})
    }
