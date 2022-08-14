#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:43:53 2021

@author: lamberts_888
"""
import pandas as pd
import numpy as np

# import data
df = pd.read_excel("MC22.xlsx")

# preprocess the dataframe so we only have the data we want
# We want to get it down to be only successful passes made by Bruno Penandes
# we can use pandas .loc method to achieve this with a bunch of & statements

#df = df.loc[(df['teamId']==212) & (df['playerId']==85470) & (df['outcomeType/displayName']=='Successful') & (df['type/displayName']=='Pass')]

#Import xT Grid, turn it into an array, and then get how many rows and columns it has
xT = pd.read_csv("xT_grid.csv", header=None)
xT = np.array(xT)
xT_rows, xT_cols = xT.shape
xT

print(xT_rows,xT_cols)

df['x1_bin'] = pd.cut(df['x'], bins=xT_cols, labels=False)
df['y1_bin'] = pd.cut(df['y'], bins=xT_rows, labels=False)
df['x2_bin'] = pd.cut(df['endX'], bins=xT_cols, labels=False)
df['y2_bin'] = pd.cut(df['endY'], bins=xT_rows, labels=False)

df['start_zone_value'] = df[['x1_bin', 'y1_bin']].apply(lambda x: xT[x[1]][x[0]], axis=1)
df['end_zone_value'] = df[['x2_bin', 'y2_bin']].apply(lambda x: xT[x[1]][x[0]], axis=1)

df['xT'] = df['end_zone_value'] - df['start_zone_value']

df.head()

df.to_excel("MC222.xlsx")