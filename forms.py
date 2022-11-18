
from wtforms.validators import InputRequired, Email, Optional
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect, CSRFError
# from wtforms import DateField, StringField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, URL, AnyOf
from wtforms import FloatField, StringField, SelectField, IntegerField, BooleanField, TextAreaField


class AddNewPet(FlaskForm):
    # name = 'Jason'
    name = StringField('Name', validators=[DataRequired()])
    species = StringField('Species', validators=[AnyOf(
        ['dog', 'Dog', 'cat', 'Cat', 'porcupine', 'Porcupine'], message="Species has to be Dog, Cat, or Porcupine", values_formatter=None)])
    age = IntegerField('Age of Pet', validators=[NumberRange(
        min=0, max=30, message="Age must be between 1-30 years.")])
    image_url = StringField('Image URL', validators=[
                            URL(require_tld=True, message="Please enter a valid URL.")])
    notes = TextAreaField('Notes')
    available = BooleanField('Available')
