from flask import request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, validators

from models.encounter import Scenario

class EncounterForm(FlaskForm):
    action = SelectField(validators=[validators.DataRequired()], coerce=int)
    submit = SubmitField("Submit")

def register_encounter_endpoints(app):

    @app.route('/encounter/<scenario_id>', methods=["GET", "POST"])
    def encounter(scenario_id):
        scenario = Scenario.query.get(scenario_id)
        form = EncounterForm(request.form)
        form.action.choices = [(choice.target_idn, choice.text) for choice in scenario.choices]
        if request.method == 'POST' and form.validate():
            return redirect('/encounter/{}'.format(form.action.data))

        return render_template('encounter.html', scenario_text=scenario.text, form=form)
