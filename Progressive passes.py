#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:49:30 2021

@author: lamberts_888
"""
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mplsoccer import Pitch

import pandas as pd
import numpy as np
from mplsoccer.pitch import VerticalPitch
import matplotlib.pyplot as plt
from mplsoccer import Pitch

df = pd.read_csv('01-24-Jul-22-ColNew-event.csv')

#df.x = df.x*1.2
#df.y = df.y*.8
#df.endX = df.endX*1.2
#df.endY = df.endY*1.2

df.head()

df['beginning'] = np.sqrt(np.square(120-df['x']) + np.square(40 - df['y']))
df['end'] = np.sqrt(np.square(120 - df['endX']) + np.square(40 - df['endY']))


df['progressive'] = [(df['end'][x]) / (df['beginning'][x]) < .75 for x in range(len(df.beginning))]

df.head(20)

df = df.loc[df['type/displayName']=='Pass']
df = df.loc[df['TeamId']==1113]


df.head(20)

df = df.loc[df['progressive']==True].reset_index()

df.head()

pitch = Pitch(pitch_type='opta', pitch_color='#22312b', line_color='#c7d5cc', pad_top=8,)  # optional stripes
fig, ax = pitch.draw()
figsize=(13.5,8)

fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch.lines(df.x,df.y,df.endX,df.endY,comet=True, color='orange',ax=ax)
plt.suptitle('Columbus Crew progressive passes',color='white',size=18)
#df.to_excel("dcunited-pro.xlsx")
plt.savefig('NERprogressive passes.png', dpi = 1500, bbox_inches='tight',facecolor='#22312b')