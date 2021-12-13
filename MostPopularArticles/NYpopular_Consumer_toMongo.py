from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# function to check for duplicate Id's.
def alreadyExists(newID):
    i =0
    for each in db.PopularArticles.find({'_id': _id}):
        i += 1
    if i == 0:
        return False
    else:
        return True
        
# Connect to MongoDB and NYT database
try:
   client = MongoClient('mongodb+srv://AmbikaNair:MongoDB@cluster0.wjpum.mongodb.net/NYT&retryWrites=true&w=majority?ssl=true&ssl_cert_reqs=CERT_NONE')
   db = client.NYT
   print("Connected successfully!")
except:  
   print("Could not connect to MongoDB")
    

# connect kafka consumer to kafka topic	'popular'
consumer = KafkaConsumer(
        "popular",
        bootstrap_servers = ['localhost:9092'],
        auto_offset_reset = 'earliest',
        group_id = "consumer-group-nytpopular")

#Fetching only desired fields from messages to send to MongoDB
for msg in consumer:
    record = json.loads(msg.value)
    _id = record['id']
    source = record['source']
    published_date = record['published_date']
    section = record['section']
    keywords = record['adx_keywords']
    title = record['title']
    abstract = record['abstract']
    frequency = record['frequency']
    
    # Create dictionary and ingest data into MongoDB
    populararticles = {'_id':_id,'source':source,'published_date':published_date,'section':section, 'keywords':keywords, 'title':title, 'abstract':abstract, 'frequency':frequency}
    
    #Calling the function 'alreadyExists' that checks for duplicate Ids.
    if alreadyExists(_id):
        pass
    else:
        rec_id1 = db.PopularArticles.insert_one(populararticles)
        print("Data inserted with record ids", rec_id1)    
