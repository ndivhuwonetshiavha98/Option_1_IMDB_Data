#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 04:07:14 2024

@author: ndivhuwo
"""

import pandas as pd

df = pd.read_csv('movie_dataset.csv')

## data cleaning

df.dropna(inplace = True)
df = df.reset_index(drop=True)

### What is the highest rated movie in the dataset? 

highest_rated_movie = df[df['Rating'] == df['Rating'].max()]


print(highest_rated_movie[['Title', 'Rating']])

#### What is the average revenue of all movies in the dataset?

revenue = df['Revenue (Millions)']

revenue_average = sum(revenue)/len(revenue)

print('revenue_average = ',revenue_average)

### What is the average revenue of movies from 2015 to 2017 in the dataset?

# Filter the dataset for movies released from 2015 to 2017
filtered_movies = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

average_revenue_2015_2017 = sum(filtered_movies['Revenue (Millions)'])/len(filtered_movies)
print(average_revenue_2015_2017)


#How many movies were released in the year 2016? 

number_of_movies_2016 = []


for i in df['Year']:
    if i == 2016:
        number_of_movies_2016.append(i)
print(len(number_of_movies_2016),'number of movies released in 2016')

