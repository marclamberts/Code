#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:38:44 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
from mplsoccer.pitch import VerticalPitch
import seaborn as sns

from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from PIL import Image
from highlight_text import ax_text

from mplsoccer import Pitch, add_image, FontManager
from mplsoccer.statsbomb import read_event, EVENT_SLUG

df = pd.read_csv('Eredivisie.csv')
df = df.loc[(df['PlayerId']==355870)].reset_index()
df = df.loc[(df['x']>=70)]
#df = df.loc[(df['x']<=100)]
#df1 = pd.read_csv('milbou.csv')
#df2 = pd.read_csv('milbou.csv')


#df = df.loc[(df['teamId']==183)].reset_index()
#df1 = df1.loc[(df1['teamId']==183)].reset_index()
#df2 = df2.loc[(df2['teamId']==183)].reset_index()

#df = df[df['result']=='Goal'].reset_index()
#df = df[df['result']=='Shots on target'].reset_index()
#df2 = df2[df2['type/displayName']=='MissedShots'].reset_index()

#df['y'] = df['y'].multiply(-1)
#df['y'] = df['y'] + 200
#df['y'] = df['y'].multiply(1/2)

df = df[df['type/displayName']=='Pass'].reset_index()


df




pitch = VerticalPitch(pitch_type='opta', line_color='white', line_zorder=2, pitch_color='#000000', half=False)
fig, ax = pitch.draw(figsize=(4.4, 6.4))
hexmap = pitch.hexbin(df.x, df.y, ax=ax, edgecolors='#f4f4f4',
                      gridsize=(16, 16), cmap='Wistia')
#hexmap = pitch.hexbin(df1.x, df1.y, ax=ax, edgecolors='#f4f4f4',
   #                   gridsize=(20, 20), cmap='Blues')
#hexmap = pitch.hexbin(df2.x, df2.y, ax=ax, edgecolors='#f4f4f4',
    #                  gridsize=(20, 20), cmap='Reds')

fig.set_facecolor('#000000')
#plt.title('Hamer Ball Recovery map',color='white',size=18)
fig.text(.25,0.01,f'@lambertsmarc / twitter',fontstyle='italic',fontsize=14,fontfamily='Andale Mono', color='w')
#plt.gca().invert_xaxis()