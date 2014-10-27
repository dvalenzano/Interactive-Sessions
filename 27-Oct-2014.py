
# coding: utf-8

# In[1]:

# Goal: to generate an input file for R to plot survival in G cross for the markers surrounding the sQTL


# In[2]:

g_days = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_days2.csv', 'rU').read()
g_daysM = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_daysM2.csv', 'rU').read()
g_daysF = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_daysF2.csv', 'rU').read()


# In[3]:

g_dayst = [list(i) for i in zip(* [ i.split(',') for i in g_days.split('\n')[:-1]])]
g_daysMt = [list(i) for i in zip(* [ i.split(',') for i in g_daysM.split('\n')[:-1]])]
g_daysFt = [list(i) for i in zip(* [ i.split(',') for i in g_daysF.split('\n')[:-1]])]

import numpy
import scipy
import math


# In[7]:

# Now I need to select which markers to use for the analysis
# I will use the same as those defined as "peak" in file /Volumes/group_dv/personal/DValenzano/Oct2014/g_lg3_peak.fa
peak = ['26385', '25003', '46347', '12535', '13555', '31890', '17025']


# In[44]:

m0 = g_daysMt[:3]+[i for i in g_daysMt[3:] if i[0] in peak]
f0 = g_daysFt[:3]+[i for i in g_daysFt[3:] if i[0] in peak]


# In[45]:

m1 = [list(i) for i in zip(*[[i[0]]+i[5:] for i in m0 ])]
f1 = [list(i) for i in zip(*[[i[0]]+i[5:] for i in f0 ])]


# In[46]:

m2 = ','.join([','.join(i)+'\n' for i in m1]).replace('\n,','\n')
f2 = ','.join([','.join(i)+'\n' for i in f1]).replace('\n,','\n')


# In[48]:

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/m_peakG.csv', 'w')
z.write(m2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/f_peakG.csv', 'w')
z.write(f2)
z.close()


# In[ ]:



