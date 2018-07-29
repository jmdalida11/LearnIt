from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from ..models import User, db
from ..forms import RegistrationForm, LoginForm
from datetime import date
import hashlib

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

    if request.method == 'POST':

        hash_password = hashlib.sha1(request.form['password'].encode()).hexdigest()
        registered_user = User.query.filter_by(email=request.form['email'],
            password=hash_password).first()

        if registered_user is None:
            flash('Email or Password is invalid' , 'log_failed')
            return redirect(url_for('pages.login'))
        else:
            flash('successfully Login!' , 'log_failed')
            return redirect(url_for('pages.login'))

    form = LoginForm()
    return render_template('pages/login.html', form=form)



