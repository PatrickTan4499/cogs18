from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SearchForm(FlaskForm):
    '''
    Form for user to input music genre and search for videos
    '''
    genre = StringField('Genre', validators=[DataRequired()])
    submit = SubmitField('GET LIT')


class RegistrationForm(FlaskForm):
    '''
    Form for user to register with my application
    
    External Code: External Code used from CoreyMSchafer 'Python Flask Tutorial'
    '''
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    '''
    Form for user to login to my application

    External Code: External Code used from CoreyMSchafer 'Python Flask Tutorial'
    '''
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
