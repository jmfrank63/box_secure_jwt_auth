# -*- coding: utf-8 -*-
'''
Populates the environment variables or a keyring from a json file
and authenticates via Jason Web Token
'''

import json
import os

from boxsdk import JWTAuth, Client

SETTINGS_PATH = './.box'
SETTINGS_FILE = 'app_settings.json'
TOKEN_FILE = 'access_token.txt'


def read_settings(path):
    '''
    Put the exported settings into a dictionary
    '''
    with open(path, 'r', encoding='utf-8') as sfile:
        settings = json.load(sfile)
    return settings


def get_token(token_path):
    '''
    Read a token from a file if it exists
    '''
    if os.path.exists(token_path):
        with open(token_path, 'r') as token_file:
            token = token_file.read()
    return token


def store_token(access_token, _):
    '''
    Store the token in file
    '''
    with open(os.path.join(SETTINGS_PATH, TOKEN_FILE), 'w') as token_file:
        token_file.writelines(access_token)


def main(json_file):
    '''
    Authorize the application and print the user name and email
    '''
    settings = read_settings(json_file)
    auth = JWTAuth(
        client_id=settings['boxAppSettings']['clientID'],
        client_secret=settings['boxAppSettings']['clientSecret'],
        enterprise_id=settings['enterpriseID'],
        jwt_key_id=settings['boxAppSettings']['appAuth']['publicKeyID'],
        rsa_private_key_data=settings['boxAppSettings']['appAuth']
        ['privateKey'],
        rsa_private_key_passphrase=settings['boxAppSettings']['appAuth']
        ['passphrase'],
        store_tokens=store_token,
        access_token=get_token(os.path.join(SETTINGS_PATH, TOKEN_FILE)))
    client = Client(auth)
    current_user = client.user(user_id='me').get()
    print('Successfully authenticated user: {} with email: {}'.format(
        current_user.name, current_user.login))


if __name__ == '__main__':
    main(os.path.join(SETTINGS_PATH, SETTINGS_FILE))
