import requests
import os
from pprint import pprint

apikey = os.getenv('NYTIMES_APIKEY', '...')

# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "science"
query_url = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key=O9AAFWpjSNBTWZVc1lRCycpZ44KOs6J1"

r = requests.get(query_url)
print(r.text)