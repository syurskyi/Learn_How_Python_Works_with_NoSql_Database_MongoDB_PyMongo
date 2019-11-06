import pymongo
from datetime import datetime
from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
db = client.test
conn = db.userss

user_doc = {"username": "janedoe",
            "firstname": "Jane",
            "surname": "Doe",
            "dateofBirth": datetime(1989, 4, 12),
            "email": "janedoe@example.com",
            "score": 0
            }

result = conn.insert(user_doc)

for record in conn.find():
    print(record)
# print list(conn.find())

# set operator example
conn.update({"username": "janedoe"}, {"$set": {"email": "doejane72@example.com"}}, safe=True)

for record1 in conn.find():
    print(record1)

print()

# $inc operator
conn.update({"username": "janedoe"}, {"$inc": {"score": 5}})

# $unset total posts
conn.update({"username": "janedoe"}, {"$unset": {"score": " "}})

# $rename operator
conn.update({"username": "janedoe"}, {"$rename": {"firstname": "NAME"}})

# exists example in update modifiers
cur1 = conn.find({"username": {"$exists": True}}).count()
print(cur1)

# $push operator

conn.update({"username": "janedoe"}, {"$push": {"sentiment": {"nb":
                            random.randint(-5, 5), "svm" : random.randint(-5, 5)}}})


# pop operator

conn.update({"username": "janedoe"}, {"$pop": {"sentiment": 1}})

# pull operator example

conn.update({"username": "janedoe"}, {"$set":
                        {"skills": ["python", "pymongo", "mongoDB", "R"]}})


conn.update({"username": "janedoe"}, {"$pull": {"skills": "R"}})
