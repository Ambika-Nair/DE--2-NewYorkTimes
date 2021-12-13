import json
from kafka import KafkaProducer
from time import sleep
from data_NYpopular import get_nyt_popular
from pprint import pprint

#function to dump data into json and encoding it, so that when it is de-serialized, the text is based on utf-8
def json_serializer(data):
  return json.dumps(data).encode("utf-8")

#Defining kafka producer that connects to kafka server and returns a json
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer = json_serializer)


#Main function to iterate over APIs and send messages to kafka topic
if __name__ == "__main__":
  popular_daily,popular_weekly, popular_monthly = get_nyt_popular()
  
  res_daily = popular_daily['results']
  for each in res_daily:
    each["frequency"] = "daily"
    print(each)
    producer.send('popular',each)
    
    sleep(5)

  res_weekly = popular_weekly['results']
  for each in res_weekly:
    each["frequency"] = "weekly"
    print(each)
    producer.send('popular',each)
    sleep(5)

  res_monthly = popular_monthly['results']
  for each in res_monthly:
    each["frequency"] = "monthly"
    print(each)
    producer.send('popular',each)
    sleep(5)