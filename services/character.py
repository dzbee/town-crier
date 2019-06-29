from flask import request, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, validators

from lib.character import GENDER, RACES, CLASSES

class CharacterForm(FlaskForm):
    name = StringField("Name")
    gender = SelectField("Gender", validators=[validators.DataRequired()],
                         coerce=int, choicse=GENDER)
    race = SelectField("Race", validators=[validators.DataRequired()],
                       coerce=int, choices=RACES)
    role = SelectField("Class", validators=[validators.DataRequired()],
                       coerce=int, choices=CLASSES)
    submit = SubmitField("Submit")

def register_character_endpoints(app):

    @app.route('/character')
    def character():
        form = CharacterForm(request.form)
        if request.method == 'POST' and form.validate():
            return 'hello world'

        return render_template('form.html', form=form)
