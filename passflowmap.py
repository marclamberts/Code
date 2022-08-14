#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:31:16 2021

@author: lamberts_888
"""
from mplsoccer.pitch import VerticalPitch
from mplsoccer.statsbomb import read_event, EVENT_SLUG
from matplotlib import rcParams
from scipy.stats import circmean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

rcParams['text.color'] = '#c7d5cc'  # set the default text color

df = pd.read_csv('wimbledonplymouth.csv')
df = df.loc[(df['teamId']==212)].reset_index()

df['x'] = df['x']
df['y'] = df['y']
df['endX'] = df['endX']
df['endY'] = df['endY']

pitch = VerticalPitch(pitch_type='opta', orientation='horizontal', figsize=(16, 11), line_zorder=2,
              line_color='white', constrained_layout=True, tight_layout=False, pitch_color='#22312b')
bins = (6, 4)

fig, ax = pitch.draw()

bs_heatmap = pitch.bin_statistic(df.x, df.y, statistic='count', bins=bins)
hm = pitch.heatmap(bs_heatmap, ax=ax, cmap='Blues')

mask = df.endX.notnull()
df = df[mask].copy()

 #  plot the pass flow map with a single color ('black') and length of the arrow (5)
fm =pitch.flow(df.x, df.y, df.endX, df.endY, color='#000000', arrow_type='same', arrow_length=10, bins=bins, ax=ax)

#grey = LinearSegmentedColormap.from_list('custom cmap', ['#DADADA', 'black'])
#fm = pitch.flow(df.x, df.y, df.endX, df.endY, cmap=grey,
 #              arrow_type='average', arrow_length=10, bins=bins, ax=ax)

fig.set_facecolor('#22312b')
