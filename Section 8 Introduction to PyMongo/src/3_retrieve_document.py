import pymongo
from pymongo import MongoClient

# connect to host and server
client = MongoClient('localhost', 27017)
# connect to database myFirstE
db = client.myFirstE
# connect to collection 
stud1 = db.stud

# print'connection made successfully'

# inserting a document

# post = {"author" : "mike", "text" : "my first blog", "tags" : ["mongodb", "python", "pymongo"]}

# stud1.insert(post)

# print'inserted successfully'

results = stud1.find()

# it will retrive only 2 documents
for record in results[:2]:
    print("here are the documents:", record)
