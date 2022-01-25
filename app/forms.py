from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired
# from wtforms.widgets.html5 import DateInput, TimeInput

class NewAppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("start date", validators=[DataRequired()])
    start_time = TimeField("start time", validators=[DataRequired()])
    end_date = DateField("end date", validators=[DataRequired()])
    end_time = TimeField("end time", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    private = BooleanField("private")

    submit = SubmitField("Add Appointment")
