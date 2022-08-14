#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:29:01 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
from mplsoccer.pitch import VerticalPitch
import seaborn as sns
from matplotlib import patches
import numpy as geek
import numpy as np


df = pd.read_excel('wales.xlsx')

df = df.loc[(df['playerId']==5)].reset_index()

#final third passes

#right half space
#df = df.loc[(df['x']>=50)]
#df = df.loc[(df['x']<=80)]
#df = df.loc[(df['y']<=35)]
#df = df.loc[(df['y']>=25)]

#left half space
#df = df.loc[(df['x']>=50)]
#df = df.loc[(df['y']<=75)]
#df = df.loc[(df['y']>=65)]

df = df[df['type/displayName']=='Pass'].reset_index()


df['x'] = df['x']
df['y'] = df['y']
df['xend'] = df['endX']
df['yend'] = df['endY']
df['startpass'] = geek.sqrt((np.square(df['x']-100))+(np.square(df['y']-50)))
df['endpass'] = geek.sqrt((np.square(df['endX']-100))+(np.square(df['endY']-50)))
df['progressive pass'] = -(df['endpass']-df['startpass'])/df['startpass']

df['progressive pass']>0.25

df

fig ,ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')


#this is how we create the pitch
pitch = VerticalPitch(pitch_type='opta', positional=True, positional_color='#eadddd', orientation='vertical',
              pitch_color='#22312b', line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=False, tight_layout=True, half=False)

#Draw the pitch on the ax figure as well as invert the axis for this specific pitch
pitch.draw(ax=ax)
#plt.gca().invert_yaxis()
#plt.gca().invert_xaxis()

#use a for loop to plot each pass
for x in range(len(df['x'])):
    if df['outcomeType/displayName'][x] == 'Successful':
        #on here you have the parenthesis around the arguments which will essentially make it be missing some values. 
        # if you remove those like below it should work.You also need to add ax=ax at the end so it plots correctly.
        #pitch.arrows((df['x'][x],df['y'][x]),(df['xend'][x],df['yend'][x]),color='green')
        #pitch.arrows(df['x'][x],df['y'][x],color='green')
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2,
             headwidth=10, headlength=10, zorder=2, color='#ad993c',ax=ax)
    if df['outcomeType/displayName'][x] == 'Unsuccessful':
        #same thing here with the 
        #pitch.arrows((df['xend'][x],df['x'][x]),(df['yend'][x],df['y'][x]),color='red')
        #plt.scatter(df['x'][x],df['y'][x],color='red')
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2,
             headwidth=10, headlength=10, color='#ba4f45',ax=ax)