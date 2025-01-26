#Imports
from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


#App
app = Flask(__name__)







def index():
    return "test"