from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


# Core views
# import main.auth.views
import main.api.views
