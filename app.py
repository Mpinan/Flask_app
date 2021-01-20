from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
# ORM
from flask_sqlalchemy import SQLAlchemy
# Psql adapter
import psycopg2
# Python OS module provides easy functions that allow us to interact and get Operating System information and even control processes up to a limit, 
# irrespective of it being a Windows Platform, Macintosh or Linux.
import os


load_dotenv()
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@localhost/%s' % ( DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE )

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username



# PostgreSQL Database credentials loaded from the .env file


@app.route('/')
def index():
    return "Hello"

