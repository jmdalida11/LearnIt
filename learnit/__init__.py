from flask import Flask
from .views.pages import pages

app = Flask(__name__)

app.register_blueprint(pages)

