from app.forms import NewAppointmentForm
from flask import Blueprint, render_template, redirect
import psycopg2
import os
from datetime import datetime

bp = Blueprint('main', __name__, url_prefix="/")

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route("/", methods=["GET", "POST"])
def main():
  form = NewAppointmentForm()

  with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
      with conn.cursor() as curs:
        def get_appoint():
          curs.execute(
            """
            SELECT id, name, start_datetime, end_datetime
            FROM appointments
            ORDER BY start_datetime;
            """)
          return curs.fetchall()

        results = get_appoint()
        print(results)


  if form.validate_on_submit():
    params = {
        'name': form.name.data,
        'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
        'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
        'description': form.description.data,
        'private': form.private.data
    }
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
      with conn.cursor() as curs:
        # @mark.parameterize
        def add_appoint(name, start_datetime, end_datetime, description, private):
          curs.execute(
            """
            INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
            VALUES (%(name)s, %(start_datetime)s, %(end_datetime)s, %(description)s, %(private)s)
            """,
                {
                'name': name,
                'start_datetime': start_datetime,
                'end_datetime': end_datetime,
                'description': description,
                'private': private
                }
          )

        add_appoint(**params)
    return redirect('/')


  return render_template("main.html", rows=results, form=form)
