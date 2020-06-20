import os
from flask import Flask
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
    import env

# Define the app, and set the MONGO_URI secret key
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello World ... this is a new app'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
