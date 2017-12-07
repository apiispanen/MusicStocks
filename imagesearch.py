
def get_image(search_term):
    import pprint
    import requests
    key = '7265758-6ef0b15f84f114613b42008f3'
    url = 'https://pixabay.com/api/'
    q = search_term.replace(' ','+')
    params = {'key':key, 'q': q}
    a = requests.get(url, params=params)
    b = a.json()
    if len(b['hits'])<1:
            return 'http://canacopegdl.com/images/shrug/shrug-8.jpg'
    else:
        return b['hits'][0]['previewURL']