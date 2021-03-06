#from flask import Flask, jsonify, json, Response, request
import mandrakeTableClient


# A very basic API created using Flask that has two possible routes for requests.

#app = Flask(__name__)
#CORS(app)

# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
#@app.route("/")
def healthCheckResponse():
    return "Nothing here, used for health check. Try /mandrake instead."

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

def getTodayNewer():
    return mandrakeTableClient.getTodayAndNewerEvents()