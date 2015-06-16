"""
settings.py

All default settings. No configuration required, unless you want to enable digest authentication.

:copyright: (C) 2014 by github.com/alfg.
:license:   MIT, see README for more details.
"""

import os

# Settings for running a local dev server with runserver.py
APP_HOST = '127.0.0.1'
APP_PORT = 5000
APP_DEBUG = True

# Ice connectivity
ICE_HOST = 'Meta:tcp -h 127.0.0.1 -p 6502'
ICE_SECRET = 'barrelsexpoundutmoststaffs'
SLICE_FILE = 'Murmur.ice'

# Default path of application
MURMUR_ROOT = os.path.dirname(os.path.abspath(__file__))

# Digest Authentication. Add users as necessary.
ENABLE_AUTH = False  # If enabled, add user credentials below
USERS = {
    "admin": "password",
}
