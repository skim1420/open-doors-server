#!/usr/bin/python
import datetime
import hashlib
import logging
import os
import time

""" Replace keys set below with your own client/secret sets.
    You can just go to any random string generator website to get your keys. """

keys = {
    'client1' : ('User 1', 'secret1'),
    'client2' : ('User 2', 'secret2'),
    'client3' : ('User 3', 'secret3')
}

print "Content-type: text/html"
print

def getHashedKey(client):
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H')
    hashbase = client + '&' + keys[client][1] + '&' + timestamp
    m = hashlib.md5()
    m.update(hashbase)
    return m.hexdigest()

auth = os.environ['HTTP_X_OD']
auth_components = auth.split('&')
client = auth_components[0]
hashstring = auth_components[1]

if hashstring == getHashedKey(client):
# RPi.GPIO requries root /dev/mem access
    call(["sudo", "/usr/lib/cgi-bin/od.py"])
else:
    logging.error('An imposter has been stopped!')
