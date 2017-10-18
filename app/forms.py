from flask_wtf import Form
from wtforms import StringField, BooleanField 
from wtforms.validators import DataRequired

class searchForm(Form):
    query = StringField('query', validators=[DataRequired()])