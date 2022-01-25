from app import routes
from flask import flask
import os

app = Flask(__name__)
app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(routes.bp)