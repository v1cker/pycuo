import requests
def url_get(url,**kwargs):
    try:
        req = requests.get(url,kwargs)
    except:
        return None
    #print(req.encoding)
    return req