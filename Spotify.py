import requests
from pprint import pprint

def artist_search(name):
    #takes name into api and searches for its ID. returns ID.
    pass

######          TOP TRACKS FOR AN ARTIST        #####
def top_tracks(artistID):
    Client_id = '1a3a8ea947e0445f88fa68c4056d0e2a'
    Client_secret = '5ed0d9e6382143d2882915ba397271e4'
    Token = 'Bearer BQAMRC-5f5Xuu0uza9RHC9-M6jX65aHq4LgIlQgNS7iWhAPXFdefiKPZwh9PPQqTDwOqj8kicTqeVfoURzuJrpttPP1wHm6kKQBhZP1FVyAiBqh978oRm-I6jVg0bBffbo64ajFagP-7Ou_tUQ'
    Sample_id = '1vCWHaC5f2uS3yhpwWbIA6'
    url = 'https://api.spotify.com/v1/artists/'+Sample_id+'/top-tracks'

    params = {'country':'US'}
    headers= {'Accept':'application/json','Authorization':Token}

    r= requests.get(url,params=params,headers=headers)
    print(r.status_code)
    a= r.json()

    top_list = a['tracks']

    
    song1 = top_list[0]['name']
    pop1 = top_list[0]['popularity']
    song2 = top_list[1]['name']
    pop2 = top_list[1]['popularity']
    song3 = top_list[2]['name']
    pop3 = top_list[2]['popularity']
    song4 = top_list[3]['name']
    pop4 = top_list[3]['popularity']
    song5 = top_list[4]['name']
    pop5 = top_list[4]['popularity']
    song6 = top_list[5]['name']
    pop6 = top_list[5]['popularity']
    song7 = top_list[6]['name']
    pop7 = top_list[6]['popularity']
    song8 = top_list[7]['name']
    pop8 = top_list[8]['popularity']
    song9 = top_list[8]['name']
    pop9 = top_list[9]['popularity']
    song10= top_list[9]['name']
    pop10 = top_list[9]['popularity']

    top_names = [song1,song2,song3,song4,song5,song6,song7,song8,song9,song10]
    top_pops = [pop1, pop2, pop3, pop4, pop5, pop6, pop7, pop8, pop9, pop10 ]

    return top_pops
# def track_req(blah, Client_id = Client_id, Client_secret = Client_secret):
# 	url = 'https://api.spotify.com/v1/artists/',blah,'top-tracks'
# 	headers = {'Authorization':'	'}

	
# url_users = 'https://accorin.harvestapp.com/api/v2/users'
# headers={'Authorization':'Bearer 1394475.pt.LGPWqst-aA_J3P1Wz4_q-qHEcHRcVKRQ8zZhidxjjSRh83dPz1AxgQYrVZss1-ibpXE2rBph6N1G8WbD2TdqAA','Harvest-Account-Id': '564947','User-Agent':'MyApp (andrewp@accorin.com)'}
# u=requests.get(url_users, headers=headers)
# proj_users = u.json()['users']