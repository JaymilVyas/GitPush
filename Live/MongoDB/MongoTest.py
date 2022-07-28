import pymongo
client = pymongo.MongoClient("mongodb+srv://Jaymilv:Jimmy123@jaymilcluster.wtvzm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "Name":"Jimmy",
    "EmailID":"jaymilvyas@gmail.com",
    "Surname":"Vyas"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
