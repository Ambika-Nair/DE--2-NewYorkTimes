import spacy
from spacy.lang.en.examples import sentences 
import tomotopy as tp
from multiprocessing.managers import BaseManager
from bertopic import BERTopic
from databaseoperations import db, collection
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string


x = db.collection.find({},{"results":{"abstract":1}})

list_cur = list(x)


list2 = list_cur[0]['results']


list = []

for i in range(2,25 ):
    list.append(list2[i]['abstract'])



# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

string = listToString(list)

nlp = spacy.load("en_core_web_sm")

def clean_up(text):
    removal=['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE']
    text_out = []
    doc= nlp(text)
    for token in doc:
        if token.is_stop == False and token.is_alpha and len(token)>2 and token.pos_ not in removal:
            lemma = token.lemma_
            text_out.append(lemma)
    return text_out

content1 = remove_stopwords(string)
datalist = clean_up(content1)

topic_model = BERTopic()
topics, probabilities = topic_model.fit_transform(datalist)
print(topic_model.get_topic_info())

# topic_model.visualize_barchart().show()
# topic_model.visualize_hierarchy().show()