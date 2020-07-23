import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
@app.route('/index.html')
def index():
    return render_template("index.html", movies=mongo.db.movies.find())


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


# ---- Help ---- #
@ app.route('/faq')
def faq():
    return render_template('faq.html')


# ---- ERRORS ----- #

@app.errorhandler(404)
def user_error(error):
    return render_template('errors/404.html'), 404


@app.route('/<path:path>')
def path_error(path):
    return render_template("errors/404.html"), 404


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")), debug=True)
