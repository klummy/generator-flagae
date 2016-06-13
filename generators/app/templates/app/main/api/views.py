from flask import render_template, request, make_response, redirect, url_for, flash, jsonify
from flask.ext import restful
from flask_restful import reqparse
from flask.ext.login import login_required

from main import app, api
from main.utils import *

from .models import Event


parser = reqparse.RequestParser()
parser.add_argument('name', type = str, required = True, help = 'Provide event name')
parser.add_argument('date', type=str)
parser.add_argument('time', type=str)
parser.add_argument('location', type = str,)
parser.add_argument('description', type = str)
parser.add_argument('type', type = str, action='append')



class Index(restful.Resource):
    """ApiRoot"""
    def get(self):
        return {'message': 'Welcome to the Funophile APIRoot'}



class EventList(restful.Resource):
    """Get and create events"""
    def get(self):
        events = Event.query().order(Event.created)
        return jsonify(events=[r.serialize() for r in events])

    # @login_required
    def post(self):
        args = parser.parse_args()
        event = Event()
        event.id = Event.query().count() + 1

        event.name = args['name']
        event.type = args['type']
        event.date = args['date']
        event.time = args['time']
        event.location = args['location']
        event.description = args['description']
        event.put()

        return jsonify(event=[event.serialize()])


class EventDetail(restful.Resource):
    def get(self, event_id):
        event_id = int(event_id)
        abort_if_event_doesnt_exist(event_id)
        event = Event.query(Event.id == event_id).get()
        return jsonify(event=[event.serialize()])

    # @login_required
    def delete(self, event_id):
        event_id = int(event_id)
        abort_if_event_doesnt_exist(event_id)

        event = Event.query(Event.id == event_id).get()
        event.key.delete()
        return {'message': 'Event {} deleted'.format(event_id)}

    # @login_required
    def put(self, event_id):
        args = parser.parse_args()
        event_id = int(event_id)
        event = Event.query(Event.id == event_id).get()

        if args['name']:
            event.name = args['name']
        else: pass

        if args['type']:
            event.type = args['type']
        else: pass

        if args['date']:
            event.date = args['date']
        else: pass

        if args['time']:
            event.time = args['time']
        else: pass

        if args['location']:
            event.location = args['location']
        else: pass

        if args['description']:
            event.description = args['description']
        else: pass

        event.put()

        return jsonify(event=[event.serialize()])



@app.errorhandler(404)
def page_not_found(env):
    """Return 404 error page"""
    return 'Page not found-ed.', 404


@app.errorhandler(500)
def application_error(e):
    """Return custom 500 error."""
    return 'Application error: {}'.format(e), 500
