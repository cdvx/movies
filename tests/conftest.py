"""Module for setting up testing fixtures"""

# Third-party libraries
import pytest
from flask import current_app, Response

# Local imports
from application import create_app
from app.db import MovieStore

# constants
from app.utils import BASE_URL

@pytest.yield_fixture(scope='session')
def app_():
    """
    Setup flask test app, this only gets executed once.

    Args:
        None
    Returns:
        Flask app
    """
    _app = create_app(env_config='testing')

    return _app

@pytest.fixture(scope='function')
def client(app_):
    """
    Setup an app client, this gets executed for each test function.

    Args:
        app_(obj): Pytest fixture
    Returns:
        Flask app client
    """
    yield app_.test_client()
