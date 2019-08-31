"""
Author: Jay
This is the python file that will:
    - Import Flask
    - Declare the instance of the app
    - Import the blueprints from the nexus folder
"""
from flask import Flask

app = Flask(__name__)

'''
import secrets
secrets.token_hex(16)
'77cb97cd58c33327c245c87a4a8babcb'
'''

app.config['SECRET_KEY'] = '77cb97cd58c33327c245c87a4a8babcb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from flask_master_template.home.routes import home
from flask_master_template.login.routes import login
from flask_master_template.index.routes import index
from flask_master_template.forms_example.routes import forms_example

app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(index)
app.register_blueprint(forms_example)
