from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = Config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = Config['DATABASE_URI']

db = SQLAlchemy(app)
