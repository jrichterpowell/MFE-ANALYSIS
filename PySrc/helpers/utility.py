import csv
import pandas as pd
import numpy as np

#loads the csv into a pandas dataframe, converting all fields into floats by removing the units from the header
def loadFromCsv(filepath):
    df = pd.read_csv(filepath, skiprows=12,sep=',')[1:].astype(float)

    #immediately clean all zero columns to save memory
    return df.loc[:,(df != 0).any(axis=0)]    

def distance(x,y):
    if len(x) != len(y):
        print("Invalid Distance Computation on Points of Different Dimension")
    else:
        return np.sqrt( sum([ (i-j)**2 for i,j in zip(x,y)]))

colours = ['#00E5E3', '#0DE1CC', '#1ADDB5','#28D99E', '#35D588', '#43D271', '#50CE5A', '#5DCA44', '#6BC62D', '#78C216', '#86BF00'] 

In [417]: ent_speeds                                                                                                                                                                 
Out[417]: 
[65.31050287868078,
 63.22453400204951,
 51.34475096536379,
 52.550628394172556,
 51.084509276454575,
 71.64735196362362,
 50.45397074239964,
 61.70915052945064,
 41.96190119943908,
 45.66607689163669]

 [65.14514846576783,
 60.743040143523196,
 49.00092242232039,
 49.71946046214715,
 67.2480634769169,
 64.13118435925496,
 59.89686456752491,
 53.45055981533011,
 46.14482261090722,
 77.4274537998564]