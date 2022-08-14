#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:41:38 2021

@author: lamberts_888
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib as mpl
from mplsoccer.pitch import Pitch
from scipy import stats

df = pd.read_csv('norwich.csv')
df = df.fillna(0)

#convert the x and y values to the size of the pitch we will use (120,80)
df['y'] = df['y']
df['x'] = df['x']

#filter for the team we want and reset the index so that we can use for loops over it
df = df[df['teamId']==168].reset_index()

#the player ids are technically floats so we want to change those to ints
df['playerId'] = df['playerId'].astype(int) 

#Get a list of the unique player ids if you just want the starters, get a list of the first 11.
#it is 11 because it goes down the column so the first 11 will be the starters 
#unless someone is subbed off in like the first 5 minutes
players = df['playerId'].unique()
starters = players[0:11]
#you can sort them if you want
starters.sort()

#set up the pitch
fig, ax = plt.subplots(figsize=(13,8.5))
fig.set_facecolor('#000000')
ax.patch.set_facecolor('#000000')

pitch = Pitch(pitch_type='opta', orientation='vertical',
              pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=False, tight_layout=True)

pitch.draw(ax=ax)
plt.gca().invert_yaxis()

#Create a new data frame for the player and filter for only passes
df1 = df[df["playerId"]==362103]
df1 = df1[df1['type/value']==1]

#filter that dataframe to exclude outliers. Anything over a z score of 2 will be excluded for the data points
df1 = df1[(np.abs(stats.zscore(df1[['x','y']])) < 3)]

#Create an array of the x/y coordinate groups
points = df1[['x', 'y']].values

#Create the convex hull
hull = ConvexHull(df1[['x','y']])

#plot the pass locations
plt.scatter(df1.x,df1.y)

#Loop through each of the hull's simplices
for i in hull.simplices:
    #Draw a black line between each
    plt.plot(points[i, 0], points[i, 1], 'white')
    plt.fill(points[hull.vertices,0], points[hull.vertices,1], c='white', alpha=0.01)
    
    plt.title('Max Aarons Convex Hull vs Coventry City',color='white',size=20)