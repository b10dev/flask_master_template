from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
def indexpage():
    return render_template('index/index.html')
