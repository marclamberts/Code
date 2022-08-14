#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:25:33 2021

@author: jensjeukens
"""

import matplotlib.pyplot as plt
import numpy as np

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80

#ID for Sweden vs Ukraine EURO2020
match_id_required = 3794692
home_team_required ="Sweden"
away_team_required ="Ukraine"

# Load in the data
# I took this from https://znstrider.github.io/2018-11-11-Getting-Started-with-StatsBomb-Data/
file_name=str(match_id_required)+'.json'

#Load in all match events 
import json
with open('Statsbomb/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)

#get the nested structure into a dataframe 
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

#Draw the pitch
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','black')

df['x'] = df['x']
df['y'] = df['y']

if X in range(len(df['X'])):
    if df['type/displayName'][X] == 'goal':
        plt.scatter(df['y'][X],df['X'], color='red', s=50,alpha=9, zorder=2)
    if df['type/displayName'][x] == 'SavedShot':
        plt.scatter(df['y'][X],df['X'], color='gray', s=50,alpha=7, zorder=2)
    if df['type/displayName'][X] == 'MissedShors':
        plt.scatter(df['y'][X],df['X'], color='grey', s=50,alpha=7, zorder=2)
    if df['type/displayName'][X] == 'ShotOnPosts':
        plt.scatter(df['y'][X],df['X'], color='grey', s=50,alpha=7, zorder=2)
        
        
plt.gca().invert_xaxis()