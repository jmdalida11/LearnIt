from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .__init__ import app
from flask_login import LoginManager, UserMixin

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    gender = db.Column(db.Enum('M', 'F'), default='M')
    bday = db.Column(db.DateTime)
    bio = db.Column(db.Text)
    premium = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(120), nullable=False, default='default.png')
    created_by = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    activities = db.relationship('Activity', backref='user')
    quizzes = db.relationship('Quiz', backref='user')

    def __repr__(self):
        return f"User: {self.firstname} {self.lastname}"

login_manager = LoginManager()
login_manager.login_view = 'pages.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    about = db.Column(db.String(60), nullable=False)
    activity_type = db.Column(db.Enum('quiz', 'learn'), default='learn')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class PostIt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    content = db.Column(db.String(60), nullable=False)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(60), nullable=False)
    about = db.Column(db.Text)
    quiz_type = db.Column(db.Enum('learn', 'choices', 'enumeration'), default='learn')
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


