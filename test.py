import requests
import json
import html
Client_id = '1a3a8ea947e0445f88fa68c4056d0e2a'
Client_secret = '5ed0d9e6382143d2882915ba397271e4'
url = "https://accounts.spotify.com/authorize"
redirect_uri = None
params = {'client_id':Client_id, 'response_type':'code', 'redirect_uri':redirect_uri, 'show_dialog':'True'}
a = requests.get(url, params = params)
print(a.status_code)
print(a._content)
