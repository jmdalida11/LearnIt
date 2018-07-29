from flask import Blueprint, render_template, session, request
from ..models import User

pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    user = User.query.first()
    session['name'] = f"{user.firstname} {user.lastname}"
    session['email'] = f"{user.email}"
    return render_template('pages/home.html', user=user)

@pages.route('/register')
def register():
    return render_template('pages/register.html')