# Import gensim packages and libraries 
from gensim.summarization import keywords 

# Import user packages and libraries 
from mongoConnect import get_count_groupby_author, get_count_groupby_section, get_newsWire_data

# Import visualization packages and libraries 
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# % matplotlib inline
import seaborn as sns

# Find keywords from text
def get_keywords(t):
    k = keywords(t, words=2, lemmatize=True)
    return k

# Create and generate a word cloud image
def create_wordcloud(text):
    wc = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    # Display the generated image:
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def create_plot(df,x_label,y_label):
    # Bar plot 
    plt.figure(figsize=(15,10))
    df.sort_values(by="total",ascending=False).plot.bar(x='_id',y='total')
    plt.xticks(rotation=50)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

if __name__ == '__main__':
    
    count_section = get_count_groupby_section()
    ls_section = []
    for each in count_section:
        ls_section.append(each)
    df_section = pd.DataFrame(ls_section,index=None)
    print('Counts by News Section :')
    print(df_section)
    # Bar plot of News Section vs article count
    create_plot(df_section, "News Section", "Number of articles")
    
    ls_author = []
    count_author = get_count_groupby_author()
    for each in count_author:
        ls_author.append(each)
    df_author = pd.DataFrame(ls_author,index=None)
    print('Counts by Author')
    print(df_author)

    # Bar plot of authors vs article count
    create_plot(df_author, "Author", "Number of articles")
    
    data = get_newsWire_data()

    section=''
    key_words=''

    d = []
    for each in data:
        section = section+" "+each['section']
        kw = get_keywords(each['abstract'])
        key_words = key_words+" "+kw
        d.append(each)

    # Convert data list into dataframe
    df_data = pd.DataFrame(d,index=None)  
    print(df_data.head())

    # Create and generate a word cloud image
    create_wordcloud(section)
    create_wordcloud(key_words)