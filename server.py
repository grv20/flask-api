from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#app
app = Flask(__name__)
#The flask object implements a WSGI app and acts as the central
#object. It is passed the name of the module or package of the app.
#Once it is created it will act as a central registry for the
#view functions, the URL Rules, template config & much more.

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
#SQLAlchemy is python SQL toolkit & Object Relational Mapper(ORM)
#that gives app developers the full power & flexibility of SQL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0
#config dict behaves like a regular dict, but supports additional 
#methods to load a config from files.

#configure slite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()
#we needed to import from sqlalchemy to implement this foreign
#key function, other than this we will use flask_sqlalchemy

db = SQLAlchemy(app)
#This class is used to control the SQLAlchemy integration to one
#or more Flask Apps i.e. connecting ORM with flask app
now = datetime.now()

#models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")

class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

#routes
@app.route("/user", methods=["POST"])
def create_user():
    pass
#A decorator that is used to register a view function for a given URL Rule. 

@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    pass

@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    pass

@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
    pass
    
@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    pass

@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    pass

@app.route("/user/<user_id>", methods=["GET"])
def get_all_blog_posts(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["DELETE"])
def delete_blog_post(blog_post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)
#if we are this file server.py as our main application
#then we are going to start our api with debug=True
#i.e. if we are running like python server.py --> then it will
#set __name__ to __main__ (bcoz server.py is main file in that case)