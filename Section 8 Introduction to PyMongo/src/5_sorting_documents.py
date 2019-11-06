import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.tt
connect = db.example

# sorting in ascending order
print(list(connect.find().sort('name')))

# sorting in descending order
print(list(connect.find().sort('name', -1)))
