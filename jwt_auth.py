#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Populates the environment variables from a json file
and authenticates via Jason Web Token
'''

import json
import os
import sys

from keyring import get_password, set_password
from boxsdk import JWTAuth, Client

JSON_FILE = './.box/app_settings.json'
PRIVATE_KEY_FILE = './.box/private_key.pem'


# Set a service name to use the keyring or set service to None to
# use the environment to store your credentials
# If using a service name the json file is removed after the first run
# Your credentials are now save withouth having them in the code
SERVICE = 'jwt_auth'


def get_key(key, service=None):
    '''
    Stores a credential in keyring or environment
    '''
    if service is None:
        return os.environ.get(key)
    return get_password(service, key)


def set_key(key, value, service=None):
    '''
    Retrieves a credential from keyring or environment
    '''
    if service is None:
        os.environ.setdefault(key.lower(), value)
    else:
        set_password(service, key.lower(), value)


def write_private_key(value, key_path):
    '''
    Write the private key to a file with secure permissions
    '''
    with open(key_path, 'w+') as key_file:
        os.chmod(key_path, 0o600)
        key_file.write(value)


def store_json(data, service, key_path):
    '''
    Walk through the json file and store each entry in the keyring
    as a key value pair
    store the key in a separate file and change permission to user ro
    '''
    for key, value in data.items():
        # if we hit the private key, store it in a file
        if key.lower() == 'privatekey':
            write_private_key(value, key_path)
            continue
        if isinstance(value, dict):
            # recursively call the function until all key value pairs are done
            store_json(value, service, key_path)
        else:
            set_key(key, value, service)


def store_token(access_token, _, service=None):
    '''
    Callback function for storage of the access token
    '''
    set_key('access_token', access_token, service)


def init_credentials(json_path, private_key_file, service=None):
    '''
    Populate the the application secrets into keyring or environment
    Store the private key in a file
    '''
    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            json_data = json.load(json_file)
            store_json(json_data, service, private_key_file)
        if service:
            os.remove(json_path)
    else:
        # No credentials are available
        if service is None or get_key('clientid', service) is None:
            sys.exit('No app configuration file and\
 keyring not enabled or empty')


def authorize_jwt_client(private_key_file, service=None):
    '''
    Create a jwt client
    '''
    jwt_auth = JWTAuth(
        client_id=get_key('clientid', service),
        client_secret=get_key('clientsecret', service),
        enterprise_id=get_key('enterpriseid', service),
        jwt_key_id=get_key('publickeyid', service),
        access_token=get_key('access_token', service=None),
        rsa_private_key_file_sys_path=private_key_file,
        rsa_private_key_passphrase=str(get_key('passphrase',
                                               service)).encode('utf_8'),
        store_tokens=lambda acc, _: store_token(acc, _, service)
    )
    jwt_auth.authenticate_instance()
    return Client(jwt_auth)


def main(json_file, private_key_file, service=None):
    '''
    The main program authorize the application
    '''
    init_credentials(json_file, private_key_file, service)
    client = authorize_jwt_client(private_key_file, service)
    current_user = client.user(user_id='me').get()
    current_user.name 
    print('Successfully authenticated as Box user:',
          current_user.name,
          'email:',
          current_user.login)


if __name__ == '__main__':
    main(JSON_FILE, PRIVATE_KEY_FILE, SERVICE)
