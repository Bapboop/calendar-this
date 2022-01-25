from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix="/")


def main():
  return "Calendar working"