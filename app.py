import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# creates instance of Flash
app = Flask(__name__)

app.config["MONGODB_NAME"] = 'foodie'
app.config["MONGODB_URI"] = 'mongodb+srv://root:<password>@firstcluster.gtfgd.mongodb.net/<foodie>?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

def hello():
    return ('Hello World ...again')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
