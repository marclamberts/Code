#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:36:33 2021

@author: lamberts_888
"""

import pandas as pd
from highlight_text import fig_text
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

df = pd.read_excel('ned2.xlsx')
df = df.loc[(df['teamId']==335)].reset_index()
df['passer'] = df['playerId']
df['recipient'] = df['playerId'].shift(-1)

#find passes and then only look for the successful passes
passes = df[df['type/displayName']=='Pass']
successful = passes[passes['outcomeType/displayName']=='Successful']
successful

formation_dict = {1: 'GK', 2: 'RB', 3: 'RCB', 4: 'CB', 5: 'LCB', 6: 'LB', 7: 'RWB',
                  8: 'LWB', 9: 'RDM', 10: 'CDM', 11: 'LDM', 12: 'RM', 13: 'RCM',
                  14: 'CM', 15: 'LCM', 16: 'LM', 17: 'RW', 18: 'RAM', 19: 'CAM',
                  20: 'LAM', 21: 'LW', 22: 'RCF', 23: 'ST', 24: 'LCF', 25: 'SS'}
subs = df[df['type/displayName']=='SubstitutionOff']
subs = subs['minute']
firstSub = subs.min()


#you do this to filter for below the 20th minute, delete the hashtag to uncomment and run the code.
#successful = successful[successful['minute'] < 20]

#this code will filter the dataframe for between the 20th and 45th minute. delete the hashtag to uncomment and run the code
successful = successful[(successful['minute'] >= 1) & (successful['minute']<45)]
successful

#this makes it so our passer and recipients are float values
pas = pd.to_numeric(successful['passer'],downcast='integer')
rec = pd.to_numeric(successful['recipient'],downcast='integer')
successful['passer'] = pas
successful['recipient'] = rec

#now we need to find the average locations and counts of the passes
average_locations = successful.groupby('passer').agg({'x':['mean'],'y':['mean','count']})
average_locations.columns = ['x','y','count']
average_locations

successful

#now we need to find the number of passes between each player
pass_between = successful.groupby(['passer','recipient']).id.count().reset_index()
pass_between.rename({'id':'pass_count'},axis='columns',inplace=True)

#merge the average location dataframe. We need to merge on the passer first then the recipient
pass_between = pass_between.merge(average_locations, left_on='passer',right_index=True)
pass_between = pass_between.merge(average_locations, left_on='recipient',right_index=True,suffixes=['', '_end'])

pass_between

pass_between = pass_between[pass_between['pass_count']>3]


pass_between


pitch = pitch = Pitch(pitch_type='opta', orientation='horizontal',
              pitch_color='#22312b', line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=True, tight_layout=False)
fig, ax = pitch.draw()
fig.set_facecolor('#22312b')

#plot the arrows

arrows = pitch.arrows(pass_between.x,pass_between.y,pass_between.x_end,pass_between.y_end,
                     width = 5, headwidth = 5, color = 'w', ax = ax, zorder = 1, alpha = .5)

#plot the nodes

nodes = pitch.scatter(average_locations.x,average_locations.y,
                     s = 300, color = 'red', edgecolors = 'black', linewidth = 2.5, alpha = 1, zorder = 1, ax=ax)

for index, row in average_locations.iterrows():
     pitch.annotate(row.name, xy=(row.x, row.y), c='#132743', va='center', ha='center', size=10, fontweight='bold', fontfamily="Century Gothic",ax=ax)

#make annotations

fig.text(.08,.08,f'@lambertsmarc/ twitter',fontstyle='italic',fontsize=14,fontfamily='Andale Mono',color='#d3d3d3')
#fig.text(.58,.08,f'Passnetwork: 1st-56th minute',fontstyle='italic',fontsize=14,fontfamily='Andale Mono',color='#d3d3d3')

#s='VVV-Venlo vs FC Utrecht'
#fig_text(s=s,
 #       x=.55,y=.9,
  #      fontfamily='Andale Mono',
   #     highlight_weights=['bold'],
    #    fontsize=24,
     #   color='#d3d3d3')