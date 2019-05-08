import csv
import pandas as pd
import numpy as np

#loads the csv into a pandas dataframe, converting all fields into floats by removing the units from the header
def loadFromCsv(filepath):
	df = pd.read_csv(filepath, skiprows=14,sep=',')[1:].astype(float)

	#immediately clean all zero columns to save memory
	for col in list(df):
		if (df[col] == 0).all():
			df.drop[col]
	return df

def distance(x,y):
	if len(x) != len(y):
		print("Invalid Distance Computation on Points of Different Dimension")
	else:
		return np.sqrt( sum([ (i-j)**2 for i,j in zip(x,y)]))

