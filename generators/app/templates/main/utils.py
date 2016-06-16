from flask import abort


# def abort_if_event_doesnt_exist(event_id):
#     if Event.query(Event.id == event_id).count() < 1:
#         # abort(404, {'message': "Event {} doesn't exist".format(event_id)})
#         abort(404)

def abort_if_item_doesnt_exist(model, item_id):
    if model.query(model.id == item_id).count() < 1:
        abort(404)
