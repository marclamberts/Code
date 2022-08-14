#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:56:43 2021

@author: lamberts_888
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import highlight_text

import matplotlib.font_manager
from IPython.core.display import HTML

def make_html(fontname):
    return "<p>{font}: <span style='font-family:{font}; font-size: 24px;'>{font}</p>".format(font=fontname)

code = "\n".join([make_html(font) for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])

df = pd.read_excel('LO1.xlsx')
#df2 = pd.read_excel('WSL MID KEY.xlsx')
df.head(10)

#split the player names
df['Player'] = df['Player'].str.split('\\',expand=True)[0]

print(df.head())

df.Player.unique()

#create a list of 6 metrics to compare
metrics = ['xA per 90','Assists per 90', 'Key passes per 90', 'Through passes per 90','Passes to final third per 90', 'Passes to penalty area per 90',]

fig,axes = plt.subplots(3,2,figsize=(14,10))
fig.set_facecolor('white')
#ax.patch.set_facecolor(background)

#set up our base layer
mpl.rcParams['xtick.color'] = 'black'
mpl.rcParams['ytick.color'] = 'black'

#create a list of comparisons
counter=0
counter2=0
met_counter = 0

for i,ax in zip(df['Player'],axes.flatten()):
    ax.set_facecolor('white')
    ax.grid(ls='dotted',lw=.5,color='black',axis='y',zorder=1)
    
    spines = ['top','bottom','left','right']
    for x in spines:
        if x in spines:
            ax.spines[x].set_visible(False)
            
    sns.swarmplot(x=metrics[met_counter],data=df,ax=axes[counter,counter2],zorder=1,color='#64645e')
    ax.set_xlabel(f'{metrics[met_counter]}',c='black')
    
    for x in range(len(df['Player'])):
     #   if df2['Player'][x] == 'Ji So-Yeon':
          #  ax.scatter(x=df2[metrics[met_counter]][x],y=0,s=200,c='#EC2227',zorder=2)
        if df['Player'][x] == 'L. Oberdorf':
            ax.scatter(x=df[metrics[met_counter]][x],y=0,s=200,c='#FF0000',zorder=2)
                        
    met_counter+=1
    if counter2 == 0:
        counter2 = 1
        continue
    if counter2 == 1:
        counter2 = 0
        counter+=1
        

        
s='<L. Oberdorf> Key passing stats BuLi 2021/2022'
highlight_text.fig_text(s=s,
                x=.05, y=.88,
                #highlight_weights = ['bold'],
                fontsize=32,
                fontfamily = 'Andale Mono',
                color = 'black',
                va='center'
               )

fig.text(.12,.05,"all stats per 90",fontsize=11, fontfamily='Andale Mono',color='black')
fig.text(.12,.03,"@lambertsmarc / data via Wyscout", fontstyle='italic',fontsize=15, fontfamily='Andale Mono',color='black')

plt.savefig('pernilleharderbeeswarmplot.png',dpi=500,bbox_inches = 'tight',facecolor='white')

