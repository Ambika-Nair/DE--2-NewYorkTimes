# Import system packages and libraries
from kafka import KafkaConsumer
import json

# Import user packages and libraries
from mongoConnect import insertNewsWire

# Kafka consumer to retrieve messages from Kafka topic - 'nytWire' 
consumer = KafkaConsumer(
        "nytWire", # topic
        bootstrap_servers = ['localhost:9092'],
        auto_offset_reset = 'earliest', #tells the new consumer to start consuming from the earliest
        group_id = "consumer-group-nytWire") #providing a consumer group id

if __name__ == '__main__':

# Run the process as long as messages are being published to the kafka topic
    for msg in consumer:
        data = json.loads(msg.value)
        insertNewsWire(data)
        print(data)