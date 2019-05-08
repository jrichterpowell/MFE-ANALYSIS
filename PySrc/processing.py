'''
Processes old run data. The big idea is to treat the data as a sample space which we draw from to perform analysis. E.g. if I want to see how the car performed in the corners, I draw samples of the car running through corners (possibly many). This allows us to analyze many different time periods from the same perspective, which should provide more average analytics. 
'''

import matplotlib.pyplot as plt 
import pandas as pd 
import tools.py

racedata = pd.read_csv("/Users/colossal/Documents/Code/Python/MFE-VISUALS/Data.nosync/AllMorningRunsNoHead.csv") 

#PROCESSING DATA 

class Processing:

	#constructor takes rate as s / row (usually 0.002)	
	def __init__(self, rate):
		self.rate = rate

	#This function filters the data from the entire test, removing the periods where the car is stationary (within 'thresh' of 0 velocity) for more than t seconds.
	#Tried to do this nicely in O(n)
	def filter_stopped(self, df, time, thresh):
		a = b = int(df.index[0])
		intervals = []

		for row in df.itertuples():
			if row.GS < thresh:
				b += 1
			else:
				if a != b and ((b - a)*self.rate) > time:
					intervals.extend( [str(x) for x in range(a, b)])
				a = b
				b += 1
			if a != b and ((b - a)*self.rate) > time:
					intervals.extend( [str(x) for x in range(a, b)])

		print(intervals)
		#actually remove the intervals we marked
		df = df.drop(df.index(intervals), axis = 0)
		
		return df

	#Returns a list of indices which represent corners. A corner is defined here as deceleration combined with increased wheel angle, followed by wheel correction back towards 0 and acceleration.
	def find_corners(self,):
		pass

	#finds a point where speed is > mspd and the car goes from inside the ball of radius epsilon centered at that point, then returns to it after.
	def find_lap(self, df, epsilon, mspd):
		x = ()
		x_idx = 0
		idx = 0
		
		#find the first point.
		for i, row in enumerate(df.itertuples()):
			if row.GS < mspd:
				continue
			else:
				x = (row.GPSLo, row.GPSLa)
				x_idx = idx = i
				break
		
		#find the first index where we leave that epsilon ball
		for i,row in enumerate(df[idx:].itertuples()):

			y=(row.GPSLo,row.GPSLa)

			if distance(x,y) > epsilon:
				idx = i
				break

		print (x, x_idx, idx)
		#find the index where we return.
		for i,row in enumerate(df[idx:].itertuples()):
			y=(row.GPSLo, row.GPSLa)
			if distance(x,y) < epsilon:
				return (x_idx, i)
		return None



