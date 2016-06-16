from flask import render_template, request, make_response, redirect, url_for, flash, jsonify
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.login import login_required

from main import app, api
from main.utils import *

from .models import *


parser = reqparse.RequestParser()
parser.add_argument('name', type = str, required = True, help = 'Provide example name')
parser.add_argument('type', type = str, action='append')


# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')
#
#
# @app.route('/<path:path>', methods=['GET'])
# def any_root_path(path):
#     return render_template('index.html')


class Index(restful.Resource):
    """ApiRoot"""
    def get(self):
        return {'message': 'Welcome to the APIRoot'}



class ExampleList(restful.Resource):
    """Get and create examples"""
    def get(self):
        examples = Example.query().order(Example.created)
        return jsonify(examples=[r.serialize() for r in examples])

    # @login_required
    def post(self):
        args = parser.parse_args()
        example = Example()
        example.id = Example.query().count() + 1

        example.name = args['name']
        example.type = args['type']

        example.put()

        return jsonify(example=[example.serialize()])


class ExampleDetail(restful.Resource):
    def get(self, example_id):
        example_id = int(example_id)

        abort_if_item_doesnt_exist(Example, example_id)

        example = Example.query(Example.id == example_id).get()
        return jsonify(example=[example.serialize()])

    # @login_required
    def delete(self, example_id):
        example_id = int(example_id)
        abort_if_item_doesnt_exist(Example, example_id)

        example = Example.query(Example.id == example_id).get()
        example.key.delete()
        return {'message': 'Example {} deleted'.format(example_id)}

    # @login_required
    def put(self, example_id):
        args = parser.parse_args()
        example_id = int(example_id)
        example = Example.query(Example.id == example_id).get()

        if args['name']:
            example.name = args['name']
        else: pass

        if args['type']:
            example.type = args['type']
        else: pass

        example.put()

        return jsonify(example=[example.serialize()])



@app.errorhandler(404)
def page_not_found(env):
    """Return 404 error page"""
    return 'Page not found-ed.', 404


@app.errorhandler(500)
def application_error(e):
    """Return custom 500 error."""
    return 'Application error: {}'.format(e), 500


api.add_resource(Index, '/', endpoint='index')
api.add_resource(ExampleList, '/api/v1/examples/', endpoint='examples')
api.add_resource(ExampleDetail, '/api/v1/examples/<example_id>', endpoint='example_detail')
