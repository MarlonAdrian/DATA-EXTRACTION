from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from facebook_scraper import get_posts
import couchdb
import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument
from pymongo.errors import ConnectionFailure


Client = MongoClient('mongodb://localhost:27017')

#Check connection to CouchDB
'''try:
    Client.admin.command('ismaster')
    print('MongoDB connection: Succes')
except ConnectionFailure as cf:
    print('MongoDB connection: Succes', cf)try:
    Client.admin.command('ismaster')
    print('MongoDB connection: Succes')
except ConnectionFailure as cf:
    print('MongoDB connection: Succes', cf)'''

db=Client['name_database']
Collection=db["name_collection_of_database"]

i=1
#https://https://www.facebook.com/olympics-> Take only "olympics"
for post in get_posts('olympics', pages=3, extra_info=True, credentials=('email_facebook', 'password_facebook')):
    print(i)
    i=i+1
    time.sleep(1)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']


    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']     
        
        
        dbFB=pd.DataFrame({"juegos_olimpicos":doc})
        dbFB.to_json('olympicos.json')
        
        with open('olympicos.json') as file:
            file_data = json.load(file)

        if isinstance(file_data, list):
            Collection.insert_many(file_data)
        else:
            Collection.insert_one(file_data)
            
        print("Saved Successfully")

    except Exception as e:
        print("Not Saved: " + str(e))
