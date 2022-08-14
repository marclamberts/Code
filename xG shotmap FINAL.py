#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:55:18 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch

text_color = 'w'

df = pd.read_csv("sonagf.csv")


df = df.loc[(df['team_id']==8487)].reset_index()

#df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

pitch = VerticalPitch(pitch_type='uefa', pad_bottom=0.5, pad_top=5, pitch_color='#22312b',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

df

fig, ax = pitch.draw(figsize=(15, 8))
fig.set_facecolor('#22312b')

#Used ax.text instead of plt.text so that you can arrange the title flexibly. Just play with the coordinates
ax.text(25, 120, 'Sønderjyske', color='white', size=20, fontname="Times New Roman")

#The next 3 lines are used to plot the legend for chance probability based on xG (Just to show what sizes demonstrate)
ax.text(17, 114, "Low xG", color="white", size=14, fontname="Times New Roman")
ax.scatter([32, 42, 52, 62], [114.5]*4, s=[i for i in range(50, 201, 50)], color="grey", 
                edgecolor="grey", clip_on=False)
ax.text(67, 114, "High xG", color="white", size=14, fontname="Times New Roman")

#The next 4 lines are used to get the type of shots legend (Shot, Goal & Shot on Target)
ax.scatter([36, 52, 79], [107.5]*3, s=200, color=["grey", "red", "blue"], clip_on=False)
ax.text(27, 107, "Shot", color="white", size=14, fontname="Times New Roman")
ax.text(43, 107, "Goal", color="white", size=14, fontname="Times New Roman")
ax.text(59, 107, "Shot on Target", color="white", size=14, fontname="Times New Roman")

for x in range(len(df['x'])):
    if df['event_type'][x] == 'Goal':
        plt.scatter(df['y'][x],df['x'][x],color='red', s=df['expected_goals'][x]*400,alpha=.9, zorder=2)
    if df['event_type'][x] == 'Miss':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=df['expected_goals'][x]*400,alpha=.9, zorder=2)
    if df['event_type'][x] == 'AttemptSaved':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=df['expected_goals'][x]*400,alpha=.9, zorder=2)
    if df['event_type'][x] == 'Post':
        plt.scatter(df['y'][x],df['x'][x],color='grey', s=df['expected_goals'][x]*400,alpha=.9, zorder=2)

plt.gca().invert_xaxis()

plt.savefig('Linköping2.png',dpi=500,bbox_inches = 'tight',facecolor='#22312b')