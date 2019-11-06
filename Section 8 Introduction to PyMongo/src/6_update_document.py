import pymongo
from pymongo import MongoClient

# connect to host and server
client = MongoClient('localhost', 27017)
# connect to database myFirstE
db = client.myFirstE
# connect to collection 
stud1 = db.stud

print('connection made successfully')

# inserting a document

post = {"author": "mike", "text": "my first blog", "tags": ["mongodb", "python", "pymongo"]}

stud1.insert(post)

print('inserted successfully')


print('earlier, we had these documents')
for record in stud1.find():
    print(record)

print()
print('+=+=+=+=+=+=+=+')
print()
stud1.find_one({"author": "mike"})

stud1.update({"author": "mike"}, {"$set": {"text": "hello world"}})

print('but now the updated document is ')
for student in stud1.find():
    print(student)
