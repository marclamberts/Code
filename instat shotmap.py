#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:56:27 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import Pitch

text_color = 'w'

df = pd.read_csv("Benteke2.csv")


#df = df.loc[(df['playerId']==69517)].reset_index()

#df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

pitch = Pitch(pitch_type='opta', pad_bottom=0.5, pad_top=5, pitch_color='#22312b',  # pitch extends slightly below halfway line
                      half=False,  # half of a pitch
                      goal_alpha=0.8)

#df['y'] = df['y'].apply(lambda x: x*-1)
#df.loc[:,'y'] *= -1
df['y'] = df['y'].multiply(-1)
df['y'] = df['y'] + 202
df['y'] = df['y'].multiply(1/2)


df

fig, ax = pitch.draw(figsize=(15, 8))
fig.set_facecolor('#22312b')

#Used ax.text instead of plt.text so that you can arrange the title flexibly. Just play with the coordinates
#ax.text(30, 120, 'Linköping shots vs Kristianstad', color='white', size=20, fontname="Times New Roman")


for x in range(len(df['x'])):
    if df['result'][x] == 'Goal':
        plt.scatter(df['y'][x], df['x'][x], color='red', s=df['xG'][x]*500, alpha=.9)
    if df['result'][x] == 'Shot on target':
        plt.scatter(df['y'][x], df['x'][x], color='grey', s=df['xG'][x]*500, alpha=.9)
    if df['result'][x] == 'Shot blocked':
        plt.scatter(df['y'][x], df['x'][x], color='grey', s=df['xG'][x]*500, alpha=.9)
    if df['result'][x] == 'Wide shot':
        plt.scatter(df['y'][x], df['x'][x], color='grey', s=df['xG'][x]*500, alpha=.9)

plt.gca().invert_yaxis()
#plt.gca().invert_xaxis()

plt.savefig('WH shot.png',dpi=500,bbox_inches = 'tight',facecolor='#22312b')