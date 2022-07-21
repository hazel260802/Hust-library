from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError
from .models import Sach
from markupsafe import Markup
class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired(), Length(max=100)])
    search_icon = Markup ("<i class=\"fa fa-search\"></i>")
    search_button = SubmitField(search_icon, id="symbolBtn")