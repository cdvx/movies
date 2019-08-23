"""Module for helper functions"""

# constants
from .constants import MSG


class Helper:
    """Class to hold helper functions/methods"""

    def create_message(self, message, error=None):
        """
        Handles creation of response message objects

        Args:
            message(str): message to comprise message/error dict
            error(bool): make error message dict if True

        Returns:
            dict: dict object with message passed
        
        """
        return {'error': message} if error else {'message': message}

    def valid_request_data(self, request):
        """
        Validates request args

        Args:
            request(obj): message to comprise message/error dict

        Returns:
            str: message to be return to user in case
                 something goes wrong
            dict: data from request object
        """
        data = request.args
        absent = 'name' not in data and 'genre' not in data
        return MSG['no_name_genre'] if absent else data

    def handle_results(self, *args):
        """
        Handles search and returns results

        Args:
            name_and_genre(bool): True if both name and genre values
                                are not None
            name_or_genre(bool): True if either if genre and name
                                values is not None
            func(function obj): function to return approriate resulsts
                                response
            name(str): name of movie to search for
            genre(str): genre of movie to search for
            store(obj): MovieStore instance

        Returns:
            list: list of results
        """
        name_and_genre, name_or_genre, name, genre, store = args
        # in case only one feild was passed
        if not name_and_genre and name_or_genre:
            results = store.get_by_single_key(name.lower(), 'name')\
                if name else store.get_by_single_key(genre.lower(), 'genre')
            return results

        # in case both feilds were passed
        elif name_and_genre:
            results =  store.get_by_both_keys(name, genre)
            return results