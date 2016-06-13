from main import api

# API URLS
from api.views import *

api.add_resource(Index, '/', endpoint='index')
api.add_resource(EventList, '/api/v1/events/', endpoint='events')
api.add_resource(EventDetail, '/api/v1/events/<event_id>', endpoint='event_detail')


# Auth URLS
# from auth.views import *
#
# api.add_resource(UserList, '/api/v1/users/', endpoint='userlist')
# # api.add_resource(Token, '/api/v1/users/token', endpoint='usertokens')
# api.add_resource(Login, '/api/v1/users/login/', endpoint='userlogin')
# api.add_resource(Logout, '/api/v1/users/logout/', endpoint='userlogout')
