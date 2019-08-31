from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_master_template import app

db = SQLAlchemy(app)


class Users(db.Model):
    username = db.Column(db.String(), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"""Users(Username :{self.username}
        Password : {self.password}
        )"""


class FExample(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    string = db.Column(db.String(), unique=False, nullable=False)
    password = db.Column(db.String(), nullable=True)
    floats = db.Column(db.Float(), nullable=True)
    booleans = db.Column(db.Boolean(), nullable=True)
    selects = db.Column(db.String, nullable=True)
    files = db.Column(db.LargeBinary(), nullable=True)
    dates = db.Column(db.Date(), nullable=True)


def createall():
    db.create_all()


def commit():
    db.session.commit()


def addit(x):
    db.session.add(x)
