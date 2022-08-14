#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:50:40 2021

@author: lamberts_888
"""
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import gaussian_filter

from mplsoccer import Pitch, VerticalPitch, FontManager
from mplsoccer.statsbomb import read_event, EVENT_SLUG

text_color = 'w'

df = pd.read_csv("WH.csv")

df = df[df['result']=='Goal'].reset_index()

pitch = VerticalPitch(pitch_type='opta', pad_bottom=0.5, pad_top=5, pitch_color='#22312b',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_alpha=0.8)

#df['y'] = df['y'].apply(lambda x: x*-1)
#df.loc[:,'y'] *= -1
df['y'] = df['y'].multiply(-1)
df['y'] = df['y'] + 200
df['y'] = df['y'].multiply(1/2)


df

fig, ax = pitch.draw(figsize=(15, 8))
fig.set_facecolor('#22312b')

bin_statistic = VerticalPitch.bin_statistic(df.x, df.y, statistic='count', bins=(25, 25))
bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
pcm = pitch.heatmap(bin_statistic, ax=ax, cmap='hot', edgecolors='#22312b')
# Add the colorbar and format off-white
cbar = fig.colorbar(pcm, ax=ax, shrink=0.6)
cbar.outline.set_edgecolor('#efefef')
cbar.ax.yaxis.set_tick_params(color='#efefef')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#efefef')

plt.gca().invert_yaxis()