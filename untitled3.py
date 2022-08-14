#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:09:27 2021

@author: lamberts_888
"""
from mplsoccer.pitch import VerticalPitch
from mplsoccer.statsbomb import read_event, EVENT_SLUG
import os
import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
plt.style.use('dark_background')

df = pd.read_csv('newcastle.csv')

df = df.loc[(df['teamId']==30)].reset_index()

df['x'] = df['x']
df['y'] = df['y']
df['endX'] = df['endX']
df['endY'] = df['endY']

# setup pitch
pitch = VerticalPitch(pitch_type='opta', figsize=(16, 9), line_zorder=2, line_color='white', orientation='horizontal')
# draw
fig, ax = pitch.draw()
bin_statistic = pitch.bin_statistic(df.x, df.y, statistic='count', bins=(15, 10))
bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
pcm = pitch.heatmap(bin_statistic, ax=ax, cmap='Reds', edgecolors='#22312b')
#cbar = fig.colorbar(pcm, ax=ax)
#title = fig.suptitle('Heatmap - Tottenham vs Newcastle', x=0.5, y=0.99, fontsize=23)