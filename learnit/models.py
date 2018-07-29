from datetime import datetime
from .__init__ import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    gender = db.Column(db.Enum('M', 'F'), default='M')
    bday = db.Column(db.DateTime)
    bio = db.Column(db.Text)
    premium = db.Column(db.Boolean, default=False)
    image_profile = db.Column(db.String(120), nullable=False, default='default.jpg')
    created_by = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User: {self.username}"