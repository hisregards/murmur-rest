## Murmur-rest API v1

### Overview

Murmur-REST is a RESTful web application wrapper over the Murmur SLICE API to administer virtual Mumble servers. The API allows you to develop your own application using the feature set and endpoints provided. This project was built to administer Mumble servers for [Guildbit.com](http://guildbit.com). 

Murmur-REST is still in early development. If you find any issues or would like to help contribute to the project, please report them via Github issues or send a pull request.

### Endpoints

#### Servers

| Endpoint | Description |
| ---- | --------------- |
| GET /servers/ | Get server list |
| GET /servers/:serverid/ | Get server details |
| POST /servers/:serverid/ | Create server |
| DELETE /servers/:serverid/ | Delete server |
| GET /server/:serverid/logs/ | Get server logs
| GET /server/:serverid/channels/ | Get server channels
| GET /server/:serverid/channels/:channelid/ | Get server channel details
| GET /server/:serverid/bans/ | Get list of banned users
| GET /server/:serverid/conf/ | Get server configuration for specified id
| GET /server/:serverid/channels/:channelid/acl/ | Get ACL list for channel ID
| POST /server/:serverid/setsuperuserpw/ | Sets SuperUser password
| GET /server/:serverid/authenticator | Turns on an authenticator callback for the server ID given

#### Stats

| Endpoint | Description |
| ---- | --------------- |
| GET /stats/ | Get all statistics |

#### Users

| Endpoint | Description |
| ---- | --------------- |
| GET /server/:serverid/user/:userid | Get User |
| POST /server/:serverid/user | Create User, formdata:  username&password |
| DELETE /server/:serverid/user/:userid | Delete User |

###  Deployment for Development

Assuming you already have Murmur running and set up, follow the instructions below to run murmur-rest
for development. Tested on Ubuntu 13.10, but should be to run wherever Murmur and Zero Ice are supported.

Runserver.py uses Flask's development server. This should be used for development only. See 
Deployment for Production for running in production mode. Python virtualenv is highly recommended as well.

1) Install required Zero Ice library

`sudo apt-get install python-zeroc-ice`

2) Clone and install murmur-rest

```
git clone git@github.com:alfg/murmur-rest.git
cd /directory/to/murmur-rest
pip install -r requirements.txt
```

*Note*: If running in virtualenv, use the `--system-site-packages` flag in order to import the Ice library.

3) Run and test application

```
$ python runserver.py
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
 
$ curl http://127.0.0.1:5000/servers/
[
    {
        "address": ":::64739",
        "channels": 1,
        "humanize_uptime": "0:00:02",
        "id": 2,
        "log_length": 35,
        "maxusers": "10",
        "name": "",
        "running": true,
        "uptime": 2,
        "users": 0
    }
]
```

###  Deployment for Production

Following the same steps for Deployment for Development, just use a Python WSGI application server
such as [Gunicorn](http://gunicorn.org/) instead of the built-in Flask server. The provided `wsgi.py`
file is provided for this.

For example, if using Gunicorn and virtualenv:

```
/path/to/murmur-rest/env/bin/gunicorn -b 127.0.0.1:5000 wsgi:app
```

### Notes

- Early development. Expect changes that might break the first revision of the RESTful API
- API is incomplete and will be completed over time
- I'm following the RESTful API specification and standards as closely as I can (with some exceptions), please feel
free to suggest any corrections
- Murmur SLICE API is located here: http://mumble.sourceforge.net/slice/Murmur.html

### TODO

- Authentication
- Complete support for full Murmur SLICE API
- Easier deployment for production
- Documentation
- Error Handling

### Resources
- [Murmur SLICE API](http://mumble.sourceforge.net/slice/Murmur.html)
- RESTful design resources:
    - https://github.com/WhiteHouse/api-standards
    - http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
    - http://mark-kirby.co.uk/2013/creating-a-true-rest-api/

### License

The MIT License (MIT)

Copyright (c) 2014 github.com/alfg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
