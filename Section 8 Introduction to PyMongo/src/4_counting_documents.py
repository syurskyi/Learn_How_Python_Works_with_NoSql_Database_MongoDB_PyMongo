import pymongo
from pymongo import MongoClient

# connect to host and server
client = MongoClient('localhost', 27017)
# connect to database myFirstE
db = client.myFirstE
# connect to collection 
stud1 = db.stud

results = stud1.find().count()
print(results)