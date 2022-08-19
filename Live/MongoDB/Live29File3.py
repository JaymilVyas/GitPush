import pymongo
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

client = pymongo.MongoClient("mongodb+srv://Jaymilv:Jimmy123@cluster0.wtvzm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]
collection.insert_many(data)
#d = collection.find()
#for i in d:
#    print(i)

#d1 = collection.find({'status': 'A'})
#for i in d1:
#    print(i)

#d2 = collection.find({'status': {'$in': ['A', 'P']}})
#for i in d2:
#    print(i)

#d3 = collection.find({'qty': {'$gt': 50}})
#for i in d3:
#    print(i)

# d4 = collection.find({'qty': {'$gte': 100}})
# for i in d4:
#    print(i)

#d5 = collection.find({'item': 'sketch pad', 'qty': 95})
#for i in d5:
#    print(i)

#d6 = collection.find({'item': 'sketch pad', 'qty': {"$gte": 75}})
#for i in d6:
#    print(i)

#d7 = collection.find({'$or': [{'item': 'sketch pad'}, {'qty': {"$gte": 75}}]})
#for i in d7:
#    print(i)

#collection.update_one({'item': 'canvas'}, {'$set': {'item': 'Jimmy'}})
#d8 = collection.find({'item': 'Jimmy'})
#for i in d8:
#    print(i)

collection.delete_one({'item': 'Jimmy'})
d9 = collection.find({'item': 'Jimmy'})
for i in d9:
    print(i)
