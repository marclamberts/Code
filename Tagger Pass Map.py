#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:44:34 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
from mplsoccer.pitch import VerticalPitch
import seaborn as sns
from matplotlib import patches
df = pd.read_excel('Robson passing.xlsx')


#df = df.loc[(df['PlayerId']==97719)].reset_index()

#final third passes
#df = df.loc[(df['x']>=70)]

#df = df.loc[(df['x']<=60)]


df = df[df['Event']=='Pass'].reset_index()


df['X'] = df['X']
df['Y'] = df['Y']
df['X2'] = df['X2']
df['Y2'] = df['Y2']



df

fig ,ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('#15242e')
ax.patch.set_facecolor('#15242e')

pitch = VerticalPitch(pitch_type='opta', orientation='vertical',
              pitch_color='#15242e', line_zorder=2, line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=False, tight_layout=True)

#Draw the pitch on the ax figure as well as invert the axis for this specific pitch
pitch.draw(ax=ax)
#plt.gca().invert_yaxis()
#plt.gca().invert_xaxis()

#use a for loop to plot each pass
for x in range(len(df['X'])):
    if df['Result'][x] == 'Successful':
        #on here you have the parenthesis around the arguments which will essentially make it be missing some values. 
        # if you remove those like below it should work.You also need to add ax=ax at the end so it plots correctly.
        #pitch.arrows((df['x'][x],df['y'][x]),(df['xend'][x],df['yend'][x]),color='green')
        #pitch.arrows(df['x'][x],df['y'][x],color='green')
        pitch.arrows(df['X'][x],df['Y'][x],df['X2'][x],df['Y2'][x],width=2, zorder=2,
             headwidth=10, headlength=10, color='#ad993c',ax=ax)
    if df['Result'][x] == 'Unsuccessful':
        #same thing here with the 
        #pitch.arrows((df['xend'][x],df['x'][x]),(df['yend'][x],df['y'][x]),color='red')
        #plt.scatter(df['x'][x],df['y'][x],color='red')
        pitch.arrows(df['X'][x],df['Y'][x],df['X2'][x],df['Y2'][x],width=2, zorder=2,
             headwidth=10, headlength=10, color='#ba4f45',ax=ax)
        
#plt.suptitle('Charlotte Potts vs Liverpool',color='white',size=25)

plt.gca().invert_xaxis()

plt.savefig('MGPASS.png',dpi=1500,bbox_inches = 'tight',facecolor='#15242e')

