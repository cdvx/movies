"""Module for app factory"""

# System libraries
import os

# Third-party libraries
from flask import Flask, jsonify

# Local imports
from config import app_config
from app import movies
from app.utils import MSG, Helper

# get function reference
create_message = Helper().create_message


def create_app(env_config=None):
    """Instantiate and return flask app"""

    app = Flask(__name__)
    
    # configure app object
    app.config.from_object(app_config.get(env_config\
        or os.getenv('FLASK_ENV')))

    # handle unknown url errors
    @app.errorhandler(404)
    def url_unknown(e):
        return jsonify(
            create_message(MSG['url_unknown'], error=True)
        ), 404

    # handle Internal Server Errors
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify(
            create_message(MSG['internal_server_error'], error=True)
        ), 500

    # handle unauthorized method errors
    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify(
            create_message(MSG['unsupported_action'], error=True)
        ), 405

    # register movies app
    app.register_blueprint(movies)

    return app