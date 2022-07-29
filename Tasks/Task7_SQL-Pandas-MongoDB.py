#Q4.: Convert attribute dataset in json format
import pandas as pd
df = pd.read_csv(r'C:\Users\Jaymil\PycharmProjects\MyWork\Live\Pandas\data fsds\Attribute DataSet CSV.csv')
df.to_json('AttributeDatasetToJson.json')
Attributedata = df.to_dict(orient="records")


#Q5.: Store this dataset into mongodb
import pymongo
client = pymongo.MongoClient("mongodb+srv://Jaymilv:Jimmy123@cluster0.wtvzm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['JaymilTask7']
collection = database["AttributeDataset"]
collection = database["DressSales"]
collection.insert_many(Attributedata)