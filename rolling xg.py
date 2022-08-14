#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:29:37 2022

@author: lamberts_888
"""
# use pandas to load and manipulate the data, matplotlib to plot
#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.patheffects as path_effects
import matplotlib.patches as mpatches
import matplotlib.image as mpimg
from matplotlib import rcParams
from matplotlib.patches import Arc
import numpy as np
from highlight_text import fig_text
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import json


df = pd.read_excel('eskilstunaxg.xlsx')

df['Date'] = range(1,19)

df['xgSMA'] = df['xG'].rolling(window=3).mean()
df['xGASMA'] = df['xGA'].rolling(window=3).mean()

#plt.margins(x=0,y=0)



plt.style.use('dark_background')
fig,ax = plt.subplots(figsize = (20,14))
# plotting xG and xGA
ax.plot(df.Date,df.xgSMA,label='Expected goals',color='lime')
ax.plot(df.Date,df.xGASMA,color='red',label='Expected goals Against')

ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.legend()

ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

#plt.xticks(df['Matches'], teams_played, rotation='vertical')

# title
fig_text(0.04,1.1, s="Eskilstuna 2022 season\n", fontsize = 80, fontweight = "bold")
fig_text(0.04,0.97, s=" Expected Goals Scored (xG) vs Expected Goals Against (xGA)",color="white", fontsize = 40, fontweight="light")

# text
fig_text(0.4,0.05, s="Matches\n", fontsize = 40, fontweight = "bold", color = "white")
fig_text(0.03,0.6, s="Rolling averages\n", fontsize = 40, fontweight = "bold", color = "white",rotation=90)

#plt.plot(df.Match,df.xgSMA,color='green', label="Expected goals")
#plt.plot(df.Match,df.GFSMA,color='red', label="Goals scored")
#leg = plt.legend(loc='upper right')

plt.grid(False)

plt.savefig('rollingxgeskilstuna.png',dpi=500,bbox_inches = 'tight')



