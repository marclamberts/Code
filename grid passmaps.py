#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 19:44:54 2021

@author: lamberts_888
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
import cmasher as cmr

from mplsoccer import VerticalPitch
from mplsoccer.statsbomb import read_event, EVENT_SLUG
from mplsoccer.utils import FontManager
import seaborn as sns

df = pd.read_csv('plybla.csv')
df1 = pd.read_csv('plywim.csv')
df2 = pd.read_csv('milply.csv')
df3 = pd.read_csv('shrply.csv')

df = df.loc[(df['playerId']==366166)].reset_index()
df1 = df1.loc[(df1['playerId']==366166)].reset_index()
df2 = df2.loc[(df2['playerId']==366166)].reset_index()
df3 = df3.loc[(df3['playerId']==366166)].reset_index()

df

df['x'] = df['x']
df['y'] = df['y']
df['endX'] = df['endX']
df['endY'] = df['endY']

df1['x'] = df1['x']
df1['y'] = df1['y']
df1['endX'] = df1['endX']
df1['endY'] = df1['endY']

df2['x'] = df2['x']
df2['y'] = df2['y']
df2['endX'] = df2['endX']
df2['endY'] = df2['endY']

df3['x'] = df3['x']
df3['y'] = df3['y']
df3['endX'] = df3['endX']
df3['endY'] = df3['endY']


ax = ax
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
pitch= VerticalPitch(line_color ='#121212', line_zorder=2, figsize=(8.4, 10.4), orientation='vertical', pitch_color='#FDFDFD', pad_top=15, pad_bottom=15)

for count, ax in enumerate(fig.get_axes()):
    pitch.draw(ax=ax)
    ax.set_facecolor("#FDFDFD")
    if count == 0:
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2,
             headwidth=10, headlength=10, color='#ad993c',ax=ax)
        
        pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2,
             headwidth=10, headlength=10, color='#ad993c',ax=ax)
    if count == 1:
        kde_after = pitch.kdeplot(df1.x, df1.y, ax=ax,
                          shade=True, levels=100, shade_lowest=True,
                          cut=4, cmap='Blues')
    
        
