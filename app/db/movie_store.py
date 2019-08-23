"""Module for MovieStore"""

# System libraries
import json, os

# constants
from app.utils import MOCK_DATA_PATH

class MovieStore:
    """Class to store and manage movie data"""

    def __init__(self):
        # open json file with movie data and load it into 
        # a list
        with open(os.getenv(MOCK_DATA_PATH)) as file:
            data = json.load(file)
        # close file
        file.close()
        self.data = data

    def get_by_single_key(self, key: str, where: str):
        """
        Get movies by a single key [name or genre]

        Args:
            key(str): complete or incomplete key to search for movie
            where(str): feild from which to pick the key [name or genre]
        Returns:
            list: results list of movie(s) results else None
        """
        # get movies that match the key
        results = [mov for mov in self.data if self.check_for_key(key, mov, where)]
        return results if results else None

    def check_for_key(self, key: str, mov: dict, where: str):
        """
        Check that movie with key exists

        Args:
            key(str): complete or incomplete key to search for movie
            mov(dict): movie dictionary
            where(str): feild from which to check key from [name or genre]
        Returns:
            bool: True if movie with key exists else False
        """
        # get complete key from incomplete key
        key = self.check_incomplete_key(key, mov, where)
        return (mov[where] == key) if key else False

    def check_incomplete_key(self, key: str, mov: dict, where: str):
        """
        Check that key is complete or try to get complete version of it

        Args:
            key(str): complete or incomplete key to search for movie
            mov(dict): movie dictionary
            where(str): feild from which to check key from [name or genre]
        Returns:
            NoneType: complete key if key exists else None
        """
        return mov[where] if mov[where].lower().find(key) != -1 else None

    def get_by_both_keys(self, *args):
        """
        Get movie given both keys

        Args:
            name(str): name of movie
            genre(str): genre to which movie belongs
        Returns:
            list: list of movie(s) else None
        """
        name, genre = args
        # since names are not sorted
        results = [mov for mov in self.data if self.check_for_key(name, mov, 'name')\
            or self.check_for_key(genre, mov, 'genre')]
        return results if results else None
