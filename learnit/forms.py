from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email
from datetime import datetime
import calendar

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname',
        validators=[DataRequired(), Length(min=2, max=80)])
    lastname = StringField('Lastname',
        validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email',
        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
        validators=[DataRequired(), Length(min=8, max=20)])
    bmonth = SelectField('Month', validators=[DataRequired()], choices=[(str(i+1), calendar.month_name[i+1]) for i in range(12)])
    bday = SelectField('Day', validators=[DataRequired()], choices=[(str(i+1),i+1) for i in range(31)])
    byear = SelectField('Year', validators=[DataRequired()], choices=[(str(i),i) for i in range(datetime.now().year, 1900, -1)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
        validators=[DataRequired()])
    submit = SubmitField('Login')
