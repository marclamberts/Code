#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 02:03:46 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
from mplsoccer.pitch import VerticalPitch
import seaborn as sns
from matplotlib import patches
df = pd.read_csv('01-10-Apr-22-PSVRKC-event.csv')


df = df.loc[(df['PlayerId']==382556)].reset_index()

#final third passes
#df = df.loc[(df['x']>=50)]

#df = df.loc[(df['x']<=60)]


df = df[df['type/displayName']=='Pass'].reset_index()


df['x'] = df['x']
df['y'] = df['y']
df['xend'] = df['endX']
df['yend'] = df['endY']



df

fig ,ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('white')
ax.patch.set_facecolor('white')


#this is how we create the pitch
pitch = VerticalPitch(pitch_type='opta', orientation='vertical',
              pitch_color='white', line_zorder=3, line_color='black', figsize=(13, 8),
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

        
        
        
#plt.suptitle('Passmap Kökcü vs AZ',color='white',size=25)