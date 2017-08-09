#!/usr/bin/env python
# -*- coding: utf-8 -*-
u'''
Populates the environment variables from a json file
and authenticates via Jason Web Token
'''

from __future__ import with_statement
from __future__ import absolute_import
from io import open #pylint: disable=redefined-builtin
import json
import os
import sys


from keyring import get_password, set_password
from boxsdk import JWTAuth, Client

JSON_FILE = u'./.box/app_settings.json'
PRIVATE_KEY_FILE = u'./.box/private_key.pem'

# Set a service name to use the keyring or set service to None to
# use the environment to store your credentials
# If using a service name the json file is removed after the first run
# Your credentials are now save withouth having them in the code
SERVICE = None # u'jwt_demo'


def get_key(key, service=None):
    u'''
    Stores a credential in keyring or environment
    '''
    if service is None:
        return os.environ.get(key)
    return get_password(service, key)


def set_key(key, value, service=None):
    u'''
    Retrieves a credential from keyring or environment
    '''
    if service is None:
        os.environ.setdefault(key.lower(), value)
    else:
        set_password(service, key.lower(), value)


def write_private_key(value, key_path):
    u'''
    Write the private key to a file with secure permissions
    '''
    with open(key_path, u'w+') as key_file:
        os.chmod(key_path, 0600)
        key_file.write(value)


def store_json(data, service, key_path):
    u'''
    Walk through the json file and store each entry in the keyring
    as a key value pair
    store the key in a separate file and change permission to user ro
    '''
    for key, value in data.items():
        # if we hit the private key, store it in a file
        if key.lower() == u'privatekey':
            write_private_key(value, key_path)
            continue
        if isinstance(value, dict):
            # recursively call the function until all key value pairs are done
            store_json(value, service, key_path)
        else:
            set_key(key, value, service)


def read_token(key, service=None):
    u'''
    Reads the access token from keyring
    '''
    return get_key(key, service)


def store_token(access_token, _, service=None):
    u'''
    Callback function for storage of the access token
    '''
    set_key(u'access_token', access_token, service)


def init_credentials(json_path, private_key_file, service=None):
    u'''
    Populate the the application secrets into keyring or environment
    Store the private key in a file
    '''
    if os.path.exists(json_path):
        with open(json_path, u'r') as json_file:
            json_data = json.load(json_file)
            store_json(json_data, service, private_key_file)
        if service:
            os.remove(json_path)
    else:
        # No credentials are available
        if service is None or get_key(u'clientid', service) is None:
            sys.exit(u'No app configuration file and\
 keyring not enabled or empty')


def get_passphrase(service):
    u'''
    Passphrase is different in python2 and python3
    '''
    return str(get_key('passphrase', service)).encode('utf_8')


def authorize_jwt_client(private_key_file, service=None):
    u'''
    Create a jwt client
    '''
    passphrase = get_passphrase(service)
    jwt_auth = JWTAuth(
        client_id=get_key(u'clientid', service),
        client_secret=get_key(u'clientsecret', service),
        enterprise_id=get_key(u'enterpriseid', service),
        jwt_key_id=get_key(u'publickeyid', service),
        access_token=read_token(u'access_token', service),
        rsa_private_key_file_sys_path=private_key_file,
        rsa_private_key_passphrase=passphrase,
        store_tokens=lambda acc, _: store_token(acc, _, service)
    )
    jwt_auth.authenticate_instance()
    return Client(jwt_auth)


def main(json_file, private_key_file, service=None):
    u'''
    The main program authorize the application
    '''
    init_credentials(json_file, private_key_file, service)
    client = authorize_jwt_client(private_key_file, service)
    current_user = client.user(user_id=u'me').get()
    print u'Box User:', current_user.name
    users = client.users()
    print users
    user = users[0]
    print user.id, user.login, user.created_at
    files = client.as_user(user).folder(0).get_items(10)
    for file in files:
        print file.id, file.name


if __name__ == u'__main__':
    main(JSON_FILE, PRIVATE_KEY_FILE, SERVICE)
