import json
import time
import mandrakeService as mk
from InstagramAPI import InstagramAPI
ig = InstagramAPI("bikthorm", "1nfr4mund0")

ig.USER_AGENT='Mozilla/5.0 (Linux; Android 5.0.1; LG-H342 Build/LRX21Y; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 40.0.0.14.95 Android (21/5.0.1; 240dpi; 480x786; LGE/lge; LG-H342; c50ds; c50ds; pt_BR; 102221277)'
ig.login()
ig.getHashtagFeed("conciertoencasa")
response=ig.LastJson
for item in response['items']:
    # 1 = Photo, 8 = photos carrousel
    if item['media_type'] in (1,8)
## Recorrer hashtags como:
    #cuarentenamusical
    #conciertoencasa
    #cuarentenafest
    #liveconcert
def defoe(event, context):
    print(event)
    a="Desde la A"
    return {
        "statusCode":200,
        "body ":json.dumps({"message":a})
    }

    print(datetime.utcfromtimestamp(1586738855).strftime('%Y-%m-%d %H:%M:%S'))
FOLLOWER_COUNT=10000
MEDIA_TYPES=[1]
user_cache=defaultdict(list)

for item in items2:
    if item['media_type'] in MEDIA_TYPES:
        user_in_cache,user=getCachedUser(item['user']['pk'],user_cache,'user')
        if(not user_in_cache):
            _=ig.getUsernameInfo(item['user']['pk'])
            user=ig.LastJson['user']
            user_cache['user'].append(user)
            print("added ",user['username'])
        else:
            print("cached ",user['username'])
        if(user['follower_count']>FOLLOWER_COUNT):
            time.sleep(10)
            print(datetime.utcfromtimestamp(item['taken_at']).strftime('%Y-%m-%d %H:%M:%S')," ", item['image_versions2']['candidates'][0]['url']," ",user['follower_count'])

def getCachedUser(userId,dict,key):
    for user in dict[key]:
        if(userId == user['pk']):
            return True,user
    return False,''
