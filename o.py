#!/usr/bin/python
import datetime
import hashlib
import json
import logging
import os
import time
from subprocess import call

print "Content-type: text/html"
print

def generate_hashstring(user):
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H')
    hashbase = user['client'] + '&' + user['secret'] + '&' + timestamp
    m = hashlib.md5()
    m.update(hashbase)
    return m.hexdigest()

def open_door(user):
    logging.error(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S ') + user['name'] + ' is home!')
    call(["sudo", "/usr/lib/cgi-bin/od.py"])

def get_user(client):
    with open('keys.json') as keys_file:
        keys = json.load(keys_file)
    for key in keys:
        if key['client'] == client:
            return key
    return none

auth = os.environ['HTTP_X_OD']
auth_components = auth.split('&')
client = auth_components[0]
hashstring = auth_components[1]
user = get_user(client)
if user and (hashstring == generate_hashstring(user)):
    open_door(user)
else:
    logging.error('An imposter has been stopped!')
