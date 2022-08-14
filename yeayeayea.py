#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:57:05 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
from mplsoccer.pitch import Pitch
import seaborn as sns
from matplotlib import patches
df = pd.read_excel('MC2.xlsx')

#df = df.loc[(df['teamId']==212)].reset_index()

#final third passes
#df = df.loc[(df['x']>=70)]
#df = df.loc[(df['x']<=60)]


#df = df[df['type/displayName']=='Pass'].reset_index()


df['x'] = df['x']
df['y'] = df['y']
df['xend'] = df['endX']
df['yend'] = df['endY']

df

fig ,ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')


#this is how we create the pitch
pitch = Pitch(pitch_type='opta', orientation='vertical',
              pitch_color='#22312b', line_zorder=2, line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=False, tight_layout=True)

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
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2, zorder=2,
             headwidth=10, headlength=10, color='#ad993c',ax=ax)
    if df['outcomeType/displayName'][x] == 'Unsuccessful':
        #same thing here with the 
        #pitch.arrows((df['xend'][x],df['x'][x]),(df['yend'][x],df['y'][x]),color='red')
        #plt.scatter(df['x'][x],df['y'][x],color='red')
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2, zorder=2,
             headwidth=10, headlength=10, color='#ba4f45',ax=ax)

#rect=patches.Rectangle(
#xy=(63,0.3), width=17, height=100, fc='red', alpha=0.3)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

#rect=patches.Rectangle(
#xy=(20,0.3), width=17, height=100, fc='red', alpha=0.3)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

        
        
        
plt.suptitle('Matty Cash throw ins, Aston Villa - first 7 PL games',color='white',size=25)