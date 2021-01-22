from flask import Flask
from flask import jsonify

from app.models.movies_model import Films
from app import app

import os


@app.route('/')

@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Films.get_all_films()

    return jsonify([*map(films_serializer, movies)])