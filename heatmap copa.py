#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:52:12 2021

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

df = pd.read_csv('monmar.csv')

df = df.loc[(df['teamId']==249)].reset_index()

df

df['x'] = df['x']
df['y'] = df['y']
df['endX'] = df['endX']
df['endY'] = df['endY']

# dark
pitch_dark = VerticalPitch(line_color='#cfcfcf', line_zorder=2, pitch_color='#000000')
fig, ax = pitch_dark.draw()
fig.set_facecolor('#000000')
kdeplot_dark = pitch_dark.kdeplot(df.x, df.y, ax=ax, cmap=cmr.sunburst, shade=True, levels=100)

plt.title('Heatmap Marseille vs Montpellier',color='white',size=15)
plt.savefig('ja.png',dpi=500,bbox_inches = 'tight',facecolor='#000000')