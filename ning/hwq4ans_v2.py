import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pylab

df=pd.read_csv('TrainingData_new.csv')

dff=df[['WAP087','BUILDINGID']]
print(dff)

# find the building we need 
use2=dff.loc[dff['BUILDINGID'] == 2]
#use1=dff.loc[dff['BUILDINGID'] == 1]
#use0=dff.loc[dff['BUILDINGID'] == 0]
#print(use1)
## just for make sure ans2+ans1+ans0 equals to 19937
ans2=use2.count()
#ans1=use1.count()
#ans0=use0.count()
#print(ans2)
#print(ans1)
#print(ans0)

# create a new dataframe
dfnew = pd.DataFrame(columns=['X','total'])

# forloop for range
sum1=0

for dec in range(-105,1):
    
    a=Counter(use2['WAP087']== dec)
    atrue=a[True]
    sum1=sum1+atrue
    #print(sum1)
    ##just for make sure the value is right
    #str1 = " %d: %d" %(dec,sum1)
    #print(str1)
    #dfnew=dfnew.append({},ignore_index=True)
    #store the value into dataframe
    dfnew=dfnew.append({'X': (str(dec)),'total': sum1}, ignore_index=True) 
    sum1=0

# PDF
dfnew['pdf'] = dfnew['total'] / sum(dfnew['total'])

# CDF
dfnew['cdf'] = dfnew['pdf'].cumsum()

print(dfnew)

#plot
##use python to plot (not necessary , we can get data from dfnew and draw it in excel)
major_ticks = np.arange(0, 1.1, 0.1)
minor_ticks = np.arange(0, 1.1, 0.05)
mm=dfnew.plot.bar(x = 'X', y = ['pdf', 'cdf'])
mm.set_ylim(0,1.2)
mm.set_yticks(major_ticks)
mm.set_yticks(minor_ticks, minor=True)
mm.grid(which='both')
pylab.show()
