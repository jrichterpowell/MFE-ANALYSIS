'''
Processes old run data. The big idea is to treat the data as a sample space which we draw from to perform analysis. 
E.g. if I want to see how the car performed in the corners, I draw samples of the car running through corners (possibly many). 
This allows us to analyze many different time periods from the same perspective, which should provide more average (and general) analytics. 
'''

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

#smoothes points by averaging those in a window (i.e maps a dataframe with point every 0.002s to one with points every 0.1s if the window was 5)
def smooth_points(df, k):
	return df.groupby(df.index // k).mean()

#Returns a list of indices which represent corners. A corner is defined here as deceleration combined with increased wheel angle, followed by wheel correction back towards 0 and acceleration.
def find_corners(self,):
	pass

#removes intervals where the car is not traveling faster than `speed` for more than `period` seconds
def remove_stopped(df, period, speed, rate): 
    if period < rate: 
        print("Error") 
    df['GSmax'] = df['Ground Speed'].rolling(window=int(period/rate), center=True).max() 
    new_df = df[df['GSmax'] > speed] 
    del new_df['GSmax'] 
    return new_df 

def mark_turning(df, degree): 
    df['turn'] = np.where(np.abs(df['direction'].diff()) > degree, True, False) 
    return df 

def normalize(sr):
	return (sr - sr.min())/ (sr.max() - sr.min())

def distance(x,y):
    if len(x) != len(y):
        print("Invalid Distance Computation on Points of Different Dimension")
        print(x, y)
    else:
        return np.sqrt( sum([ (i-j)**2 for i,j in zip(x,y)]))