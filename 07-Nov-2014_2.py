# Goal: to generate an input file for R to plot survival in G cross for the markers in control regions in LG3 for cross AA, i.e. not in the sQTL
# This one is based on https://github.com/dvalenzano/Interactive-Sessions/blob/master/05-Nov-2014.py

aa_days = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_days2.csv', 'rU').read()
aa_daysM = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_daysM2.csv', 'rU').read()
aa_daysF = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_daysF2.csv', 'rU').read()


# In[2]:

aa_dayst = [list(i) for i in zip(* [ i.split(',') for i in aa_days.split('\n')[:-1]])]
aa_daysMt = [list(i) for i in zip(* [ i.split(',') for i in aa_daysM.split('\n')[:-1]])]
aa_daysFt = [list(i) for i in zip(* [ i.split(',') for i in aa_daysF.split('\n')[:-1]])]

import numpy
import scipy
import math


# In[4]:

# Now I need to select which markers to use for the analysis
# I will use the same as those defined as "peak"
peak = ['27839','39610','30997','30674','25041','22860','18891','11124','22990','18523','20516','1421','5858','8546','10922','38791','29887','16483','26784','37338']


# In[5]:

m0 = aa_daysMt[:3]+[i for i in aa_daysMt[3:] if i[0] in peak]
f0 = aa_daysFt[:3]+[i for i in aa_daysFt[3:] if i[0] in peak]

m1 = [list(i) for i in zip(*[[i[0]]+i[5:] for i in m0 ])]
f1 = [list(i) for i in zip(*[[i[0]]+i[5:] for i in f0 ])]

m2 = ','.join([','.join(i)+'\n' for i in m1]).replace('\n,','\n')
f2 = ','.join([','.join(i)+'\n' for i in f1]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Nov2014/AA-cross/m_notpeakAA.csv', 'w')
z.write(m2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Nov2014/AA-cross/f_notpeakAA.csv', 'w')
z.write(f2)
z.close()


# In[ ]:



