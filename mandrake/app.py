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
    '''artist=event["artist"]
    date=event["date"]
    utc_time=event["utc_time"]
    '''
    type(event)
    type(json.dumps(event))
    print("INSERTIIIING...")
    mk.putItem(event)
    return event


def defoe(event, context):
    #print(event)
    
    return "ok"
