#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:14:01 2022

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

df = pd.read_csv('Dumfriespost.csv')
df = df.loc[(df['PlayerId']==322153 )].reset_index()
df = df.loc[(df['type/displayName']=='BallRecovery')].reset_index()


df

pitch = VerticalPitch(pitch_type='opta', line_zorder=2,
              pitch_color='#000000', half=False, line_color='#efefef')
# draw
fig, ax = pitch.draw(figsize=(6.6, 4.125))
fig.set_facecolor('#000000')
bin_statistic = pitch.bin_statistic(df.x, df.y, statistic='count', bins=(25, 25))
bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
pcm = pitch.heatmap(bin_statistic, ax=ax, cmap='seismic', edgecolors='#000000')
#pcm = pitch.heatmap(bin_statistic, ax=ax, cmap='magma', edgecolors='#000000')

#cbar = fig.colorbar(pcm, ax=ax, shrink=0.6)
#cbar.outline.set_edgecolor('#efefef')
#cbar.ax.yaxis.set_tick_params(color='#efefef')
#plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#efefef')

#labels = pitch.label_heatmap(bin_statistic, color='#f4edf0', fontsize=18,ax=ax, ha='center', va='center')

#plt.suptitle('Antony - Ajax: pass map',color='white',size=20)

#plt.gca().invert_yaxis()
#plt.gca().invert_xaxis()
plt.savefig('Dumfriesrecovery2.png',dpi=500,bbox_inches = 'tight',facecolor='#000000')
