from flask import Blueprint, render_template, request, url_for


home = Blueprint('home',__name__)

@home.route('/home')
def homepage():
    return render_template('home/home.html')