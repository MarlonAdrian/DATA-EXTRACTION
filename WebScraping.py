import requests #peticion a las paginas 
from bs4 import BeautifulSoup #extrae la info

"----------------------------------------GUARDAR EL CSV A MONGODB-----------------------------------------------"
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument


"----------------------------------------CONEXION A MONGODB-----------------------------------------------"
from pymongo import MongoClient
myClient = MongoClient ('mongodb://localhost:27017/')
try:
    myClient.admin.command('ismaster')
    print('MongoDB connection: Succes')
except ConnectionFailure as cf:
    print('MongoDB connection: Succes', cf)


    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
 
response = requests.get('https://www.elcomercio.com/tag/columnistas/') #pagina web
soup = BeautifulSoup(response.content, "lxml") #manipular la info, es recomendable utilizar el formato lxml

#Arrays to save data
Author=[]
Fecha=[]
Titulo=[]
Lectura=[]

#web page tags
post_author= soup.find_all("p", class_="list-item__author") 
post_fecha=soup.find_all("time", class_="list-item__date text-primary")
post_lectura= soup.find_all("p", class_="list-item__excerpt") 
post_titulo= soup.find_all("h3", class_="list-item__title")
extracted = []

#Searching in web page 
for element in post_author: 
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Author.append(limpio.strip())

for element in post_fecha:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Fecha.append(limpio.strip())
    
for element in post_titulo:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, 'https')+1:find_2nd(element,'<')])
    #print (limpio)
    Titulo.append(limpio.strip())
    

for element in post_lectura:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Lectura.append(limpio.strip())



#Save on Dataframe with pandas
archivo = pd.DataFrame({'Author':Author,'Date':Fecha,'Read':Lectura,})
archivo.to_json('comercio.json')

#Creating new database and collection
db = myClient["name_database"]
Collection= db["name_collection_of_database"]

#Save database as file and send  it to MongoDB
with open('comercio.json') as file:
    file_data = json.load(file)

    
if isinstance (file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)

archivo
