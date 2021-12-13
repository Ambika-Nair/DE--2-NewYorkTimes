import pymongo
client = pymongo.MongoClient("mongodb+srv://AmbikaNair:MongoDB@cluster0.wjpum.mongodb.net/NYT&retryWrites=true&w=majority?ssl=true&ssl_cert_reqs=CERT_NONE")
import matplotlib.pyplot as plt
import pandas as pd

# Database
database = client["NYT"]

# Collection
collection = database["PopularArticles"]

#Function to create bar chart
def create_plot(df,x_label,y_label):

    # Bar plot
    plt.figure(figsize=(15,10))
    df.sort_values(by="total",ascending=False).plot.bar(x="_id", y = "total")
    plt.xticks(rotation=50) 
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.show()

#Query to get the count of popular articles on daily, weekly and monthly basis
article_count = collection.aggregate(
    [{
    "$group" : 
        {"_id" : "$frequency",
         "total" : {"$sum" : 1}
         }}
    ])

print("Count of popular articles are:")
ls1=[]
for count in article_count:
    ls1.append(count)

article_data = pd.DataFrame(ls1)
print(article_data)
create_plot(article_data,"Frequency","Count of popular articles") 


#Query to get the count of all sections in which the popular articles are:
sectiondoc = collection.aggregate(
    [{
     "$group":
            {"_id": "$section",
             "total" : {"$sum":1}
            }}
    ])

print("Most popular articles are published in these sections:")
ls2=[]
for sectioncount in sectiondoc:
    ls2.append(sectioncount)

totalsectioncount = pd.DataFrame(ls2)
print(totalsectioncount)
create_plot(totalsectioncount,"Most popular Sections","Number of popular articles") 


#Query to get the count of each section on daily basis
dailydoc = collection.aggregate(
    [{
        "$match":{
            "frequency" : "daily"}},
         {"$group": 
             {"_id":"$section",
              "total" : {"$sum":1}
            }
    }]
)

print("Daily popular articles are in section:")
ls3=[]
for sectioncount in dailydoc:
    ls3.append(sectioncount)

dailysectioncount = pd.DataFrame(ls3)
print(dailysectioncount)
create_plot(dailysectioncount,"Daily Sections","Number of popular articles") 


#Query to get the count of each section on weekly basis

weeklydoc = collection.aggregate(
    [{
        "$match":{
            "frequency" : "weekly"}},
         {"$group": 
             {"_id":"$section",
              "total" : {"$sum":1}
            }
    }]
)

print("Weekly popular articles are in section:")
ls4=[]
for sectioncount in weeklydoc:
    ls4.append(sectioncount)

weeklysectioncount = pd.DataFrame(ls4)
print(weeklysectioncount)
create_plot(weeklysectioncount,"Weekly Sections","Number of popular articles") 


#Query to get the count of each section on monthly basis

monthlydoc = collection.aggregate(
    [{
        "$match":{
            "frequency" : "monthly"}},
         {"$group": 
             {"_id":"$section",
              "total" : {"$sum":1}
            }
    }]
)

print("Monthly popular articles are in section:")
ls5=[]
for sectioncount in monthlydoc:
    ls5.append(sectioncount)

monthlysectioncount = pd.DataFrame(ls5)
print(monthlysectioncount)
create_plot(monthlysectioncount,"Monthly Sections","Number of popular articles") 