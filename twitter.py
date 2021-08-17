import couchdb
from tweepy import Stream
from tweepy import OAuthHandler #used to confirm authentication
from tweepy.streaming import StreamListener
import json

###################API-CREDENTIALS FROM TWITTER#########################
ckey = "put here"
csecret = "put here"
atoken = "put here"
asecret = "put here"
#######################################################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        


auth = OAuthHandler(ckey, csecret)   #toman los valores de las keys
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========CONNECTION TO COUCHDB=========='''
server = couchdb.Server('http://user:password@localhost:5984/')
try:
    db = server.create('name_data_base')
except:
    db = server['name_data_base'] 
    
'''===============LOCATIONS=============='''    
#https://boundingbox.klokantech.com/
twitterStream.filter(locations=[139.7580100399,35.6821407043,139.7609336478,35.6842496247]) #TOKIO
#twitterStream.filter(track=['olympics','Tokio']) #topics: olympics, tokio
