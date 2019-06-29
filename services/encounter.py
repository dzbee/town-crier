from flask import request, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, validators

class EncounterForm(FlaskForm):
    action = SelectField(validators=[validators.DataRequired()])

def register_encounter_endpoints(app):

    @app.route('/encounter')
    def encounter():
        form = EncounterForm(request.form)
        form.action.choices = [('hello world', 0)]
        if request.method == 'POST' and form.validate():
            return 'hello world'

        return render_template('form.html', form=form)
