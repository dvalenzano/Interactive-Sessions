
# coding: utf-8 - Developed with ipython

# In[1]:

You can download the data 
data = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Jun2015/simul/surv.csv', 'rU').read()


# In[30]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import math


# turn the table in an array

# In[7]:

datal = [i.split(',') for i in data.split('\n')[:-1] ]
age = [i[0] for i in datal]
n = [i[1] for i in datal]


# Now I derive survival, survival rate, death rate and logarithm of the death rate

# In[12]:

surv = [float(i)/float(n[1])*100 for i in n[1:]]
relsurv = [i/100.0  for i in surv]
deathr = [0.0]+[ (surv[i-1]-surv[i])/surv[i-1] for i in range(1,len(surv))]
logdr = [math.log1p(i)  for i in deathr]


# Plotting all the above

# In[54]:

plt.scatter(age[1:], deathr, color='k', label="death rate")
plt.scatter(age[1:], relsurv, color= 'g', label="survival rate")
plt.scatter(age[1:], logdr, color= 'b', label="log(death rate)")
legend(bbox_to_anchor=(0.7, 1.0), loc=1, borderaxespad=0.)
plt.show()


# In[ ]:



