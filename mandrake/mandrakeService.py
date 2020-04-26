#from flask import Flask, jsonify, json, Response, request
import mandrakeTableClient
import uuid

# A very basic API created using Flask that has two possible routes for requests.

#app = Flask(__name__)
#CORS(app)

# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
#@app.route("/")
def healthCheckResponse():
    return jsonify({"message" : "Nothing here, used for health check. Try /mandrake instead."})

# Returns the data for all of the Mysfits to be displayed on
# the website.  If no filter query string is provided, all mysfits are retrived
# and returned. If a querystring filter is provided, only those mysfits are queried.
#@app.route("/mandrake")
def getAllEvents():

    '''filterCategory = request.args.get('filter')
    if filterCategory:
        filterValue = request.args.get('value')
        queryParam = {
            'filter': filterCategory,
            'value': filterValue
        }
        # a filter query string was found, query only for those mysfits.
        serviceResponse = mysfitsTableClient.queryMysfits(queryParam)
    else:'''
        # no filter was found, retrieve all mysfits.
    serviceResponse = mandrakeTableClient.getAllEvents()

    ##flaskResponse = Response(serviceResponse)
    ##flaskResponse.headers["Content-Type"] = "application/json"

    #return flaskResponse
    return serviceResponse

# Run the service on the local server it has been deployed to,
# listening on port 8080.
##if __name__ == "__main__":
    ##app.run(host="0.0.0.0", port=8080)

def putItem(item):
    mandrakeTableClient.putItem(item)

def getTodayNewer(tz):
    return mandrakeTableClient.getTodayAndNewerEvents(tz)

def getToday():
    return mandrakeTableClient.getTodayEvents()

def getUUID(name,prefix=''):
        lname=name.lower()
        lname=''.join(lname.split(' '))
        print(lname)
        name_id=uuid.uuid5(uuid.NAMESPACE_DNS,lname)
        return prefix+"_"+name_id.hex        

def getEventUUID(event):
        return getUUID(event,'event')

def getArtistUUID(event):
        return getUUID(event,'artist')

def saveArtist(name,photo):
    pk=getArtistUUID(name)
    return mandrakeTableClient.putArtist(pk,name,photo)

def getArtist(name):
    pk=getArtistUUID(name)
    return mandrakeTableClient.getArtist(pk)
    
#def saveEvent(name,artists,)