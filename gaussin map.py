#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:20:10 2021

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

df = pd.read_csv('austria.csv')

df['x'] = df['x']
df['y'] = df['y']

df = df[df['type/displayName']=='BallTouch'].reset_index()
df = df.loc[(df['playerId']==92051)].reset_index()


pitch = VerticalPitch(pitch_type='opta', line_zorder=2, pad_bottom=0.5, pad_top=5, pitch_color='#000000',  # pitch extends slightly below halfway line
                      half=True,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)
# draw
fig, ax = pitch.draw(figsize=(12, 8))
fig.set_facecolor('#22312b')

# draw
fig, ax = pitch.draw(figsize=(12, 8))
fig.set_facecolor('#22312b')

bin_statistic = pitch.bin_statistic(df['x'], df['y'], statistic='count', bins=(20, 20))
bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
pcm = pitch.heatmap(bin_statistic, ax=ax, cmap='hot', edgecolors='#22312b')
# Add the colorbar and format off-white

# inverting y axis
plt.gca().invert_xaxis()

#plt.title('Ball Recovery',color='white',size=30)
