# Import system packages and libraries 
import requests
from pprint import pprint

# Provide API key generated from New Tork Times developer login
api_key = 'LCucvFVIBGr3W0LGj8FwkTe8L00xiAxA'
# API url of Times NewsWire API for real-time stream of every article published in New York Times
url = 'https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key='+api_key

# Data pre-processing to filter and clean required fields
def get_newsWire():
    query = requests.get(url).json()
    ls = query['results']
    d = []
    for dict in ls:
        data = {}
        data['section'] = dict['section']
        data['title'] = dict['title']
        data['abstract'] = dict['abstract']
        data['url'] = dict['url']
        byline  = dict['byline'] 
        data['author'] = byline[3:len(byline)]
        data['source'] = dict['source']
        data['published_date'] = dict['published_date']
        d.append(data)
    return d

if __name__ == '__main__':
    data = get_newsWire()
    pprint(data[0])
