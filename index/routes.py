from flask import Blueprint, render_template, request, url_for


index = Blueprint('index',__name__)

@index.route('/')
def homepage():
    return render_template('index/index.html')