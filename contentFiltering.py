import pandas as pd
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

df2 = pd.read_csv('final.csv')
df2 = df2[df2['soup'].notna()]

count=CountVectorizer(stop_words='english')
count_matrix=count.fit_transform(df2['soup'])

cosine_sim=cosine_similarity(count_matrix,count_matrix) 

df2=df2.reset_index()
indexsis=pd.Series(df2.index, index=df2['title'])

def get_recommendation(title,cosine_sim):
  i=indexsis[title]
  scores=list(enumerate(cosine_sim[i]))
  scores=sorted(scores,key=lambda x:x[1],reverse=True)
  scores=scores[1:11]
  movie_index=[i[0] for i in scores]
  return df2 ['title_x', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview'].iloc[movie_index].values.tolist()
