from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_required 

activities = Blueprint('activities', __name__)

@activities.route('/quiz')
@login_required
def quiz():
    return render_template('activities/quiz.html')