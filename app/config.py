import os

class Config(object):
    # DATABASE = os.getenv('DATABASE')
    # DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    # DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_URL = "postgres://igcjukkymuicfq:3e1c8c7eb7753d59cd3f7362697ed5d018f49cf72b4c2640c287499ec0fa3612@ec2-52-70-135-246.compute-1.amazonaws.com:5432/dad3uilljjvvg"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
