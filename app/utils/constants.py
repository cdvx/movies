"""Module to hold constants"""

MSG = {
    'no_movie_id':'Please provide a movie id!',
    'movie_not_found': 'Movie not found!',
    'missing_json': 'Missing JSON in request!',
    'no_name_genre':'Please provide either of name or genre to search for movies!',
    'url_unknown': 'Sorry, resource you are looking for does not exist',
    'internal_server_error': 'Sorry,we are experiencing some technical difficulties\
        \nPlease report this to cedriclusiba@gmail.com and check back with us soon',
    'unsupported_action': 'Sorry, this action is not supported for this url'
}

BASE_URL = '/api/v1/movies'
MOCK_DATA_PATH = 'MOCK_DATA_PATH'
