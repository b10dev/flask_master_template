"""
Author: Jay
This is the python file that will:
    - Import Flask
    - Declare the instance of the app
    - Import the blueprints from the nexus folder
"""
from flask import Flask

app = Flask(__name__)

from nexus.home.routes import home

app.register_blueprint(home)