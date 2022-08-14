#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 15:25:31 2022

@author: lamberts_888
"""
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from highlight_text import fig_text
from matplotlib.patches import Arc
import numpy as np

link = "https://understat.com/match/17120/"
res = requests.get(link)
soup = BeautifulSoup(res.content,'lxml')
scripts = soup.find_all('script')
# Get the shotsData, it's the second script executed in order
strings = scripts[1].string 
# Getting rid of unnecessary characters from json data
ind_start = strings.index("('")+2 
ind_end = strings.index("')") 
json_data = strings[ind_start:ind_end] 
json_data = json_data.encode('utf8').decode('unicode_escape')
data = json.loads(json_data)

df_h = pd.DataFrame(data['h'])
df_a = pd.DataFrame(data['a'])
df = df_h.append(df_a)

# Changing the data types 
df['xG'] = df['xG'].astype('float64')
df['X'] = df['X'].astype('float64')
df['Y'] = df['Y'].astype('float64')

# Adjusting the measurements
df['X'] = (df['X']/100)*105*100
df['Y'] = (df['Y']/100)*68*100

# Dividing the df between away and home again
df_h = pd.DataFrame(df[df['h_a']=='h'])
df_a = pd.DataFrame(df[df['h_a']=='a'])

# xG for each team
# Sociedad
total_shots_h = df_h[df_h.columns[0]].count()
xGcum_h = np.round(max(np.cumsum(df_h['xG'])),3)
xG_per_shot_h = np.round(max(np.cumsum(df_h['xG']))/(df_h[df_h.columns[0]].count()),3)
goal_h = df_h[df_h['result']=='Goal']
goal_h = goal_h[goal_h.columns[0]].count()
h_team = df['h_team'].iloc[0]

# Barcelona 
# xG for each team
total_shots_a = df_a[df_a.columns[0]].count().tolist()
xGcum_a = np.round(max(np.cumsum(df_a['xG'])),3).tolist()
xG_per_shot_a = np.round(max(np.cumsum(df_a['xG']))/(df_a[df_a.columns[0]].count()),3).tolist()
goal_a = df_a[df_a['result']=='Goal']
goal_a = goal_a[goal_a.columns[0]].count().tolist()
a_team = df['a_team'].iloc[0]

def football_pitch(x_min=0, x_max=105,
               y_min=0, y_max=68,
               pitch_color="#f9f8dd",
               line_color='black',
               line_thickness=1.5,
               point_size=20,
               orientation="horizontal",
               aspect="full",
               axis='off',
               ax=None
               ):

    if not ax:
        raise TypeError("This function is intended to be used with an existing fig and ax in order to allow flexibility in plotting of various sizes and in subplots.")


    if orientation.lower().startswith("h"):
        first = 0
        second = 1
        arc_angle = 0

        if aspect == "half":
            ax.set_xlim(x_max / 2, x_max + 5)

    elif orientation.lower().startswith("v"):
        first = 1
        second = 0
        arc_angle = 90

        if aspect == "half":
            ax.set_ylim(x_max / 2, x_max + 5)

    
    else:
        raise NameError("You must choose one of horizontal or vertical")
    
    ax.axis(axis)

    rect = plt.Rectangle((x_min, y_min),
                         x_max, y_max,
                         facecolor="white",
                         edgecolor="none",
                         zorder=-2)

    ax.add_artist(rect)

    x_conversion = x_max / 100
    y_conversion = y_max / 100

    pitch_x = [0,5.8,11.5,17,50,83,88.5,94.2,100] # x dimension markings
    pitch_x = [x * x_conversion for x in pitch_x]

    pitch_y = [0, 21.1, 36.6, 50, 63.2, 78.9, 100] # y dimension markings
    pitch_y = [x * y_conversion for x in pitch_y]

    goal_y = [45.2, 54.8] # goal posts
    goal_y = [x * y_conversion for x in goal_y]

    # side and goal lines
    lx1 = [x_min, x_max, x_max, x_min, x_min]
    ly1 = [y_min, y_min, y_max, y_max, y_min]

    # outer box
    lx2 = [x_max, pitch_x[5], pitch_x[5], x_max]
    ly2 = [pitch_y[1], pitch_y[1], pitch_y[5], pitch_y[5]]

    lx3 = [0, pitch_x[3], pitch_x[3], 0]
    ly3 = [pitch_y[1], pitch_y[1], pitch_y[5], pitch_y[5]]

    # goals
    lx4 = [x_max, x_max+2, x_max+2, x_max]
    ly4 = [goal_y[0], goal_y[0], goal_y[1], goal_y[1]]

    lx5 = [0, -2, -2, 0]
    ly5 = [goal_y[0], goal_y[0], goal_y[1], goal_y[1]]

    # 6 yard box
    lx6 = [x_max, pitch_x[7], pitch_x[7], x_max]
    ly6 = [pitch_y[2],pitch_y[2], pitch_y[4], pitch_y[4]]

    lx7 = [0, pitch_x[1], pitch_x[1], 0]
    ly7 = [pitch_y[2],pitch_y[2], pitch_y[4], pitch_y[4]]


    # Halfline, penalty spots, and kickoff spot
    lx8 = [pitch_x[4], pitch_x[4]]
    ly8 = [0, y_max]

    lines = [
        [lx1, ly1],
        [lx2, ly2],
        [lx3, ly3],
        [lx4, ly4],
        [lx5, ly5],
        [lx6, ly6],
        [lx7, ly7],
        [lx8, ly8],
        ]

    points = [
        [pitch_x[6], pitch_y[3]],
        [pitch_x[2], pitch_y[3]],
        [pitch_x[4], pitch_y[3]]
        ]
    circle_points = [pitch_x[4], pitch_y[3]]
    arc_points1 = [pitch_x[6], pitch_y[3]]
    arc_points2 = [pitch_x[2], pitch_y[3]]


    for line in lines:
        ax.plot(line[first], line[second],
                color=line_color,
                lw=line_thickness,
                zorder=-1)

    for point in points:
        ax.scatter(point[first], point[second],
                   color=line_color,
                   s=point_size,
                   zorder=-1)

    circle = plt.Circle((circle_points[first], circle_points[second]),
                        x_max * 0.088,
                        lw=line_thickness,
                        color=line_color,
                        fill=False,
                        zorder=-1)

    ax.add_artist(circle)

    arc1 = Arc((arc_points1[first], arc_points1[second]),
               height=x_max * 0.088 * 2,
               width=x_max * 0.088 * 2,
               angle=arc_angle,
               theta1=128.75,
               theta2=231.25,
               color=line_color,
               lw=line_thickness,
               zorder=-1)

    ax.add_artist(arc1)

    arc2 = Arc((arc_points2[first], arc_points2[second]),
               height=x_max * 0.088 * 2,
               width=x_max * 0.088 * 2,
               angle=arc_angle,
               theta1=308.75,
               theta2=51.25,
               color=line_color,
               lw=line_thickness,
               zorder=-1)

    ax.add_artist(arc2)

    ax.set_aspect("equal")

    return ax
fig, ax = plt.subplots(figsize=(11, 7))
#Drawing a full pitch horizontally
football_pitch(orientation="horizontal",aspect="full",line_color="black",ax=ax)

# Barcelona away team 
z_a = df_a['xG'].tolist()
z1 = [1000 * i for i in z_a] # This is to scale the "xG" values for plotting
colors = {'Goal':'lightsteelblue', 'MissedShots':'tomato', 'BlockedShot':'gold', 'SavedShot':'gray', 'ShotOnPost':'peru'}
##markers = {'Goal':'Star', 'MissedShots':'X', 'BlockedShot':'O', 'SavedShot':'V', 'ShotOnPost':'S'}
plt.scatter(y=df_a["Y"],x=df_a["X"],s=z1, marker='o',color=df_a['result'].map(colors),edgecolors="black")
plt.tight_layout()

# Real Sociedad  
z_h = df_h['xG'].tolist()
z2 = [1000 * i for i in z_h] # This is to scale the "xG" values for plotting
colors = {'Goal':'lightsteelblue', 'MissedShots':'tomato', 'BlockedShot':'gold', 'SavedShot':'gray', 'ShotOnPost':'peru'}
#markers = {'Goal':'Star', 'MissedShots':'X', 'BlockedShot':'O', 'SavedShot':'V', 'ShotOnPost':'S'}
plt.scatter(y=65-(df_h["Y"]),x=105-(df_h["X"]),s=z2, marker='o',color=df_h['result'].map(colors),edgecolors="black")
plt.tight_layout()

# text
# Sociedad
fig_text(0.199,1.04, s="<{}> | Goals : <{}> | Shots : <{}> | xG per Shot : <{}> ".format(h_team,goal_h,total_shots_h,xG_per_shot_h), fontsize = 15, fontweight = "bold", color="black")

# Barcelona
fig_text(0.199,.99, s="<{}>        | Goals : <{}> | Shots : <{}> | xG per Shot : <{}> ".format(a_team,goal_a,total_shots_a,xG_per_shot_a), fontsize = 15, fontweight = "bold", color="black")
# xG per team
fig_text(0.1,.17, s="{} : <{}> ".format(h_team,xGcum_h), fontsize = 15.5, fontweight = "bold", color="black")
fig_text(0.55,.17, s="{} : <{}> ".format(a_team,xGcum_a), fontsize = 15.5, fontweight = "bold", color="black")

# Scatter plot for goals, blocked shots, missed shots
plt.scatter(15,65,s=180, edgecolor="black",color='lightsteelblue')
plt.scatter(35,65,s=180, edgecolor="black",color='tomato')
plt.scatter(55,65,s=180, edgecolor="black",color='gold')
plt.scatter(75,65,s=180, edgecolor="black",color='gray')
plt.scatter(95,65,s=180, edgecolor="black",color='peru')
xx = [10,25,45,65,85]
yy = [65,65,65,65,65]
xx_yy = ['Goal', 'MissedShots', 'BlockedShot', 'SavedShot', 'ShotOnPost']
for i in range(len(xx)):
    plt.text(xx[i], yy[i], xx_yy[i], fontsize=12, color="black",ha="center", va="center",fontweight='bold')
fig.text(.50,0.01,f'@lambertsmarc / twitter',fontstyle='italic',fontsize=15,fontfamily='Andale Mono', color='black')

plt.savefig('HERBOCH.png',dpi=750,bbox_inches = 'tight',facecolor='white')

