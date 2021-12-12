import requests
from pprint import pprint

#Extracting data from 3 APi's to get popular articles published daily, weekly and monthly.
requestUrl_daily = "https://api.nytimes.com/svc/mostpopular/v2/emailed/1.json?api-key=L3F9t43bEo6WtwYPQwsz9CT7XryDDfzq"
requestUrl_weekly = "https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key=L3F9t43bEo6WtwYPQwsz9CT7XryDDfzq"
requestUrl_monthly = "https://api.nytimes.com/svc/mostpopular/v2/emailed/30.json?api-key=L3F9t43bEo6WtwYPQwsz9CT7XryDDfzq"

def get_nyt_popular():
    query_daily = requests.get(requestUrl_daily)
    query_weekly = requests.get(requestUrl_weekly)
    query_monthly = requests.get(requestUrl_monthly)
    
    data_daily = query_daily.json()
    data_weekly = query_weekly.json()
    data_monthly = query_monthly.json()
    # print (data)
    return (data_daily, data_weekly, data_monthly)

if __name__ == '__main__':
    print(get_nyt_popular)
