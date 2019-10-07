import pandas as pd
import numpy as np

df=pd.read_csv('TrainingData_new.csv')

sdf=df.drop(["LONGITUDE","LATITUDE","FLOOR","BUILDINGID","SPACEID","SPACEID","RELATIVEPOSITION","USERID","PHONEID","TIMESTAMP"],axis="columns")
#only choose necessary column

ltcount = np.linspace(0,0,110)
#Use a array to store the count of less then number

for i in range (-100,5,5):
    c = sdf.lt(i)
    for j in range (0,520):
        ltcount[-i] = ltcount[-i] + np.sum(c)[j]
#Find the count of less then (-100~0)

print("       <= x < %+3d : %d"%((-100),ltcount[100]))    
for i in range (-100,0,5):
    ans = ltcount[-(i+5)]-ltcount[-i]
    str = "  %+4d <= x < %+3d  : %d" %(i,(i+5),ans)
    print(str)
#Find the count of -(n+5)~-n which n is (100~0)