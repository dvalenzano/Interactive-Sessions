
# Goal: to generate an input file for R to plot survival in G cross for the markers surrounding the sQTL
# This one is based on https://github.com/dvalenzano/Interactive-Sessions/blob/master/27-Oct-2014.py

aa_days = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_days2.csv', 'rU').read()
aa_daysM = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_daysM2.csv', 'rU').read()
aa_daysF = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_daysF2.csv', 'rU').read()


# In[4]:

aa_dayst = [list(i) for i in zip(* [ i.split(',') for i in aa_days.split('\n')[:-1]])]
aa_daysMt = [list(i) for i in zip(* [ i.split(',') for i in aa_daysM.split('\n')[:-1]])]
aa_daysFt = [list(i) for i in zip(* [ i.split(',') for i in aa_daysF.split('\n')[:-1]])]

import numpy
import scipy
import math


# In[5]:

# Now I need to select which markers to use for the analysis
# I will use the same as those defined as "peak"
peak = ['33911', '8423', '19589', '39073', '25587', '44971', '8178', '4179', '32767', '26568',
'26780', '2663', '36581', '12275', '34490', '39114', '10884', '2093', '6074', '18588',
'32724', '32599']


# In[7]:

m0 = aa_daysMt[:3]+[i for i in aa_daysMt[3:] if i[0] in peak]
f0 = aa_daysFt[:3]+[i for i in aa_daysFt[3:] if i[0] in peak]


# In[45]:

m1 = [list(i) for i in zip(*[[i[0]]+i[5:] for i in m0 ])]
f1 = [list(i) for i in zip(*[[i[0]]+i[5:] for i in f0 ])]


# In[46]:

m2 = ','.join([','.join(i)+'\n' for i in m1]).replace('\n,','\n')
f2 = ','.join([','.join(i)+'\n' for i in f1]).replace('\n,','\n')


# In[8]:

z = open('/Volumes/group_dv/personal/DValenzano/Nov2014/m_peakAA.csv', 'w')
z.write(m2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Nov2014/f_peakAA.csv', 'w')
z.write(f2)
z.close()


# In[ ]:



