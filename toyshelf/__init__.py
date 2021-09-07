from flask import Flask
from .modules.shelves import shelves

app = Flask(__name__)

# Register blueprints
app.register_blueprint(shelves, url_prefix="/shelves")


@app.route('/')
def hello_world():
    return 'Hello, World!'
