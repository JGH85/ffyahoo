from rauth import OAuth1Service
import xml.etree.ElementTree as ET
import pandas as pd
import time
import os
from config import client_id, client_secret

OAUTH_CONSUMER_KEY = client_id
OAUTH_SHARED_SECRET = client_secret

request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
authorize_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
access_token_url = 'https://api.login.yahoo.com/oauth/v2/get_token'

yahoo = OAuth1Service(consumer_key=OAUTH_CONSUMER_KEY,\
                      consumer_secret=OAUTH_SHARED_SECRET,\
                      name='yahoo',\
                      access_token_url=access_token_url,\
                      authorize_url=authorize_url,\
                      request_token_url=request_token_url,\
                      base_url='https://api.login.yahoo.com/oauth/v2/')

request_token, request_token_secret = yahoo.get_request_token\
(data = {'oauth_callback': "http://example.com/callback/" })

print("Request Token:") 
print(" - oauth_token = %s" % request_token)
print(" - oauth_token_secret = %s" % request_token_secret)
auth_url = yahoo.get_authorize_url(request_token)
print('Visit this URL in your browser: ' + auth_url)

pin = raw_input('Enter PIN from browser: ')

session = yahoo.get_auth_session(request_token,\
                                 request_token_secret,\
                                 method='POST',\
                                 data={'oauth_verifier': pin})
