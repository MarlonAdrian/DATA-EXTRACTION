from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument
from pymongo.errors import ConnectionFailure
import sqlite3

connection_string = sqlite3.connect("database.db")
#Location csv
dfsql = pd.read_csv('C:/Users/USUARIO/Documents/Tiktok/nombre.csv', index_col=0)

dfsql.to_sql('olimpycs', connection_string)
dfsql
