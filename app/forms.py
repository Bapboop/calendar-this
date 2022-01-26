from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime
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

    def validate_end_date(form, field):
        start = datetime.combine(form.start_date.data, form.start_time.data)
        end = datetime.combine(form.end_date.data, form.end_time.data)
        print('start date here', start)

        if form.start_date.data != form.end_date.data:
            raise ValidationError("Your start date must be the same as your end date")

        if start >= end:
            raise ValidationError("End date/time must come after start date/time")
