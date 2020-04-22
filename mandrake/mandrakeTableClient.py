import boto3
import json
import logging
from collections import defaultdict
from datetime import datetime,timedelta
import argparse
from boto3.dynamodb.conditions import Key, Attr
import pytz

# create a DynamoDB client using boto3. The boto3 library will automatically
# use the credentials associated with our ECS task role to communicate with
# DynamoDB, so no credentials need to be stored/managed at all by our code!
client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
TABLE_NAME="Mandrake"
table = dynamodb.Table(TABLE_NAME)

def getEventsJson(items):
    # loop through the returned mysfits and add their attributes to a new dict
    # that matches the JSON response structure expected by the frontend.
    mandrakeList = defaultdict(list)

    for item in items:
        mandrake = {}

        mandrake["artist"] = item["artist"]["S"]
        mandrake["date"] = item["date"]["S"]
        '''mandrake["link"] = item["link"]["S"]
        mandrake["description"] = item["Description"]["S"]
        mandrake["age"] = int(item["Age"]["N"])
        mandrake["goodevil"] = item["GoodEvil"]["S"]
        mandrake["lawchaos"] = item["LawChaos"]["S"]
        mandrake["thumbImageUri"] = item["ThumbImageUri"]["S"]
        mandrake["profileImageUri"] = item["ProfileImageUri"]["S"]
        mandrake["likes"] = item["Likes"]["N"]
        mandrake["adopted"] = item["Adopted"]["BOOL"]
        '''
        mandrakeList["events"].append(mandrake)
    print("a: ",type(mandrakeList))
    print("b: ",type(mandrakeList["events"]))
    return dict(mandrakeList["events"])

def getAllEvents():
    # Retrieve all Mysfits from DynamoDB using the DynamoDB scan operation.
    # Note: The scan API can be expensive in terms of latency when a DynamoDB
    # table contains a high number of records and filters are applied to the
    # operation that require a large amount of data to be scanned in the table
    # before a response is returned by DynamoDB. For high-volume tables that
    # receive many requests, it is common to store the result of frequent/common
    # scan operations in an in-memory cache. DynamoDB Accelerator (DAX) or
    # use of ElastiCache can provide these benefits. But, because out Mythical
    # Mysfits API is low traffic and the table is very small, the scan operation
    # will suit our needs for this workshop.
    response = table.scan(
        TableName='Mandrake'
    )

    logging.info(response["Items"])

    # loop through the returned mysfits and add their attributes to a new dict
    # that matches the JSON response structure expected by the frontend.
    #mandrakeList = getEventsJson(response["Items"])
    #print("c: ",type(mandrakeList))
    #type(response["Items"])
    return response["Items"]

'''def queryMysfitItems(filter, value):
    # Use the DynamoDB API Query to retrieve mysfits from the table that are
    # equal to the selected filter values.
    response = client.query(
        TableName='MysfitsTable',
        IndexName=filter+'Index',
        KeyConditions={
            filter: {
                'AttributeValueList': [
                    {
                        'S': value
                    }
                ],
                'ComparisonOperator': "EQ"
            }
        }
    )

    # loop through the returned mysfits and add their attributes to a new dict
    # that matches the JSON response structure expected by the frontend.
    mysfitList = getMysfitsJson(response["Items"])

    # convert the create list of dicts in to JSON
    return json.dumps(mysfitList)

def queryMysfits(queryParam):

    logging.info(json.dumps(queryParam))

    filter = queryParam['filter']
    value = queryParam['value']

    return queryMysfitItems(filter, value)
'''

def putItem(item):
    response = table.put_item(
        TableName='Mandrake',
            Item=item)

def getTodayAndNewerEvents(tz='UTC'):    
    tudei=datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d")
    fe = Key('date').gte(tudei) 
    response = table.scan(
        FilterExpression=fe
    )
    return response["Items"]

def getTodayEvents(tz='America/Bogota'):
    today=datetime.now(pytz.timezone(tz))
    begin=today.strftime("%Y-%m-%d")
    end=(today+timedelta(days=1)).strftime("%Y-%m-%d")
    fe = Key('date').gte(begin) & Key('date').lte(end)
    response = table.scan(
        FilterExpression=fe
    )
    return response["Items"]

def getDayEvents(deit,tz='America/Bogota'):
    today=datetime.strptime(deit, '%Y-%m-%d')
    begin=today.strftime("%Y-%m-%d")
    end=(today+timedelta(days=1)).strftime("%Y-%m-%d")
    fe = Key('date').gte(begin) & Key('date').lte(end)
    response = table.scan(
        FilterExpression=fe
    )
    return response
# So we can test from the command line
'''if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filter')
    parser.add_argument('-v', '--value')
    args = parser.parse_args()

    filter = args.filter
    value = args.value

    if args.filter and args.value:
        print 'filter is '+args.filter
        print 'value is '+args.value

        print "Getting filtered values"
        items = queryMysfitItems(args.filter, args.value)
    else:
    print("Getting all values")
    items = getAllEvents()

    print(items)
'''