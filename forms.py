from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, email_validator, Length, Email
# from wtforms.widgets import TextArea
from models import *


class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    comment = SearchField('Comment', validators=[DataRequired()])


class RecMovieForm(FlaskForm):
    movie_name = StringField('Movie Name', validators=[DataRequired()])
    producer = StringField('Producer', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    your_point = IntegerField('Your Point', validators=[DataRequired()])
