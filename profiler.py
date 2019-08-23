"""Module for profiling api"""

# Third-party libraries
from werkzeug.contrib.profiler import ProfilerMiddleware

# Local imports
from application import create_app

# create app object and set up profiling middleware
app = create_app('testings')
app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])


if __name__ == '__main__':
    app.run(debug = True)