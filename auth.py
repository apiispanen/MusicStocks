def req_token():
    import spotipy
    import spotipy.util as util
    import requests 
    import sys
    spotify = spotipy.Spotify()
    Client_id = '1a3a8ea947e0445f88fa68c4056d0e2a'
    Client_secret = '5ed0d9e6382143d2882915ba397271e4'
    scopes = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private	streaming ugc-image-upload user-read-email user-top-read user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played'

    scope = 'user-library-read user-read-private user-read-email' 

    usernamed = '1224597393'
    tusername = sys.argv[0]
    username = 'appiispanen@gmail.com'

    token ='Bearer '+util.prompt_for_user_token(username, scope = scope, client_id = Client_id, client_secret=Client_secret, redirect_uri ='http://127.0.0.1:5000/')

    return token 
# results = spotify.search(q='artist:' + 'Birdy', type='artist')
# print(results)