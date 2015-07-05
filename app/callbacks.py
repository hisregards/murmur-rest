"""
murmur-rest

callbacks.py
Initialize murmur-rest project.

:copyright: (C) 2014 by github.com/alfg.
:license:   MIT, see README for more details.
"""

from app import Murmur
import drupalpw

class MetaCallback(Murmur.MetaCallback):
    def __init__(self):
        Murmur.MetaCallback.__init__(self)
    def started(self, server, current = None):
        print("Server {} started".format(server.id()))
    def stopped(self, server, current = None):
        print("Server {} stopped".format(server.id()))

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
