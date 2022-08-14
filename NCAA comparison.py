#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:19:45 2022

@author: lamberts_888
"""
import pandas as pd
import numpy as np

from scipy import stats
import math

from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt

#import csv of premier league defensive stats from fbref. I have uploaded the data but I changed the column names in the csv prior.
#df = pd.read_excel('SCO1 AM ATT.xlsx')
df = pd.read_excel('NCAA D1 top goals per 90.xlsx')
#df = pd.read_excel('SCO1 Wingers.xlsx')

#when you first read in the csv from fbref, you'll notice the player names are kind of weird. This code splits them on the \
df['Player'] = df['Player'].str.split('\\',expand=True)[0]

df = df.drop(['Age', 'Club', 'Minutes', 'Postion',],axis=1).reset_index()

#Create a parameter list
params = list(df.columns)
params

params = params[2:]
params

player = df.loc[df['Player']=='Michelle Cooper'].reset_index()
player = list(player.loc[0])
print(player)

df.Player.values

# the length of our players in longer than the length of the params. we need to drop the first 3 player list items
print(len(player),print(len(params)))
player = player[3:]
print(len(player),print(len(params)))

values = []
for x in range(len(params)):   
    values.append(math.floor(stats.percentileofscore(df[params[x]],player[x])))
    
round(stats.percentileofscore(df[params[0]],player[0]))

for n,i in enumerate(values):
    if i == 100:
        values[n] = 99
        
baker = PyPizza(
    params=params,                  # list of parameters
    straight_line_color="#000000",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_lw=1,               # linewidth of last circle
    other_circle_lw=1,              # linewidth for other circles
    other_circle_ls="-."            # linestyle for other circles
)

# color for the slices and tex
slice_colors = ["#1A78CF"] * 7 + ["#FF9300"] * 0 + ["#D70232"] * 0
text_colors = ["#000000"] * 8 + ["#F2F2F2"] * 5

# plot pizza
fig, ax = baker.make_pizza(
    values,              # list of values
    figsize=(8, 8.5),      # adjust figsize according to your need
    param_location=110,# where the parameters will be added
    color_blank_space="same",
    slice_colors=slice_colors,
    kwargs_slices=dict(
        edgecolor="#000000",
        zorder=2, linewidth=1
    ),                   # values to be used when plotting slices
    kwargs_params=dict(
        color="#000000", fontsize=12,
        va="center", alpha=.5
    ),                   # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=12,
        zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#6CABDD",
            boxstyle="round,pad=0.2", lw=1
        )
    )                    # values to be used when adding parameter-values
)

# add title
fig.text(
    0.515, 0.97, "Michelle Cooper - Duke Blue Devils University \n\n", size=20,
    ha="center", color="#000000"
)

# add subtitle
fig.text(
    0.515, 0.932,
    "Per 90 Percentile Rank vs top 30 NCAA D1 strikers\n\n",
    size=15,
    ha="center", color="#000000"
)

fig.text(
    0.09, 0.005, f"Minimal 300 minutes\n")

# add credits
notes = '@lambertsmarc'
CREDIT_1 = "by Marc Lamberts | @lambertsmarc \ndata: Wyscout"
CREDIT_2 = '@lambertsmarc'
CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"
CREDIT_3 = "by Alina Ruprecht | @alina_rxp"

fig.text(
    0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
    color="#000000",
    ha="right"
)




plt.savefig('engmanpercentileradar.png',dpi=500,bbox_inches = 'tight', facecolor='white')

