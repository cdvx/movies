"""Module to run app"""

# create_app
from application import create_app

# create app object
app = create_app()

if __name__=='__main__':
    app.run(port=5000)