import tweepy
from textblob import TextBlob
import  numpy as np
import pandas as pd
import re
import pandas as pd
import matplotlib.pyplot as plt
import sys

Positive=0
Negative=0
Neutral=0
def cleanText(text):
    global Positive,Negative,Neutral
    text=re.sub(r'RT @[\w]*:',"",text)
    text = re.sub('#', '', text)
    text=re.sub(r'@[\w]*',"",text)
    text=re.sub(r'https?://[A-Za-z0-9./]*','',text)
    text=re.sub('\n','',text)
    tb= TextBlob(text)
    if(tb.sentiment.polarity>0): #-1 0 1
        Positive+=1
    elif(tb.sentiment.polarity<0):
        Negative+=1
    else:
        Neutral+=1

    #print(str(i) + ". " + text)
    return text

hero-field=input("Enter the Keyword : ") #Search topic
consumer_key='Aj6xXyi8K5h2VY0v4kH689HU8'
consumer_secret='lsDauVmn0Y5ilrrEEZDrPPYJgdjtIQw2DvuBemjlEoCHCNF8zi'

access_token='1328731514402713601-oIrA6RLGai6MUvYdxY6piGVoIhV1QD'
access_token_secret='yY8W5DlQtWDMYmA5y11oLFTnZBSGMYE8yQlzvitbgENCm'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth,wait_on_rate_limit=True)
Date_since='2020-09-1'# date
public_tweets=tweepy.Cursor(api.search,q=search_word,lang='en',date_since=Date_since).items(500)
tweet_details=[[tweet.text,tweet.user.location,tweet.created_at] for tweet in public_tweets]
df=pd.DataFrame(data=tweet_details,columns=['Tweets','Location','Time'])

l=len(df.index)
print(df.head(l-1))
df['Tweets']=df['Tweets'].apply(cleanText)
#print(df['Location']);
Agree=(Positive/l)*100
Disagree=(Negative/l)*100
Neutral=(Neutral/l)*100
print('Positive:',round(Agree,2),"%")
print('Negative:',round(Disagree,2),"%")
print('Neutral:',round(Neutral,2),"%")
print(df['Time'][1])

names = ['Positive', 'Negative', 'Neutral']
values = [Agree,Disagree , Neutral]
plt.ylim(0,100)
plt.bar(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
