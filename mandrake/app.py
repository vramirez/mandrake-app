import json
import mandrakeService as mk


def lambda_main(event, context):
    obj=mk.getAllEvents()     
    return obj

def write_event(event, context):
    mk.putItem(event)
    return event

def defoe(event, context):
    #print(event)
    
    return "ok"

def getTodayNewerEvents(event, context):
    obj=mk.getTodayNewer()
    return obj