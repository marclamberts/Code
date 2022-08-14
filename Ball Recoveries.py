#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:12:03 2021

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
import matplotlib.patheffects as path_effects

df = pd.read_csv('neccam.csv')

df = df.loc[(df['playerId']==351532)].reset_index()
df = df[df['type/displayName']=='Pass'].reset_index()

df

robotto_regular = FontManager()

path_eff = [path_effects.Stroke(linewidth=3, foreground='black'),
            path_effects.Normal()]

pearl_earring_cmap = LinearSegmentedColormap.from_list("Pearl Earring - 100 colors",
                                                       ['#15242e', '#4393c4'], N=100)

pitch = VerticalPitch(pitch_type='statsbomb', line_zorder=2, pitch_color='#22312b')
fig, axs = pitch.grid(endnote_height=0.03, endnote_space=0,
                      title_height=0.08, title_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      grid_height=0.84)
fig.set_facecolor('#22312b')

# heatmap and labels
bin_statistic = pitch.bin_statistic_positional(df.x, df.y, statistic='count',
                                               positional='full', normalize=True)
pitch.heatmap_positional(bin_statistic, ax=axs['pitch'],
                         cmap='coolwarm', edgecolors='#1e4259')
labels = pitch.label_heatmap(bin_statistic, color='#f4edf0', fontsize=18,
                             ax=axs['pitch'], ha='center', va='center',
                             str_format='{:.0%}', path_effects=path_eff)

# endnote and title
#axs['endnote'].text(1, 0.5, '@lambertsmarc', va='center', ha='right', fontsize=20,
#                    fontproperties=robotto_regular.prop, color='#dee6ea')
#axs['title'].text(0.5, 0.5, "Ball Recoveries by\n Rotherham vs Morecambe", color='#dee6ea',
 #                va='center', ha='center', path_effects=path_eff,
  #              fontproperties=robotto_regular.prop, fontsize=25)
#plt.gca().invert_xaxis()
plt.show()  # If you are using a Jupyter notebook you do not need this line

plt.savefig('bra3.png', dpi = 500, bbox_inches='tight',facecolor='#22312b')