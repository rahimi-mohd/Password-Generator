from flask_wtf import FlaskForm
from wtforms import validators, SubmitField, StringField
from wtforms.validators import DataRequired

class PasswordGeneForm(FlaskForm):
    lowercase = StringField("Lowercase", validators=[DataRequired()], render_kw={'placeholder':'How many lowercase alphabet...'})
    uppercase = StringField("Uppercase", validators=[DataRequired()], render_kw={'placeholder':'How many uppercase alphabet...'})
    symbols = StringField("Symbols",validators=[DataRequired()], render_kw={'placeholder':'How many symbols...'})
    save_for = StringField("Save For", validators=[DataRequired()], render_kw={'placeholder':'Password for ?'})
    submit = SubmitField("Enter")