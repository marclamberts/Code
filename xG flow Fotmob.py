#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:45:38 2022

@author: lamberts_888
"""
#import packages
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('heerenveensparta.csv')

df

#now that we have our dataframe set up, we are going to create some lists to plot the different xG values
#4 lists - home and away xg and minutes
#We start these with zero so our charts will start at 0
a_xG = [0]
h_xG= [0]
a_min = [0]
h_min = [0]


#this finds our team names from the dataframe. This will only work as long as both teams took a shot
hteam = df['team_id'].iloc[0]
ateam = df['team_id'].iloc[-1]

for x in range(len(df['expected_goals'])):
    if df['team_id'][x]==8614:
        a_xG.append(df['expected_goals'][x])
        a_min.append(df['min'][x])
    if df['team_id'][x]==10228:
        h_xG.append(df['expected_goals'][x])
        h_min.append(df['min'][x])
        
#this is the function we use to make our xG values be cumulative rather than single shot values
#it goes through the list and adds the numbers together
def nums_cumulative_sum(nums_list):
    return [sum(nums_list[:i+1]) for i in range(len(nums_list))]

a_cumulative = nums_cumulative_sum(a_xG)
h_cumulative = nums_cumulative_sum(h_xG)

#this is used to find the total xG. It just creates a new variable from the last item in the cumulative list
alast = round(a_cumulative[-1],2)
hlast = round(h_cumulative[-1],2)

fig, ax = plt.subplots(figsize = (10,5))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

#set up our base layer
mpl.rcParams['xtick.color'] ='white'
mpl.rcParams['ytick.color'] ='white'

ax.grid(ls='dotted',lw=.5,color='lightgrey',axis='y',zorder=1)
spines = ['top','bottom','left','right']
for x in spines:
    if x in spines:
        ax.spines[x].set_visible(False)

plt.vlines( ymin=0, ymax=1,x=45, color='white', alpha=0.1,linestyle="solid")

        
plt.xticks([0,15,30,45,60,75,90])
plt.xlabel('Minute',fontname='Andale Mono',color='white',fontsize=16)
plt.ylabel('xG',fontname='Andale Mono',color='white',fontsize=16)

#plot the step graphs8593d3d3d3
ax.step(x=a_min,y=a_cumulative,color='red',label=ateam,linewidth=5,where='post')
ax.step(x=h_min,y=h_cumulative,color='blue',label=hteam,linewidth=5,where='post')

#ax.set_title("England vs Austria \n 2,01 xG vs 0,36 xG", fontsize=25, color="w", fontfamily="Andale Mono", fontweight='bold', pad=8)
fig.text(.68,0.47,f'Heerenveen',fontstyle='italic',fontsize=14,fontfamily='Andale Mono', color='w')
fig.text(.85,0.43,f'Sparta',fontstyle='italic',fontsize=14,fontfamily='Andale Mono', color='w')
#fig.text(.79,0.43,f'1-0(77.)',fontstyle='italic',fontsize=14,fontfamily='Andale Mono', color='w')

#fig.text(.63,0.01,f'@lambertsmarc / twitter',fontstyle='italic',fontsize=14,fontfamily='Andale Mono', color='w')


plt.savefig('heespa2.png', dpi = 1500, bbox_inches='tight',facecolor='#22312b')