#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 00:57:26 2022

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
from PIL import Image
import os

df = pd.read_excel('Dumfries pre serie a.xlsx')

df['Player'] = df['Player'].str.split('\\',expand=True)[0]
df.Player.unique()

df = df[(df['Player']=='D. Dumfries') | (df['Player']=='Average')].reset_index()
df = df.drop(['index','Team','Position',],axis=1)

#get parameters
params = list(df.columns)
params = params[1:]
params

ranges = []
a_values = []
b_values = []

for x in params:
    a = min(df[params][x])
    a = a - (a*.25)
    
    b = max(df[params][x])
    b = b + (b*.25)
    
    ranges.append((a,b))
    
for x in range(len(df['Player'])):
    if df['Player'][x] == 'D. Dumfries':
        a_values = df.iloc[x].values.tolist()
    if df['Player'][x] == 'Average':
        b_values = df.iloc[x].values.tolist()
        
a_values = a_values[1:]
b_values = b_values[1:]

values = [a_values,b_values]

#title 

title = dict(
    title_name='D. Dumfries\n',
    title_color = 'red',
    subtitle_name = 'Inter\n2021/2022',
    subtitle_color = 'black',
    title_name_2='Average\n',
    title_color_2 = 'cornflowerblue',
    subtitle_name_2 = 'Serie A\n2021/2022',
    subtitle_color_2 = 'black',
    title_fontsize = 18,
    subtitle_fontsize=15
)

endnote = '@lambertsmarc\data via Wyscout\nMinimal 900 minutes played\nFB/Wide mid template'

radar = Radar()

fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                         radar_color=['red','cornflowerblue'],
                         alphas=[.7,.7],title=title,endnote=endnote,
                         compare=True)





plt.savefig('comparisonplotdumfriespre.png',dpi=1500,bbox_inches = 'tight', facecolor='#FFFFF0')
