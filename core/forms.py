from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

from wtforms.validators import Length


class ContactForm(FlaskForm):
    name = StringField(render_kw={"placeholder": "Name and surname"}, 
                       validators=[Length(min=3, max=30)])
    phone = StringField(render_kw={"placeholder": "Enter phone number"},
                        validators=[Length(min=10, max=15)])
    message = TextAreaField(render_kw={"placeholder": "Enter message"})
