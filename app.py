from flask import Flask
from flask_pymongo import PyMongo

import json


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/Employees"


mongo = PyMongo(app)


db = mongo.db.details


with open('data.json') as file:

    file_data = json.load(file)


if isinstance(file_data, list):

    db.insert_many(file_data)

else:

    print("error loading file")
