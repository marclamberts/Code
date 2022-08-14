#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:51:31 2021

@author: lamberts_888
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import highlight_text

# the famous import font code to use Andale Mono
import matplotlib.font_manager
from IPython.core.display import HTML

def make_html(fontname):
    return "<p>{font}: <span style='font-family:{font}; font-size: 24px;'>{font}</p>".format(font=fontname)

code = "\n".join([make_html(font) for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])


#import data
df = pd.read_excel('NWSL.xlsx')

text_color = 'white'
background = '#000000'

#look at top of dataframe
df.head()

fig, ax = plt.subplots(figsize=(10,5))
fig.set_facecolor(background)
ax.patch.set_facecolor(background)

#set up our base layer
mpl.rcParams['xtick.color'] = text_color
mpl.rcParams['ytick.color'] = text_color

ax.grid(ls='dotted',lw=.5,color='lightgrey',axis='y',zorder=1)
spines = ['top','bottom','left','right']
for x in spines:
    if x in spines:
        ax.spines[x].set_visible(False)

sns.swarmplot(x='xGF',data=df,color='white',zorder=1)


#plot de bruyne
plt.scatter(x=7.65,y=0,c='blue',edgecolor='white',s=200,zorder=2)
plt.text(s='Gotham FC',x=7.65,y=-.04,c=text_color)

plt.title('xGF in NWSL 2021',c=text_color,fontsize=14)

plt.xlabel('Expected goals for',c=text_color)



#plt.savefig('swarm.png',dpi=500,bbox_inches = 'tight',facecolor=background)