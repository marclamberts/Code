#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 02:15:47 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'

df = pd.read_csv('01-09-Apr-22-EveMan-event.csv')
df = df.loc[(df['PlayerId']==300299)].reset_index()

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


for x in range(len(df['x'])):
    if df['type/displayName'][x] == 'Goal':
        plt.scatter(df['y'][x],df['x'][x],color='red', s=70,alpha=.9, zorder=2)
    if df['type/displayName'][x] == 'SavedShot':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=70,alpha=.9, zorder=2)
    if df['type/displayName'][x] == 'MissedShots':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=70,alpha=.9, zorder=2)
    if df['type/displayName'][x] == 'ShotOnPost':
        plt.scatter(df['y'][x],df['x'][x],color='grey', s=70,alpha=.9, zorder=2)
        


#fig.text(.60,.08,f'@lambertsmarc/ twitter',fontstyle='italic',fontsize=8,fontfamily='Andale Mono',color='white')


        
        
#plt.gca().invert_xaxis()
        
#rect=patches.Rectangle(
#xy=(37,67), width=26, height=16, fc='red', alpha=0.2)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

#plt.title('Shot map Mats Seuntjens',fontfamily='Andale Mono', color='white',size=15)
plt.savefig('redan.png',dpi=1500,bbox_inches = 'tight',facecolor='white')