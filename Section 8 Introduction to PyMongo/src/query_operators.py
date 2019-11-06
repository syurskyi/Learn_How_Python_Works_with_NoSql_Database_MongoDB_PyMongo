import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.tt
connect = db.example

post = [{"name": "mary", "created_at": datetime.datetime(2009, 11, 12, 18, 30), "score": 8},
        {"name": "sam", "created_at": datetime.datetime(2008, 11, 12, 18, 30), "score": 3},
        {"name": "joe", "created_at": datetime.datetime(2018, 11, 11, 18, 30), "score": 4},
        {"name": "john", "created_at": datetime.datetime(2011, 11, 12, 8, 10), "score": 2},
        {"name": "maya", "created_at": datetime.datetime(2010, 10, 12, 18, 30), "score": 1},
        {"name": "sameer", "created_at": datetime.datetime(2008, 10, 12, 18, 30), "score": 99}]

result = connect.insert(post)

print(list(connect.find()))
print()

# $lt example
cur = connect.find({"score": {"$lt": 12}})
cur.next()
for one in cur:
    print(one)
print()

# $gte and $lte example
cur2 = connect.find({"score": {"$gte": 2, "$lt": 9}})
for two in cur2:
    print(two)
print()

# $in example
print(list(connect.find({"score": {"$in": [5, 15]}})))

# or
 
# cur3 = connect.find({"score" : {"$in" : [5,15]}})
# for three in cur3:
#    print(three)
print()

# $ne example
cur4 = connect.find({"score": {"$ne": 99}})
for four in cur4:
    print(four)
print()

# $nin example
cur5 = connect.find({"score": {"$ne": 99}})
for five in cur5:
    print(five)
print()

# $or operator example
cur6 = connect.find({"$or": [{"score": 5}, {"score": 99}]})
for six in cur6:
    print(six)
print()

# $exists example
cur1 = connect.find({"name": {"$exists": True}}).count()
print(cur1)

print()
