#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 13:06:11 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib.colors import to_rgba
import numpy as np
from mplsoccer.statsbomb import read_event, EVENT_SLUG
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colorbar
from matplotlib.colors import LinearSegmentedColormap
from highlight_text import fig_text
import math

df = pd.read_csv("01-12-Aug-22-ExcVit-event.csv")
df2 = pd.read_csv("12-Aug-22-ExcVit_playerid.csv")

df2.columns =['Nr', 'PlayerId', 'PlayerName']

df = df.merge(df2, on = 'PlayerId', how = 'left')

OneTeam = df.loc[(df['TeamId']==255)]

OneTeam["newsecond"] = 60*OneTeam["minute"]+OneTeam["second"]
    
OneTeam.sort_values(by=['newsecond'])

#identify the passer and then the recipient, who'll be the playerId of the next action
OneTeam['passer'] = OneTeam['PlayerName']

OneTeam['recipient'] = OneTeam['passer'].shift(-1)


#filter for only passes and then successful passes
Passes = OneTeam.loc[(OneTeam['type/displayName']=="Pass")]

Completions = Passes.loc[(Passes['outcomeType/displayName']=="Successful")]

#find time of the team's first substitution and filter the df to only passes before that
Subs = OneTeam.loc[(OneTeam['type/displayName']=="SubstitutionOff")]
SubTimes = Subs["newsecond"]
SubOne = SubTimes.min()

pas = Completions['passer']
rec = Completions['recipient']

Completions['passer'] = pas
Completions['recipient'] = rec

SubTimes
#SubOne

Completions = Completions.loc[Completions['newsecond'] < SubOne]

average_locs_and_count = Completions.groupby('passer').agg({'x': ['mean'], 'y': ['mean','count']})
average_locs_and_count.columns = ['x', 'y', 'count']

average_locs_and_count

passes_between = Completions.groupby(['passer', 'recipient']).id.count().reset_index()
passes_between.rename({'id': 'pass_count'}, axis='columns', inplace=True)

passes_between = passes_between.merge(average_locs_and_count, left_on='passer', right_index=True)
passes_between = passes_between.merge(average_locs_and_count, left_on='recipient', right_index=True,
                                      suffixes=['', '_end'])


passes_between.dtypes

size=1000
radius = math.sqrt(size)/2.
arrow = mpl.patches.FancyArrowPatch(posA=(1.2*passes_between.x,80-.8*passes_between.y), 
                                    posB=(1.2*passes_between.x_end,80-.8*passes_between.y_end), 
                                    arrowstyle='-|>', mutation_scale=20, shrinkA=radius, shrinkB=radius)

#set minimum threshold for pass arrows to be plotted. So this will only plot combos which occured at least 5 times.
passes_between = passes_between.loc[(passes_between['pass_count']>2)]


#Make arrows less transparent if they have a higher count, totally optional of course
min_transparency = 0.3
color = np.array(to_rgba('#d3d3d3'))
color = np.tile(color, (len(passes_between), 1))
c_transparency = passes_between.pass_count / passes_between.pass_count.max()
c_transparency = (c_transparency * (1 - min_transparency)) + min_transparency
color[:, 3] = c_transparency

pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#000000', line_color='#c7d5cc',pad_bottom=10)
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False,)
fig.set_facecolor("#71797E")

def pass_line_template(ax, x, y, end_x, end_y, line_color):
    ax.annotate('', xy=(80-.8*end_y, 1.2*end_x), xytext=(80-.8*y, 1.2*x), zorder=1,
    arrowprops=dict(arrowstyle='-|>', linewidth=4, color='#c7d5cc', alpha=.85))
    
def pass_line_template_shrink(ax, x, y, end_x, end_y, line_color, dist_delta=1.2):
    dist = math.hypot(end_x - x, end_y - y)
    angle = math.atan2(end_y-y, end_x-x)
    upd_x = x + (dist - dist_delta) * math.cos(angle)
    upd_y = y + (dist - dist_delta) * math.sin(angle)
    pass_line_template(ax, x, y, upd_x, upd_y, line_color=line_color)
    
    
for index, row in passes_between.iterrows():
    pass_line_template_shrink(ax,row['x'],row['y'],row['x_end'],row['y_end'],'white')

#plot nodes
pass_box = pitch.scatter(1.2*average_locs_and_count.x, 80-0.8*average_locs_and_count.y, s=600,
                           color='#FF0000', edgecolors="#010101", linewidth=2, alpha=1, ax=ax, zorder=2)


#anootation/key at bottom
pitch.annotate("Node Positions = Average Start Location of Completed Passes\nArrows Show Pass Combinations Which Occured Over 2 Times", (-4, 40), color='white',
         fontsize=10, ha='center', va='center', ax=ax, fontweight='bold', fontfamily="Andale Mono",)


#Uncomment these next two lines to get each node labeled with the player id. Check to see if anything looks off, and make note of each player if you're going to add labeles later like their numbers
for index, row in average_locs_and_count.iterrows():
   pitch.annotate(row.name, xy=(1.2*row.x, 80-0.8*row.y), bbox = dict(boxstyle="round", fc="0.8"), c='black', va='bottom', ha='right', size=10, fontweight='bold', fontfamily="Century Gothic",ax=ax)

#Set the background color
fig.patch.set_facecolor('#000000')

#annotatios
#ax.set_title("Vitesse \nUntil first sub - 64th minute", fontsize=25, color="w", fontfamily="Andale Mono", fontweight='bold', pad=8)


#fig.text(.43,0.01,f'@lambertsmarc / twitter',fontstyle='italic',fontsize=14,fontfamily='Andale Mono', color='w')

#save the plot
plt.savefig('vitesse.png', dpi = 1500, bbox_inches='tight',facecolor='#000000')