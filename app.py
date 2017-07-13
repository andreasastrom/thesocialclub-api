import os
import requests
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
#print(os.environ['APP_SETTINGS'])

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import application
from models import *

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        signup = request.get_json()
        if signup is not None and signup != '':
            newApp = application.MyApplication()
            response = newApp.CreateApplication(signup)
            if response:
                return "Signup"
            else:
                abort(400)

if __name__ == '__main__':
    app.run()
