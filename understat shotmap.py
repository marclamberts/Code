#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:25:24 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'

df = pd.read_excel('LIGT3.xlsx')
#df = df.loc[(df['player']=='Tammy Abraham')].reset_index()

df

#pitch = VerticalPitch(pitch_type='opta', orientation='vertical',pitch_color='#000000', line_color='#c7d5cc', figsize=(13, 8),constrained_layout=False, tight_layout=True, view='half')

df['X'] = df['X'] * 120
df['Y'] = df['Y'] * 80

pitch = VerticalPitch(pitch_type='statsbomb', pad_bottom=0.5, pad_top=5, pitch_color='#000000', line_color='#c7d5cc',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

fig, ax = pitch.draw()
fig.set_facecolor('#000000')


for x in range(len(df['X'])):
    if df['result'][x] == 'Goal':
       plt.scatter(df['Y'][x], df['X'][x], color='red', s=df['xG'][x]*300, alpha=.9)
    if df['result'][x] == 'SavedShot':
        plt.scatter(df['Y'][x], df['X'][x], color='grey', marker='o',  s=df['xG'][x]*300, alpha=.9)
    if df['result'][x] == 'MissedShots':
       plt.scatter(df['Y'][x], df['X'][x], color='grey', marker='o', s=df['xG'][x]*300, alpha=.9) 
    if df['result'][x] == 'ShotOnPost':
        plt.scatter(df['Y'][x], df['X'][x], color='grey', marker='o', s=df['xG'][x]*300, alpha=.9)
    if df['result'][x] == 'BlockedShot':
        plt.scatter(df['Y'][x], df['X'][x], color='grey', s=df['xG'][x]*300, alpha=.9)


        
        
plt.gca().invert_xaxis()

#ArithmeticErrorfig.text(.60,.08,f'@lambertsmarc',fontstyle='italic',fontsize=8,fontfamily='Andale Mono',color='#c7d5cc')
#fig.text(.40,0.005,f'@lambertsmarc / twitter',fontstyle='italic',fontsize=14,fontfamily='Andale Mono', color='w')

        
#rect=patches.Rectangle(
#xy=(37,67), width=26, height=16, fc='red', alpha=0.2)
#ax.add_patch(rect)
#style="Simple, tail_width-=0,5, head_width=4, head_length=10"

#plt.title('Marco Richter - Hertha BSC 21-22\nGoals:5\n xG 3,81',fontfamily='Andale Mono', color='#c7d5cc',size=15)
plt.savefig('LIGT.png',dpi=1500,bbox_inches = 'tight',facecolor='#000000')