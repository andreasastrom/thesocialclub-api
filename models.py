import datetime
from app import db
from sqlalchemy.dialects.postgresql import JSON

'''class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
'''
class Application(db.Model):
    __tablename__ = 'application'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    createdtime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    deletedtime = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name


class User(db.Model): 
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    application = db.Column(db.Integer, db.ForeignKey("application.id"))
    