#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:42:20 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'

df = pd.read_csv('eredivisie34.csv')
df = df.loc[(df['PlayerId']==345303)].reset_index()
df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

pitch = VerticalPitch(pitch_type='opta', pad_bottom=0.5, pad_top=5, pitch_color='white', line_color='black',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

fig, ax = pitch.draw()
fig.set_facecolor('white')


for x in range(len(df['x'])):
    if df['type/displayName'][x] == 'Goal':
        plt.scatter(df['y'][x],df['x'][x],color='red', s=70,alpha=.9, zorder=3)
    if df['type/displayName'][x] == 'SavedShot':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=70,alpha=.9, zorder=2)
    if df['type/displayName'][x] == 'MissedShots':
        plt.scatter(df['y'][x],df['x'][x],color='grey', marker='x', s=70,alpha=.9, zorder=2)
    if df['type/displayName'][x] == 'ShotOnPost':
        plt.scatter(df['y'][x],df['x'][x],color='grey',marker='o', s=70,alpha=.9, zorder=2)
        
#plt.suptitle('Antony - Ajax',color='black',size=20)


fig.text(.60,.08,f'@lambertsmarc',fontstyle='italic',fontsize=8,fontfamily='Andale Mono',color='black')


        
        
#plt.gca().invert_xaxis()
        
#rect=patches.Rectangle(
#xy=(37,67), width=26, height=16, fc='red', alpha=0.2)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

#plt.title('Goals: 21',fontfamily='Andale Mono', color='black',size=15)
plt.savefig('redan.png',dpi=500,bbox_inches = 'tight',facecolor='white')