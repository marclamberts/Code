#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:38:40 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'

df = pd.read_excel('Lin2.xlsx')


#df = df.loc[(df['playerId']==69517)].reset_index()

#df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

pitch = VerticalPitch(pitch_type='opta', pad_bottom=0.5, pad_top=5, pitch_color='#22312b',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

fig, ax = pitch.draw()
fig.set_facecolor('#22312b')


for x in range(len(df['X'])):
    if df['Event'][x] == 'Shot':
        plt.scatter(df['Y'][x],df['X'][x],color='grey', s=df['xG'][x]*500,alpha=.9)
    if df['Event'][x] == 'Goal':
        plt.scatter(df['Y'][x],df['X'][x],color='red', s=df['xG'][x],alpha=.9)
    if df['Event'][x] == 'Shot on target':
        plt.scatter(df['Y'][x],df['X'][x],color='blue', s=df['xG'][x],alpha=.9)

rect=patches.Rectangle(
xy=(37,67), width=26, height=16, fc='red', alpha=0.5)
ax.add_patch(rect)
style="Simple, tail_width-=0,5, head_width=4, head_length=10"

        
plt.gca().invert_xaxis()
    
plt.title('Linköping shots vs AIK',color='white',size=18)

plt.savefig('Linköping2.png',dpi=500,bbox_inches = 'tight',facecolor='#22312b')