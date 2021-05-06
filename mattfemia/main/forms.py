from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email

#
# Root level forms 
#

class ContactForm(FlaskForm):
    ''' Contact form for / route '''
    name = StringField(
        id='contactName',
        validators=[
            InputRequired(message='Name field is required.')
        ]
    )
    email = StringField(
        id='contactEmail',
        validators=[
            InputRequired(message='Email field is required.'),
            Email(message='Please enter a valid email address.')
        ]
    )
    message = TextAreaField(
        id='contactMessage',
        validators=[
            InputRequired(message='Message is required.')
        ]
    )
    submit = SubmitField(
        id='contactSubmit',
        label='Send'
    )