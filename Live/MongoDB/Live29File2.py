import pymongo

client = pymongo.MongoClient("mongodb+srv://Jaymilv:Jimmy123@cluster0.wtvzm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['MyInfo']
collection = database["Jimmy"]
record = collection.find()
for i in record:
    print(i)

Query = collection.find({"companyName": "iNeuron"})
Query1 = collection.find({"courseOffered": {"$gt": "E"}})
for i in Query1:
    print(i)
