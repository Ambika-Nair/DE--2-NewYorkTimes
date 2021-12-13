# Import system packages and libraries 
from time import sleep
from kafka import KafkaProducer
import json

# Import user packages and libraries 
from nytWire import get_newsWire
from pprint import pprint

# Serialize json data for producer
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Kafka producer to publish messages to Kafka topic - 'nytWire' 
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer = json_serializer)

if __name__ == '__main__':
# Run the process infinitely, because the data is a real-time stream
    while 1==1:
        news = get_newsWire()
        for each in news:
            print(each)
            producer.send('nytWire',each)
            sleep(4)