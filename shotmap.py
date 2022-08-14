#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:05:31 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'

df = pd.read_excel('Joey Veerman.xlsx')
df1 = pd.read_excel('Joey Veerman 2.xlsx')
#df = df.loc[(df['playerId']==361897)].reset_index()

df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

pitch = VerticalPitch(pitch_type='opta', pad_bottom=0.5, pad_top=5, pitch_color='#22312b',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

fig, ax = pitch.draw()
fig.set_facecolor('#22312b')


for x in range(len(df['x'])):
    if df['type/displayName'][x] == 'Goal':
        plt.scatter(df['y'][x],df['x'][x],color='red', s=50,alpha=.9, zorder=2)
    if df['type/displayName'][x] == 'SavedShot':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=50,alpha=.7, zorder=2)
    if df['type/displayName'][x] == 'MissedShots':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=50,alpha=.7, zorder=2)
    if df['type/displayName'][x] == 'ShotOnPost':
        plt.scatter(df['y'][x],df['x'][x],color='grey', s=50,alpha=.7, zorder=2)

for x in range(len(df1['x'])):
    if df1['type/displayName'][x] == 'Goal':
        plt.scatter(df['y'][x],df1['x'][x],color='red', s=50,alpha=.9, zorder=2)
    if df1['type/displayName'][x] == 'SavedShot':
        plt.scatter(df['y'][x],df1['x'][x],color='grey',s=50,alpha=.7, zorder=2)
    if df1['type/displayName'][x] == 'MissedShots':
        plt.scatter(df['y'][x],df1['x'][x],color='grey',s=50,alpha=.7, zorder=2)
    if df1['type/displayName'][x] == 'ShotOnPost':
        plt.scatter(df['y'][x],df1['x'][x],color='grey', s=50,alpha=.7, zorder=2)
        
        
plt.gca().invert_xaxis()
        
#rect=patches.Rectangle(
#xy=(37,67), width=26, height=16, fc='red', alpha=0.2)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

plt.title('Shot map Joey Veerman 2021/2022',color='white',size=15)
plt.savefig('NM13.png',dpi=1000,bbox_inches = 'tight',facecolor='#22312b')