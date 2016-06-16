"""`main` is the top level module for your Flask application."""

from os import path

# Import the Flask Framework
from flask import Flask, make_response, render_template, request


app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


# Project imports
from main import app


app.config.from_object('settings')
