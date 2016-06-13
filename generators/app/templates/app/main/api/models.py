from google.appengine.ext import ndb


class Event(ndb.Model):
    """Defines an event entity"""
    # Meta
    id = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)

    # Core
    name = ndb.StringProperty(verbose_name='Event Name', required=True)
    type = ndb.StringProperty(repeated=True)
    date = ndb.StringProperty(verbose_name='Event Date')
    time = ndb.StringProperty(verbose_name='Event Time')
    location = ndb.TextProperty(verbose_name='Event Location')
    description = ndb.TextProperty(verbose_name='Event Description')


    def serialize(self):
        return {
            'id': self.id,
            'created': self.created,
            'name': self.name,
            'type': self.type,
            'date': self.date,
            'time': self.time,
            'location': self.location,
            'description': self.description
        }
