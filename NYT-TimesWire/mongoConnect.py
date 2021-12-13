# Import user packages and libraries 
from pymongo import MongoClient

# Create a connection to Mongo DB cluster
cluster = MongoClient("mongodb+srv://user1:Password1@cluster0.spop0.mongodb.net/NYT?retryWrites=true&w=majority")

# Define database
db = cluster['NYT']

# Define collection
NewsWire = db['NewsWire']

# Insert a record to NewsWire collection
def insertNewsWire(data):
    NewsWire.insert_one(data)

# Read a record from NewsWire collection
def get_newsWire_data():
    n = NewsWire.find({},{'section':1,'author':1,'published_date':1,'abstract':1,'_id':0})
    return n

# Aggregate records grouped by 'section' from NewsWire collection
def get_count_groupby_section():
    c = NewsWire.aggregate([
    # Group by author, return count
        {
        "$group":
            {"_id":"$section",
            "total":{"$sum":1}
            }
        },
    # Sort on total count DESCENDING (-1)
        {
        "$sort":
            {"total":-1}
        }
    #     },
    # # Limit to the top n rows (n=1)
    #     {
    #     "$limit": 1 
    #     }
    ])
    return c

# Aggregate records grouped by 'author' from NewsWire collection
def get_count_groupby_author():
    c = NewsWire.aggregate([
    # Group by author, return count
        {
        "$group":
            {"_id":"$author",
            "total":{"$sum":1}
            }
        },
    # Sort on total count DESCENDING (-1)
        {
        "$sort":
            {"total":-1}
        }
    #     },
    # # Limit to the top n rows (n=1)
    #     {
    #     "$limit": 1 
    #     }
    ])
    return c

if __name__ == '__main__':
    # d = {'a':1,'b':2,'c':3}
    # insertNewsWire(d)
    a = NewsWire.find({},{'section':1,'author':1,'published_date':1,'_id':0})
    i =0
    for each in a:
        i += 1
        if i == 1:
            print(each)