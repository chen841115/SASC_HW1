import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pylab

df=pd.read_csv('TrainingData_new.csv')

dff=df[['WAP087','BUILDINGID']]
#print(dff)


use2=dff.loc[dff['BUILDINGID'] == 2]
#use1=dff.loc[dff['BUILDINGID'] == 1]
#use0=dff.loc[dff['BUILDINGID'] == 0]
#print(use1)
ans2=use2.count()
#ans1=use1.count()
#ans0=use0.count()
print(ans2)
#print(ans1)
#print(ans0)



dfnew = pd.DataFrame(columns=['X','total'])



#first forloop for range
#second forloop calculate the number bewtween the range
#build2=[]
sum1=0

for dec in range(-105,5,5):
    
    # eg.number for [-100,95) equals to (total number < -95) minus (to total number < -100) 
    a=Counter(use2['WAP087']< dec)
    b=Counter(use2['WAP087']<(dec+5))
    #print(a)
    #print(b)
    atrue=a[True]
    btrue=b[True]
    ctrue=btrue-atrue
    #print(ctrue)
    sum1=sum1+ctrue
    #print(sum)
    #print(atrue)
    #print(btrue)
       
    str1 = " [ %d ~ %d ) : %d" %(dec,(dec+5),sum1)
    print(str1)
    #dfnew=dfnew.append({},ignore_index=True)
    dfnew=dfnew.append({'X': ('['+str(dec)+'~'+str(dec+5)+')'),'total': sum1}, ignore_index=True)
    
    
    sum1=0

     
#dfnew.rename(index={1: 'a'})                      
#print(dfnew)

# PDF
dfnew['pdf'] = dfnew['total'] / sum(dfnew['total'])

# CDF
dfnew['cdf'] = dfnew['pdf'].cumsum()
print(dfnew)
major_ticks = np.arange(0, 1.2, 0.1)
minor_ticks = np.arange(0, 1.2, 0.01)
mm=dfnew.plot.bar(x = 'X', y = ['pdf', 'cdf'])
mm.set_ylim(0,1.2)
mm.set_yticks(major_ticks)
mm.set_yticks(minor_ticks, minor=True)
mm.grid(which='both')

pylab.show()
