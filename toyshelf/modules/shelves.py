from flask import Blueprint

shelves = Blueprint("shelves", __name__)


@shelves.route("/")
def get_ingredients():
    return "Hello world from ingredients"
