from flask import Flask
from .modules.shelf import Bookcase


app = Flask(__name__)


@app.route('/toys/shelves')
def shelves():
    return Bookcase().shelves()


@app.route('/toys/<shelf>')
def toys(shelf):
    return Bookcase().toys(shelf)
