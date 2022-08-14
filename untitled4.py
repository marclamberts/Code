#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:35:51 2021

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

df = pd.read_csv('braarg.csv')

df = df.loc[(df['teamId']==346)].reset_index()

df

#df['x'] = df['x']
#df['y'] = df['y']
#df['endX'] = df['endX']
#df['endY'] = df['endY']

pearl_earring_cmap = LinearSegmentedColormap.from_list("Pearl Earring - 100 colors",
                                                       ['#15242e', '#4393c4'], N=100)

pitch = VerticalPitch(line_color='#cfcfcf', line_zorder=2, pitch_color='#122c3d')
fig, ax = pitch.draw(figsize=(4.4, 6.4))
fig.set_facecolor('#15242e')
bs = pitch.bin_statistic(df.x, df.y, bins=(6,4))
heatmap = pitch.heatmap(bs, edgecolors='#122c3d', ax=ax, cmap=pearl_earring_cmap)



