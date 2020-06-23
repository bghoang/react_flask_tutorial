from flask import Blueprint, jsonify, request
from . import db 
from .models import Movie

main = Blueprint('main', __name__)

# Define api call using Blueprint (don't have to use blueprint)
@main.route('/add_movie', methods=['POST'])
def add_movie():
    # Get data from request
    movie_data = request.get_json()

    # Assign data from request to the database
    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    # Add and commit request to the database
    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201

@main.route('/movies')
def movies():
    # Query all the movies in the database
    movie_list = Movie.query.all()
    movies = []

    # Save it to the movies array
    for movie in movie_list:
        movies.append({'title' : movie.title, 'rating' : movie.rating})

    return jsonify({'movies' : movies})