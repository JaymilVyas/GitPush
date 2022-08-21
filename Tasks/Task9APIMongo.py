from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Jaymilv:Jimmy123@task9apimongo.jyviamr.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collection = database['taskcollection']

@app.route("/insertmongo", methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("Successfully Inserted"))

if __name__ == '__main__':
    app.run(port = 5001)
