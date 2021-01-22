import os

class Config(object):
    DATABASE = os.getenv('DATABASE')
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')