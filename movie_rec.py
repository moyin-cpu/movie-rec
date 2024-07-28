import pandas as pd
import sklearn as sk
import numpy as np
import scipy as sp
import matplotlib as plt
import requests #used to request APIs
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json #used to change data and web data/apis- representing structured data based on java
#%%


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGY0NmNmNmMxNTZkNTUwNTgxNjViYjcwZDU3N2M4MSIsIm5iZiI6MTcyMjIwNDQxNy4xOTU4NTQsInN1YiI6IjY2YTZhNzI2MTdkMmNhMmQ5MjY1ZWY3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OWT3SWZ0Yo9W68LFekUs10IOFAyyxTapA4GlC2S6Q3Y"
}
#heders is disctionary of http headers to send with request


movie_genre = requests.get( "https://api.themoviedb.org/3/genre/movie/list?language=en", headers=headers)
#print(movie_genre.status_code) #200 = everything ok
#print(movie_genre.text)


#turn into csv- need as a data frame!
movie_genre_data = movie_genre.text #gives it as a text
json_mgd = movie_genre.json()
df = pd.DataFrame(json_mgd['genres'])


analyzer = SentimentIntensityAnalyzer()

def get_sentiment(data):
    scores = analyzer.polarity_scores(data)
    sentiment = 1 if scores['pos'] > 0 else 0
    return sentiment
df['sentiment'] = df['name'].apply(get_sentiment)

print(df)


#matching id to movie

url = "https://api.themoviedb.org/3/movie/movie_id?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGY0NmNmNmMxNTZkNTUwNTgxNjViYjcwZDU3N2M4MSIsIm5iZiI6MTcyMjIwNDQxNy4xOTU4NTQsInN1YiI6IjY2YTZhNzI2MTdkMmNhMmQ5MjY1ZWY3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OWT3SWZ0Yo9W68LFekUs10IOFAyyxTapA4GlC2S6Q3Y"
}

response = requests.get(url, headers=headers)

print(response.text)
# movie_title = movie_genre.text #gives it as a text
# json_mgd = movie_genre.json()
# df[] = pd.DataFrame(json_mgd['genres'])