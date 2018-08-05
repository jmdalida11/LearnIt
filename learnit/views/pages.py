from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from ..models import User, db
from ..forms import RegistrationForm, LoginForm
from datetime import date
import hashlib
from flask_login import login_user, logout_user, current_user, login_required 
import secrets
import os
from ..__init__ import app

pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    return render_template('pages/home.html')

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

    custom_activities = current_user.activities
    print(custom_activities)
    return render_template('pages/activities.html', custom_activities=custom_activities)

@pages.route('/profile')
@login_required
def profile():
    return render_template('pages/profile.html') 

@pages.route('/updateAvatarBio', methods=['POST'])
@login_required
def updateAvatarBio():
    data = {}
    current_user.bio = request.form['bio']
    if request.form['toUploadAvatar'] == 'True':
        image_file = save_avatar(request.files['avatar'])
        try:
            if current_user.avatar != "default.png":
                os.remove(os.path.join(app.root_path, 'static/avatar', current_user.avatar))
        except:
            print("Image not found")
        current_user.avatar = image_file
        data['status'] = 'success_avatar'
        data['avatar'] = 'static/avatar/' + image_file
    else:
        data['status'] = 'success'
    db.session.commit()
    return jsonify(data)

def save_avatar(img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(img.filename)
    image_name = random_hex + f_ext
    img.save(os.path.join(app.root_path, 'static/avatar', image_name))
    return image_name
