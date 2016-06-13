from flask import abort
from api.models import Event



def abort_if_event_doesnt_exist(event_id):
    if Event.query(Event.id == event_id).count() < 1:
        # abort(404, {'message': "Event {} doesn't exist".format(event_id)})
        abort(404)