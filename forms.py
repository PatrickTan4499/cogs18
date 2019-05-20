from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    genre = StringField('genre', validators=[DataRequired()])
    submit = SubmitField('GET LIT')

