#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:01:59 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'

df = pd.read_excel('Robson.xlsx')
#df = df.loc[(df['PlayerId']==236544)].reset_index()

df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

pitch = VerticalPitch(pitch_type='opta', pad_bottom=0.5, pad_top=5, pitch_color='#15242e', line_color='#c7d5cc',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

fig, ax = pitch.draw()
fig.set_facecolor('#15242e')


for x in range(len(df['X'])):
    if df['Event'][x] == 'Goal':
        plt.scatter(df['Y'][x],df['X'][x],color='red', s=30, marker='o', alpha=1, zorder=2)
    if df['Event'][x] == 'Shot off Target':
        plt.scatter(df['Y'][x],df['X'][x],color='orange', s=30, marker='x', alpha=.9, zorder=2)
    if df['Event'][x] == 'Shot on Target':
        plt.scatter(df['Y'][x],df['X'][x],color='blue', s=30, marker='v', alpha=.9, zorder=2)
   
        


#fig.text(.60,.08,f'@lambertsmarc/ twitter',fontstyle='italic',fontsize=8,fontfamily='Andale Mono',color='#302a75')


        
        
plt.gca().invert_xaxis()
        
#rect=patches.Rectangle(
#xy=(37,67), width=26, height=16, fc='red', alpha=0.2)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

#plt.title('Shot map Charlotte Potts - Sunderland Ladies',fontfamily='Andale Mono', color='#c7d5cc',size=15)
plt.savefig('KWshot.png',dpi=1500,bbox_inches = 'tight',facecolor='#15242e')