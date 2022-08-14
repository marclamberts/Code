#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
#from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import VerticalPitch
from matplotlib import patches

text_color = 'w'
df = pd.read_csv('fortunasittardajax.csv')
team1 = df.loc[(df['team_id']==8593)].reset_index()
team2 = df.loc[(df['team_id']==6422)].reset_index()

pitch = VerticalPitch(pitch_type='uefa', pad_bottom=0.5, pad_top=5, pitch_color='#22312b', line_color='white',  # pitch extends slightly below halfway line
                      half=False,  # half of a pitch
                      goal_type='box',
                      goal_alpha=0.8)

fig, ax = pitch.draw()
fig.set_facecolor('#22312b')

#team1 will feature down
for x in range(len(team1['x'])):
    if team1['event_type'][x] == 'Goal':
        
        print(team1['y'][x], team1['x'][x])
        #plt.scatter(team1['y'][x], team1['x'][x], color='red', s=df['expected_goals'][x]*400, alpha=.9, zorder=2)
        plt.scatter(68 - team1['y'][x], 105 - team1['x'][x], color='red', s=df['expected_goals'][x]*400, alpha=.9, zorder=3)
    if team1['event_type'][x] == 'Miss':
        print(team1['y'][x], team1['x'][x])
        #plt.scatter(team1['y'][x], team1['x'][x], color='grey', s=df['expected_goals'][x]*400, alpha=.9, zorder=2)
        plt.scatter(68 - team1['y'][x], 105 - team1['x'][x], color='grey', s=df['expected_goals'][x]*400, alpha=.9, zorder=2)   
    if team1['event_type'][x] == 'AttemptSaved':
        print(team1['y'][x], team1['x'][x])
        #plt.scatter(team1['y'][x], team1['x'][x], color='grey', s=df['expected_goals'][x]*400, alpha=.9, zorder=2)
        plt.scatter(68 - team1['y'][x], 105 - team1['x'][x], color='grey', s=df['expected_goals'][x]*400, alpha=.9, zorder=2)
    if team1['event_type'][x] == 'Post':
        print(team1['y'][x], team1['x'][x])
        #plt.scatter(team1['y'][x], team1['x'][x], color='grey', s=df['expected_goals'][x]*400, alpha=.9, zorder=2)
        plt.scatter(68 - team1['y'][x], 105 - team1['x'][x], color='grey', s=df['expected_goals'][x]*400, alpha=.9, zorder=2)

#team2 will feature up        
for x in range(len(team2['x'])):
    if team2['event_type'][x] == 'Goal':
        plt.scatter(team2['y'][x], team2['x'][x], color='red', s=team2['expected_goals'][x]*400, alpha=.9, zorder=3)
    if team2['event_type'][x] == 'Miss':
        plt.scatter(team2['y'][x], team2['x'][x], color='grey', s=team2['expected_goals'][x]*400, alpha=.9, zorder=2)
    if team2['event_type'][x] == 'AttemptSaved':
        plt.scatter(team2['y'][x], team2['x'][x], color='grey', s=team2['expected_goals'][x]*400, alpha=.9, zorder=2)
    if team2['event_type'][x] == 'Post':
        plt.scatter(team2['y'][x], team2['x'][x], color='grey', s=team2['expected_goals'][x]*400, alpha=.9, zorder=2)    


ax.set_title("Fortuna Sittarad vs Ajax 2-3\nxG 0,91 vs 1,91", fontsize=12, color="w", fontfamily="Andale Mono", fontweight='bold', pad=8)

fig.text(.40,0.005,f'@lambertsmarc / twitter',fontstyle='italic',fontsize=8,fontfamily='Andale Mono', color='w')

plt.savefig('foraja.png', dpi=750, bbox_inches = 'tight', facecolor='#22312b')

