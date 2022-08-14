#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:05:49 2021

@author: lamberts_888


"""

import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
from mplsoccer.pitch import VerticalPitch
import seaborn as sns

df = pd.read_csv('burhull.csv')

df = df.loc[(df['teamId']==1786)].reset_index()

df = df[df['type/displayName']=='Pass'].reset_index()

df['x'] = df['x']
df['y'] = df['y']
df['xend'] = df['endX']
df['yend'] = df['endY']

df

fig ,ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

#this is how we create the pitch
pitch = VerticalPitch(pitch_type='opta', orientation='vertical',
              pitch_color='#22312b', line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=False, tight_layout=True)

for x in range(len(df['x'])):
    if df['outcomeType/displayName'][x] == 'Successful':
        #on here you have the parenthesis around the arguments which will essentially make it be missing some values. 
        # if you remove those like below it should work.You also need to add ax=ax at the end so it plots correctly.
        #pitch.arrows((df['x'][x],df['y'][x]),(df['xend'][x],df['yend'][x]),color='green')
        #pitch.arrows(df['x'][x],df['y'][x],color='green')
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2,
             headwidth=10, headlength=10, color='#ad993c',ax=ax)
    if df['outcomeType/displayName'][x] == 'Unsuccessful':
        #same thing here with the 
        #pitch.arrows((df['xend'][x],df['x'][x]),(df['yend'][x],df['y'][x]),color='red')
        #plt.scatter(df['x'][x],df['y'][x],color='red')
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2,
             headwidth=10, headlength=10, color='#ba4f45',ax=ax)
        
        