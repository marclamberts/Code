#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:50:30 2021

@author: lamberts_888
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mplsoccer.pitch import Pitch

from sklearn.cluster import KMeans

df = pd.read_excel('Pass cluster roma.xlsx')

df = df.loc[(df['playerId']==92329)].reset_index()

df['x'] = df['x']*1.2
df['y'] = df['y']*.8
df['endX'] = df['endX']*1.2
df['endY'] = df['endY']*.8

df.columns

df['x'] = df.loc[:,'x'] 
df['y'] = df.loc[:,'y'] 
df['endX'] = df.loc[:,'endX'] 
df['endY'] = df.loc[:,'endY'] 

df.head()


X = np.array(df[['x','y','endX','endY']])
kmeans = KMeans(n_clusters = 4,random_state=100)
kmeans.fit(X)
df['cluster'] = kmeans.predict(X)

df.head()

df.cluster.value_counts()

fig, ax = plt.subplots(figsize=(10,10))
fig.set_facecolor('#000000')
ax.patch.set_facecolor('#000000')

pitch = Pitch(pitch_type='statsbomb',orientation='horizontal',
             pitch_color='#000000',line_color='white',figsize=(10,10),
             constrained_layout=False,tight_layout=True,view='full')

pitch.draw(ax=ax)

plt.gca().invert_yaxis()
for x in range(len(df['cluster'])):
    
    if df['cluster'][x] ==3:
        pitch.lines(xstart=df['x'][x],ystart=df['y'][x],xend=df['endX'][x],yend=df['endY'][x],
                   color='blue',lw=3,zorder=2,comet=True,ax=ax)

    if df['cluster'][x] ==2:
        pitch.lines(xstart=df['x'][x],ystart=df['y'][x],xend=df['endX'][x],yend=df['endY'][x],
                   color='red',lw=3,zorder=2,comet=True,ax=ax)        
plt.savefig('roma1.png',dpi=500,bbox_inches = 'tight',)
        
plt.title('AS Roma most common pass cluster vs Man City ',color='white',size=20)