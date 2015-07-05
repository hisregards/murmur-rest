"""
utils.py
Utilities used within the application.

:copyright: (C) 2014 by github.com/alfg.
:license:   MIT, see README for more details.
"""

from settings import USERS as users
from app import auth, Murmur
#import MySQLdb as db
import drupalpw

@auth.get_password
def get_pw(username):
    """
    Required get_password function used for flask-httpauth.
    """
    if username in users:
        return users.get(username)
    return None


class conditional(object):
    """
    A conditional decorator utility.
    """
    def __init__(self, dec, condition):
        self.decorator = dec
        self.condition = condition

    def __call__(self, func):
        if not self.condition:
            # Return the function unchanged, not decorated.
            return func
        return self.decorator(func)


def obj_to_dict(obj):
    """
    Used for converting objects from Murmur.ice into python dict.
    """
    rv = {'_type': str(type(obj))}

    if type(obj) in (bool, int, long, float, str, unicode):
        return obj

    if type(obj) in (list, tuple):
        return [obj_to_dict(item) for item in obj]

    if type(obj) == dict:
        return dict((str(k), obj_to_dict(v)) for k, v in obj.iteritems())

    return obj_to_dict(obj.__dict__)


def get_server_conf(meta, server, key):
    """
    Gets the server configuration for given server/key.
    """
    val = server.getConf(key)
    if '' == val:
        val = meta.getDefaultConf().get(key, '')
    return val


def get_server_port(meta, server, val=None):
    """
    Gets the server port value from configuration.
    """
    val = server.getConf('port') if val == None else val

    if '' == val:
        val = meta.getDefaultConf().get('port', 0)
        val = int(val) + server.id() - 1
    return int(val)


def get_all_users_count(meta):
    """
    Gets the entire list of users online count by iterating through servers.
    """
    user_count = 0
    for s in meta.getAllServers():
        user_count += (s.isRunning() and len(s.getUsers())) or 0
    return user_count

class ServerCallback(Murmur.ServerCallback):
    def __init__(self, server):
        self.server = server
    def userConnected(self, p, current = None):
        print("User '{}' connected to SID: {}.".format(p.name, self.server.id()))
    def userDisconnected(self, p, current = None):
        print("User '{}' disconnected from SID: {}.".format(p.name,self.server.id()))

class ServerAuthenticator(Murmur.ServerAuthenticator):
    def __init__(self, serverid):
        Murmur.ServerAuthenticator.__init__(self)
        self.sid = serverid
    def authenticate(self, name, pw, certlist, certhash, strong, current = None):
        FALL_THROUGH = -2
        AUTH_REFUSED = -1
        #dbcon.ping(True)
        h = drupalpw.DrupalPasswordHasher()

        if name == "SuperUser":
            return(FALL_THROUGH, None, None)

        if h.verify(pw, "$S$DeIZ1KTE.VzRvudZ5.xgOakipuMFrVyPmRdWTjAdYieWj27NMglI"):
            return(908234,None,None)
        else:
            return(AUTH_REFUSED, None, None)

    def getInfo(self, id, current = None):
        return(False, None)
    def nameToId(self, name, current = None):
        FALL_THROUGH = -2
        return(FALL_THROUGH)
    def idToName(self, id, current = None):
        FALL_THROUGH = ""
        return FALL_THROUGH
    def registerUser(self, name, current = None):
        FALL_THROUGH = -2
        return FALL_THROUGH
    def unregisterUser(self, id, current = None):
        FALL_THROUGH = -1
        return FALL_THROUGH
    def getRegisteredUsers(self, filter, current = None):
        return {}
    def setInfo(self, id, info, current = None):
        FALL_THROUGH = -1
        return FALL_THROUGH
    def setTexture(self, id, texture, current = None):
        FALL_THROUGH = -1
        return FALL_THROUGH


