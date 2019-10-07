import pandas as pd
import numpy as np
import csv

df=pd.read_csv("TrainingData_new.csv")
print(df.shape)

sdf=df.drop(["LONGITUDE","LATITUDE","FLOOR","BUILDINGID","SPACEID","SPACEID","RELATIVEPOSITION","USERID","PHONEID","TIMESTAMP"],axis="columns")
#only choose necessary column

sdf["nonezero"]=sdf.ne(0).sum(axis="columns")
#print(sdf["nonezero"])
#find the ne(none equal 0) to find the value

ans= pd.Series(sdf["nonezero"])
#print(ans)
print(ans.value_counts().sort_index())
#value_counts is a function which is used to count the series and sort the count of series

ans.value_counts().sort_index().to_csv('Result.csv')
#transfer the count to csv