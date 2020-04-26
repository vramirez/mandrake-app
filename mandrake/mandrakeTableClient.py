import boto3
import uuid
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
TABLE_NAME="events"
table = dynamodb.Table(TABLE_NAME)
ARTIST_CATEGORY='ARTIST'

def getAllEvents():
    response = table.scan(
        TableName=TABLE_NAME
    )

    logging.info(response["Items"])

    # loop through the returned mysfits and add their attributes to a new dict
    # that matches the JSON response structure expected by the frontend.
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
        TableName=TABLE_NAME,
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

def putArtist(id,artist_name, photo_url):
    artist={}
    artist['pk_id']=id
    artist['sk_id']=ARTIST_CATEGORY
    artist['name']=artist_name
    artist['photo_url']=photo_url
    #artist=json.dumps(artist,ensure_ascii=False).encode('utf8')
    response = table.put_item(Item=artist)
    return response

def getArtist(id):
    ki={}
    ki['pk_id']=id
    ki['sk_id']=ARTIST_CATEGORY
    response=table.get_item(Key=ki)
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