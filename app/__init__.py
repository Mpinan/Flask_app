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

from app import models


app = Flask(__name__)

load_dotenv()
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')


CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@localhost/%s' % ( DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE )




# PostgreSQL Database credentials loaded from the .env file


db = SQLAlchemy(app)
