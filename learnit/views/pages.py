from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from ..models import User, db
from ..forms import RegistrationForm, LoginForm
from datetime import date
import hashlib
from flask_login import login_user, logout_user, current_user, login_required 

pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    return render_template('pages/home.html', user=current_user)

@pages.route('/register', methods=['POST', 'GET'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('pages.activities'))

    form = RegistrationForm()
    if form.validate_on_submit():

        hash_password = hashlib.sha1(request.form['password'].encode()).hexdigest()
        bday = date(int(request.form['byear']), int(request.form['bmonth']), int(request.form['bday']))

        user = User(firstname=request.form['firstname'], lastname=request.form['lastname'],
            email=request.form['email'], password=hash_password, bday=bday, gender=request.form['gender'])

        db.session.add(user)
        db.session.commit()

        flash('Account successfully created!', 'register_success')
        return redirect(url_for('pages.register'))
    return render_template('pages/register.html', form=form)

@pages.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('pages.activities'))

    if request.method == 'POST':
        hash_password = hashlib.sha1(request.form['password'].encode()).hexdigest()
        user = User.query.filter_by(email=request.form['email'],
            password=hash_password).first()

        if user is None:
            flash('Email or Password is invalid' , 'log_failed')
            return redirect(url_for('pages.login'))
        else:
            login_user(user)
            return redirect(url_for('pages.activities'))

    form = LoginForm()
    return render_template('pages/login.html', form=form)

@pages.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('pages.login'))

@pages.route('/activities')
@login_required
def activities():
    return render_template('pages/activities.html')

@pages.route('/profile')
@login_required
def profile():
    return render_template('pages/profile.html') 



