from google.appengine.ext import ndb


class Example(ndb.Model):
    """Defines an example entity"""
    # Meta
    id = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)

    # Core
    name = ndb.StringProperty(verbose_name='Event Name', required=True)
    type = ndb.StringProperty(repeated=True)


    def serialize(self):
        return {
            'id': self.id,
            'created': self.created,
            'name': self.name,
            'type': self.type
        }
