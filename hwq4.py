import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pylab

df=pd.read_csv('TrainingData_new.csv')

c=df[['WAP087','BUILDINGID']]
#only choose necessary column

print(c)

BUILDINGID_0 = c.loc[c['BUILDINGID'] == 0]
BUILDINGID_1 = c.loc[c['BUILDINGID'] == 1]
BUILDINGID_2 = c.loc[c['BUILDINGID'] == 2]
print(BUILDINGID_0)