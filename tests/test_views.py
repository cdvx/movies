"""Module for testing views"""

# constants
from .conftest import BASE_URL


class TestMovieViews:
    """Test class for movies endpoints"""
    def test_get_movies(self, client):
        res = client.get(BASE_URL)
        assert res.status_code == 200
        assert b'movies' in res.data

    def test_get_movie_by_id(self, client):
        res = client.get(f'{BASE_URL}/23')
        assert res.status_code == 200
        assert b'movie' in res.data

    def test_search_movie_by_complete_name_genre(self, client):
        res = client.get(f'{BASE_URL}?name=fail-safe')
        res2 = client.get(f'{BASE_URL}?genre=drama')
        assert res.status_code == 200
        assert b'results' in res.data
        assert res2.status_code == 200
        assert b'results' in res2.data

    def test_search_movie_by_incomplete_name_genre(self, client):
        res = client.get(f'{BASE_URL}?name=fa')
        res2 = client.get(f'{BASE_URL}?genre=dr')
        assert res.status_code == 200
        assert b'results' in res.data
        assert res2.status_code == 200
        assert b'results' in res2.data

    def test_search_movie_by_both_genre_name(self, client):
        res = client.get(f'{BASE_URL}?name=fa&genre=dr')
        assert res.status_code == 200
        assert b'results' in res.data

    def test_search_non_existent(self, client):
        res = client.get(f'{BASE_URL}?name=xxr')
        assert res.status_code == 404
        assert b'message' in res.data

    def test_search_with_missing_json(self, client):
        res = client.get(f'{BASE_URL}?bb=k')
        assert res.status_code == 400
        assert b'message' in res.data

    def test_search_with_non_int(self, client):
        res = client.get(f'{BASE_URL}/2k')
        assert res.status_code == 404
        assert b'error' in res.data

