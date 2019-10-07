import pandas as pd
import csv

df=pd.read_csv('TrainingData_new.csv')

sdf=df.drop(["LONGITUDE","LATITUDE","FLOOR","BUILDINGID","SPACEID","SPACEID","RELATIVEPOSITION","USERID","PHONEID","TIMESTAMP"],axis="columns")
#only choose necessary column

ans = sdf.mean()#.sort_values(ascending=True)
print(ans)

ans.to_csv('mean.csv')
#transfer the count to csv
