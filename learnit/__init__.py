from flask import Flask
from .config import Config

app = Flask(__name__)

app.config['SECRET_KEY'] = Config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = Config['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

