#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A simple web interface for authentication
'''

import os

from flask import Flask
from flask import request


app = Flask(__name__) #pylint: disable=invalid-name


@app.route('/')
def index():
    '''
    The index page of the box demo app
    '''
    return 'This is a box api demo'


@app.route('/api/webhookv1/', methods=['GET', 'POST'])
def webhooks():
    '''
    Endpoint to receive v1 webhooks
    '''
    if request.method == 'POST':
        return 'POST has been received. Headers: {}, Args: {}'\
               .format(request.headers, request.args)
    return 'Webhook V1 endpoint GET has been received.\
 Headers: {}, Args: {}'.format(request.headers, request.args)


@app.route('/api/redirect')
def get_auth_code():
    '''
    Get the auth code for oauth2 applications
    '''
    code = request.args.get('code')
    return 'Authorization Code: {}'.format(code)


def main():
    '''
    The main app
    '''
    app.run(port=int(os.environ.get('PORT')),
            host=os.environ.get('IP'),
            debug=True)

if __name__ == '__main__':
    main()
