#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:01:58 2021

@author: lamberts_888
"""
import numpy as np
import seaborn as sns
import pandas as pd
import math
import matplotlib.image as image
from matplotlib import artist
import matplotlib.patches as mpatches
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
from matplotlib.patches import Arc
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Franklin Gothic Medium', 'Franklin Gothic Book']

defensive = pd.read_excel('WSL attackers.xlsx')
defensive.head()

## Creating DataFrame for defenders with necessary raw and processed columns from defendersfiltered

attackersfinal = pd.DataFrame()

# Player and squad names
attackersfinal['Player'] = defensive['Player']
attackersfinal['Team'] = defensive['Team']

# Tackles Won per 90- measures the number of tackles a player wins per 90 minutes played
attackersfinal['xG per 90'] = defensive['xG per 90']

# Interceptions per 90- measures the number of interceptions a player makes per 90 minutes played
attackersfinal['xA per 90'] = defensive['xA per 90']

attackersfinal.head()


## Mean calculations for important statistics in defendersfinal

x_mean = np.mean(attackersfinal['xG per 90'])
y_mean = np.mean(attackersfinal['xA per 90'])

## Splitting DataFrame into three; one with all defenders, one with Manchester United Players, and one with Sergio Reguilon

# defenders
attackersfilter = (attackersfinal['Team'] != 'MVV') | \
        (attackersfinal['Player']!= 'T. Arokodare')
attackersd = attackersfinal[attackersfilter]

teamfilter = (attackersfinal['Team'] == 'Arsenal')
teamd = attackersfinal[teamfilter]

# Sergio Reguilon
randallfilter = (attackersfinal['Player'] == 'S. Kerr')
randalld = attackersfinal[randallfilter]

randalld

from matplotlib import transforms


def rainbow_text(x, y, strings, colors, orientation='horizontal',
                 ax=None, **kwargs):
    """
    Take a list of *strings* and *colors* and place them next to each
    other, with text strings[i] being shown in colors[i].

    Parameters
    ----------
    x, y : float
        Text position in data coordinates.
    strings : list of str
        The strings to draw.
    colors : list of color
        The colors to use.
    orientation : {'horizontal', 'vertical'}
    ax : Axes, optional
        The Axes to draw into. If None, the current axes will be used.
    **kwargs
        All other keyword arguments are passed to plt.text(), so you can
        set the font size, family, etc.
    """
    if ax is None:
        ax = plt.gca()
    t = ax.transData
    canvas = ax.figure.canvas

    assert orientation in ['horizontal', 'vertical']
    if orientation == 'vertical':
        kwargs.update(rotation=90, verticalalignment='center', horizontalalignment='center')

    for s, c in zip(strings, colors):
        text = ax.text(x, y, s + " ", color=c, transform=t, **kwargs)

        # Need to draw to update the text position.
        text.draw(canvas.get_renderer())
        ex = text.get_window_extent()
        if orientation == 'horizontal':
            t = transforms.offset_copy(
                text.get_transform(), x=ex.width, units='dots')
        else:
            t = transforms.offset_copy(
                text.get_transform(), y=ex.height, units='dots')
            

# Establishing lists used for plotting in Matplotlib    
x1 = list(attackersd['xG per 90'])
x3 = list(randalld['xG per 90'])
x2 = list(teamd['xG per 90'])
y1 = list(attackersd['xA per 90'])
y3 = list(randalld['xA per 90'])
y2 = list(teamd['xA per 90'])
n1 = list(attackersd['Player'])
n3 = list(randalld['Player'])
n2 = list(teamd['Player'])

x2

print(x1)

# Creating empty plot in desired 'fivethirtyeight' style with gridlines and desired backround colours and sizes, as well
# as aesthetic settings
fig,ax= plt.subplots(figsize=(10,10))
matplotlib.style.use('fivethirtyeight')
ax.grid(True, color='xkcd:dark grey')
fig.patch.set_facecolor('#0b0d0f')
ax.set_facecolor('#171b1e')
ax.spines['bottom'].set_color('xkcd:off white')
ax.spines['top'].set_color('xkcd:off white')
ax.spines['left'].set_color('xkcd:off white')
ax.spines['right'].set_color('xkcd:off white')
ax.spines['bottom'].set_linewidth(1)
ax.spines['top'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)
ax.spines['right'].set_linewidth(1)
ax.tick_params(axis='x', colors='xkcd:off white')
ax.tick_params(axis='y', colors='xkcd:off white')
plt.text(1.075,0.5,"\n", \
        horizontalalignment='right', verticalalignment='top', color='xkcd:off white', size='18', transform=ax.transAxes)
plt.text(1., -0.05, '\nExcludes players with <600 minutes', \
         horizontalalignment='right', verticalalignment='top', color='xkcd:off white', \
             style='italic', transform=ax.transAxes, size='14')

plt.xlim(0,1)
plt.ylim(0,.5)


words = "Sam Kerr vs Arsenal attackers vs attackers WSL 2021/2022".split()
colors = ['xkcd:bright green', 'xkcd:bright green', 'xkcd:off white','xkcd:red', 'xkcd:red', 'xkcd:off white', 'xkcd:off white',
          'xkcd:off white', 'xkcd:off white']
rainbow_text(.06, .508, words, colors, size=18)


# Adding graph and axes titles
ax.set_xlabel('\nxG per 90\n', color='xkcd:off white', size = 15)
ax.set_ylabel('\nxA per 90', color='xkcd:off white', size = 15)
ax.set_title("\nExpected goals per 90 vs Expected assists per 90\n", color='xkcd:off white', size=25)

# Adding plot points from each of the three DataFrames in different colours
plt.scatter(x=x1,y=y1,s=75, color='xkcd:dark grey', zorder=100)
plt.scatter(x=x2,y=y2,s=75, color='xkcd:red', zorder=100)
plt.scatter(x=x3,y=y3,s=75,color='xkcd:bright green', zorder=100)

# Creating and labelling average lines
plt.axhline(y=y_mean, xmin =-100, xmax=100, color='xkcd:dark grey', linestyle='--', linewidth=2)
plt.axvline(x=x_mean, ymin=-100,ymax=100, color='xkcd:dark grey', linestyle = '--', linewidth=2, zorder=0.2)
ax.fill_between([x_mean, 1000], y_mean,1000, alpha=0.1, color='xkcd:light green', zorder=10)
#plt.text(x_mean/xlimval*1.04,0.995,'Avg', \
         #horizontalalignment='right', verticalalignment='top', color='xkcd:grey', transform=ax.transAxes)
#plt.text(0.995,y_mean/ylimval,'Avg', \
         #horizontalalignment='right', verticalalignment='top', color='xkcd:grey', transform=ax.transAxes)

# Annotating some text below and some above- change based on need
for i in n2:
    if i != 'S. Kerr':
        plt.annotate(i, (x2[n2.index(i)], y2[n2.index(i)]+0.02), color='xkcd:off white', \
        horizontalalignment='center', fontsize=12, zorder=100)   
#for i in n1:
 #   if i == 'L. Smans':
  #      plt.annotate(i, (x1[n1.index(i)], y1[n1.index(i)]+0.05), color='xkcd:off white', \
   #3     horizontalalignment='center', fontsize=12, zorder=100)  
for i in n3:
        plt.annotate(i, (x3[n3.index(i)], y3[n3.index(i)]+0.02), color='xkcd:off white', \
        horizontalalignment='center', fontsize=12, zorder=100) 
 
 # Watermarking visualization
plt.text(0.03, -0.07, 'Twitter @lambertsmarc\nData from Wyscout', \
         horizontalalignment='left', verticalalignment='top', color='xkcd:off white', transform=ax.transAxes,zorder=1000)
plt.show()

