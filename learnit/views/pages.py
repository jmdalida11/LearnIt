from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from ..models import User
from ..forms import RegistrationForm, LoginForm

pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    user = 'jm'
    session['name'] = 'jm'
    session['email'] = 'jm'
    return render_template('pages/home.html', user=user)

@pages.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account successfully created!', 'register_success')
        return redirect(url_for('pages.register'))
    return render_template('pages/register.html', form=form)


@pages.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('pages/login.html', form=form)