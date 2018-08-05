from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_required 
from random import shuffle

activities = Blueprint('activities', __name__)

@activities.route('/quiz')
@login_required
def quiz():

    quiz = {
        "type" : "choices",
        "contents" : [
            {
                "question" : "What is the answer of 4+4=?",
                "answer" : 0,
                "choices" : ['8', '4', '6', '3'],
                "id" : "fjklasj"
            },
            {
                "question" : "What is Computer CPU?",
                "answer" : 0,
                "choices" : ['Central Processing Unit', 'Computer Process Unit', 'Central Processing Unified', 'Computer Process Unified'],
                "id" : "fjalkdfjl"
            }
        ]
    }

    shuffle(quiz['contents'])

    return render_template('activities/quiz.html', quiz=quiz)
