#!/usr/bin/python
import datetime
import hashlib
import logging
import os
import time
import pigpio

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


def openDoor(user):
    p1 = pigpio.pi()
    p1.write(2,0)
    time.sleep(5)
    p1.write(2,1)


auth = os.environ['HTTP_X_OD']
auth_components = auth.split('&')
client = auth_components[0]
hashstring = auth_components[1]

if hashstring == getHashedKey(client):
    openDoor(keys[client][0])
else:
    logging.error('An imposter has been stopped!')
