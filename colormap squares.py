#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:21:37 2021

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

df = pd.read_csv('SUNIPS.csv')

#df = df.loc[(df['teamId']==16)].reset_index()
df = df.loc[(df['playerId']==294849)].reset_index()


df

df['x'] = df['x']
df['y'] = df['y']
df['endX'] = df['endX']
df['endY'] = df['endY']

cmap_dict = cmr.cm.cmap_cd
all_cmap_dict = {}
for cmap_type_key in cmap_dict:
    for key, cmap in cmap_dict[cmap_type_key].items():
        if key[-2:] != '_r':
            all_cmap_dict[key] = cmap
            
flamingo_cmap = LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                       ['#15242e', '#4393c4'], N=100)

# dark
pitch = VerticalPitch(line_color='#cfcfcf', line_zorder=2, pitch_color='#122c3d')
fig, ax = pitch.draw(figsize=(4.4, 6.4))
bs = pitch.bin_statistic(df.x, df.y, bins=(12, 8))
heatmap = pitch.heatmap(bs, edgecolors='#122c3d', ax=ax, cmap=flamingo_cmap)
#plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
# note use the colormap with 100 colors for a smoother finish
# sphinx_gallery_thumbnail_path = 'gallery/pitch_plots/images/sphx_glr_plot_cmap_007.png'
#kdeplot = pitch.kdeplot(df.x, df.y, ax=ax, cmap=pearl_earring_cmap, shade=True, levels=100)

#plt.suptitle('vs Swindon Town (H)',color='white',size=20)