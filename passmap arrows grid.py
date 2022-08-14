#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:54:05 2021

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

df = df.loc[(df['playerId']==366166)].reset_index()
df1 = df1.loc[(df1['playerId']==366166)].reset_index()
df2 = df2.loc[(df2['playerId']==366166)].reset_index()

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


cmap_dict = cmr.cm.cmap_cd
all_cmap_dict = {}
for cmap_type_key in cmap_dict:
    for key, cmap in cmap_dict[cmap_type_key].items():
        if key[-2:] != '_r':
            all_cmap_dict[key] = cmap

pearl_earring_cmap = LinearSegmentedColormap.from_list("Pearl Earring - 100 colors",
                                                       ['#15242e', '#4393c4'], N=100)

fig, axs = plt.subplots(nrows=1, ncols=3,figsize=(20,12), facecolor="#FDFDFD")
ax = fig.get_axes()
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
pitch= VerticalPitch(line_color ='#121212', line_zorder=2, figsize=(8.4, 10.4), orientation='vertical', pitch_color='#FDFDFD',pad_top=15, pad_bottom=15)

for count, ax in enumerate(fig.get_axes()):
    pitch.draw(ax=ax)
    ax.set_facecolor("#FDFDFD")
    if count == 0:
        for x in range(len(df['x'])):
            if df['outcomeType/displayName'][x] == 'Successful':
        #on here you have the parenthesis around the arguments which will essentially make it be missing some values. 
        # if you remove those like below it should work.You also need to add ax=ax at the end so it plots correctly.
        #pitch.arrows((df['x'][x],df['y'][x]),(df['xend'][x],df['yend'][x]),color='green')
        #pitch.arrows(df['x'][x],df['y'][x],color='green')
                pitch.arrows(df['x'][x],df['y'][x],df['endX'][x],df['endY'][x],width=2,
             headwidth=10, headlength=10, color='#ad993c',ax=ax)
            if df['outcomeType/displayName'][x] == 'Unsuccessful':
        #same thing here with the 
        #pitch.arrows((df['xend'][x],df['x'][x]),(df['yend'][x],df['y'][x]),color='red')
        #plt.scatter(df['x'][x],df['y'][x],color='red')
                pitch.arrows(df['x'][x],df['y'][x],df['xend'][x],df['yend'][x],width=2,
             headwidth=10, headlength=10, color='#ba4f45',ax=ax)
        
    if count == 1:
        kde_after = pitch.kdeplot(df1.x, df1.y, ax=ax,
                          shade=True, levels=100, shade_lowest=True,
                          cut=4, cmap='Blues')
    if count == 2:
        kde_after1 = pitch.kdeplot(df2.x, df2.y, ax=ax,
                          shade=True, levels=100, shade_lowest=True,
                          cut=4, cmap='Blues')