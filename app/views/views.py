"""Module for movies app"""

# Third-party libraries
from flask import Blueprint, jsonify, request
from memory_profiler import profile

# Local imports
from app.db import MovieStore
from app.utils import MSG, Helper, BASE_URL

# movies blueprint
movies = Blueprint('movies', __name__)

# instantiate store
store = MovieStore()

# instantiate Helper class and get methods
helper = Helper()


@movies.route(f'{BASE_URL}/<int:movie_id>', methods=['GET'])
@profile
def get_movie(movie_id=None):
    """
    Get movie by id

    Args:
        movie_id(str): string integer id of movie to get
    Returns:
        Response: movie matching id
    """
    movie = [movie for movie in store.data if movie['id'] == int(movie_id)]
    msg = helper.create_message(MSG['movie_not_found'])

    return (jsonify(movie=movie[0]), 200) if movie else (jsonify(msg), 404)


@movies.route(BASE_URL, methods=['GET'])
@profile
def search_or_get_movies(name=None, genre=None):
    """
    1. Search for movie by name, genre or both
    the name or genre could be incomplete and
    the search will still work accordingly ['POST']

    2. Get all movies ['GET']

    Args:
        name(str): name of movie to search for
        genre(str): genre in which to search
    Returns:
        Response: all movies['GET'] or movies matching
        the passed name or genre ['POST']
    """
    # return all movies if it is
    # if no request args are passed
    if not request.args:
        return jsonify(movies=store.data), 200

    # validate request args
    data = helper.valid_request_data(request)

    # return appropriate response depending on results passed
    return_results = lambda results: (jsonify(results=results), 200) if results\
        else (jsonify(helper.create_message(MSG['movie_not_found'])), 404)

    # if data is str then something went wrong
    # and data is the message showing why
    if isinstance(data, str):
        return jsonify(helper.create_message(data)), 400

    name, genre = data.get('name'), data.get('genre')

    name_and_genre = name and genre
    name_or_genre = name or genre

    # get results data
    results = helper.handle_results(
        name_and_genre, name_or_genre,
        name, genre,
        store)

    return return_results(results)

    










    
    
