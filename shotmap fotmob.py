#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:25:36 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'

df = pd.read_csv('columbuscrewnewenglandrevolution.csv', encoding = 'unicode_escape')
df = df.loc[(df['team_id']==6001)].reset_index()
#df = df.loc[(df['team_id']==5814)].reset_index()

df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

pitch = VerticalPitch(pitch_type='uefa', pad_bottom=0.5, pad_top=5, pitch_color='#22312b', line_color='white',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

fig, ax = pitch.draw()
fig.set_facecolor('#22312b')


for x in range(len(df['x'])):
    if df['event_type'][x] == 'Goal':
        plt.scatter(df['y'][x],df['x'][x],color='red', s=df['expected_goals'][x]*600,alpha=.9, zorder=3)
    if df['event_type'][x] == 'Miss':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=df['expected_goals'][x]*600,alpha=.9, zorder=2)
    if df['event_type'][x] == 'AttemptSaved':
        plt.scatter(df['y'][x],df['x'][x],color='grey',s=df['expected_goals'][x]*600,alpha=.9, zorder=2)
    if df['event_type'][x] == 'Post':
        plt.scatter(df['y'][x],df['x'][x],color='grey', s=df['expected_goals'][x]*600,alpha=.9, zorder=2)
        

ax.set_title("Columbus Crew Shot map vs NER", fontsize=18, color="w", fontfamily="Andale Mono", fontweight='bold', pad=8)

#fig.text(.60,.08,f'@lambertsmarc',fontstyle='italic',fontsize=8,fontfamily='Andale Mono',color='white')


        
        
#plt.gca().invert_xaxis()
        
#rect=patches.Rectangle(
#xy=(37,67), width=26, height=16, fc='red', alpha=0.2)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

#plt.title('Shot map Mats Seuntjens',fontfamily='Andale Mono', color='white',size=15)
plt.savefig('vsNER.png',dpi=1500,bbox_inches = 'tight',facecolor='#22312b')