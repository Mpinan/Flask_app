from flask import Flask
from flask import jsonify, request

from app.models.movies_model import Films
from app import app

import os


@app.route('/')

@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/movies', methods=['GET'])
def get_all_movies():
    all_movies = Films.get_all_films()
    return jsonify(
        movies = [movie.films_serializer for movie in all_movies]
        )

@app.route("/submit_film", methods=["POST"])
def submit_film():
    incoming = request.get_json()

    print(incoming, "hello incoming")
    success, id = Films.save(Films(
        incoming["film_name"],
        incoming["img_url"],
        incoming["release_year"],
        incoming["summary"],
        incoming["director"],
        incoming["genre"],
        incoming["rating"],
        incoming["film_runtime"],
        incoming["meta_score"]
        ))

    if not success:
        return jsonify(message="Error submitting task", id=None), 409

    return jsonify(success=True, id=id)

# @app.route("/api/delete_task", methods=["POST"])
# @requires_auth
# def delete_task():
#     incoming = request.get_json()

#     success = Task.delete_task(incoming.get('task_id'))
#     if not success:
#         return jsonify(message="Error deleting task"), 409

#     return jsonify(success=True)


# @app.route("/api/edit_task", methods=["POST"])
# @requires_auth
# def edit_task():
#     incoming = request.get_json()
   
#     success = Task.edit_task(
#         incoming.get('task_id'),
#         incoming.get('task'),
#         incoming.get('status')
#     )
#     if not success:
#         return jsonify(message="Error editing task"), 409

#     return jsonify(success=True)