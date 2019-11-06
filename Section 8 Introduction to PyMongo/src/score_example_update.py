import pymongo
from pymongo import MongoClient
from datetime import datetime

# connect to host and server
client = MongoClient('localhost', 27017)
# connect to database myFirstE
db = client.myFirstE
# connect to collection 
stud1 = db.studs

user_doc = [{
    "username": "john",
    "dateofBirth": datetime(1947, 4, 12),
    "score": 0},
            {"username": "jibin",
    "dateofBirth": datetime(1997, 5, 10),
    "email": "jibin@example.com",
    "score": 0}]

result = stud1.insert(user_doc)

print(list(stud1.find()))

print()
print()

stud1.update({"score": 0}, {"$set": {"flagged": True}}, safe=True)

# when we pass the multi : true option, it updates all the documents matched the query

# stud1.update({"score":0}, {"$set" : {"flagged" : True}}, multi= True, safe = True)
