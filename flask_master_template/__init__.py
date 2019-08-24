"""
Author: Jay
This is the python file that will:
    - Import Flask
    - Declare the instance of the app
    - Import the blueprints from the nexus folder
"""
from flask import Flask

app = Flask(__name__)

from flask_master_template.home.routes import home
from flask_master_template.index.routes import index

app.register_blueprint(home)
app.register_blueprint(index)