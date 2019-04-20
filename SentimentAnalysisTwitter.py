#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis for twitter

# In[14]:


#Import all Dataset
from textblob import TextBlob
import nltk
import tweepy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[15]:


#Check waht TextBlob does
wiki=TextBlob("Naveen is angry as he is not getting any good matches on tinder.")


# In[18]:


#Check the tags associated
wiki.tags


# In[20]:


#check the polarity of the sentiment(>0 'Positive', <0 'Negetive')
wiki.sentiment.polarity


# In[21]:


#To Tokenise the sentiment to create a bag of words attribute
wiki.words


# In[22]:


#Get Consumer key from twitter API
consumer_key='ipQJFmHQMU3dsWgUxuxP5YYEa'
consumer_secret='Lw9t9jLz6GwqcMgzKDq0dbipAKEa6zpo8yYUVehZUiE9YEzff5'


# In[23]:


#Get Access toekn from Twitter API
access_token='1098977535596015617-ycsmfetrXJuszE6XXQy9ytcdqRH41Q'
access_token_secret='Jro4H4Q6slw9aCvwrFQa1L0gEkGYcezEcMosQ5VT1KuZ1'


# In[25]:


#Pass consumer_key and consumer_token to the OAuthHandler of tweepy as a parameter.
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)


# In[26]:


#Set the access token.
auth.set_access_token(access_token,access_token_secret)


# In[27]:


Create an API by the passing the auth 
api=tweepy.API(auth)


# In[28]:


#Find the tweets related to trump.
public_tweets=api.search('Trump')


# In[30]:


#Loop over to check the sentiment polarity
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)

