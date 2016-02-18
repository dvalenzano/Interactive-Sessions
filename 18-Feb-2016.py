
# coding: utf-8

# In[28]:

otu = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/otu_table_mc5_w_tax_no_pynast_failures.txt', 'rU').read()
#otu = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L2.txt', 'rU').read()


# In[2]:

otu = otu.replace('\t',',').split('\n')[1:-1]


# In[3]:

otua = [ i.split(',') for i in otu]
otuat = [ list(i) for i in zip(*otua)]


# First, I need to generate the average numbers of OTUs per class, rather than for individual.  
# The classes are defined as follows:

# In[4]:

SM_10wk = [i for i in otuat if i[0][:8]== 'SM.10wk.']
SM_16wk = [i for i in otuat if i[0][:8]== 'SM.16wk.']
YT_10wk = [i for i in otuat if i[0][:8]== 'YM.10wk.']
YT_16wk = [i for i in otuat if i[0][:8]== 'YM.16wk.']
WT_6wk = [i for i in otuat if i[0][:7]== 'YI.6wk.']
WT_9wk = [i for i in otuat if i[0][:7]== 'WT.9wk.']
WT_10wk = [i for i in otuat if i[0][:8]== 'WT.10wk.']
WT_16wk = [i for i in otuat if i[0][:8]== 'WT.16wk.']
ABX_10wk  = [i for i in otuat if i[0][:9]== 'ABX.10wk.']
ABX_16wk  = [i for i in otuat if i[0][:9]== 'ABX.16wk.']


# In[10]:

import numpy
import scipy


# In[6]:

ABX_16wk_t = [ list(i) for i in zip(*ABX_16wk)]
ABX16wk = [ numpy.mean(map(float, i)) for i in ABX_16wk_t[1:]]


# In[3]:

class avg(object):
    
    """ Takes groups of individuals sequenced within a
    given category and returs the average values for each OTU """
    
    def __init__(self, cl):
        self.cl = [ list(i) for i in zip(*cl)]
        self.avg = [ numpy.mean(map(float, i)) for i in self.cl[1:]]   


# In[8]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

WT6 = avg(WT_6wk)
wt6 = WT6.avg


# In[9]:

wt_16_6 = [wt16[i]-wt6[i] for i in range(len(wt6))]


# Plotting densities

# In[11]:

import numpy as np
import matplotlib
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt


# In[25]:

out1 = 'title,'+','.join([str(i) for i in wt_16_6])
out1 = out1.replace(',','\n')


# In[14]:

plt.hist(wt_16_6, bins=10)
plt.show()


# In[26]:

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/density1.csv', 'w')
z.write(out1)
z.close()


# In[6]:

otu_L2 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L2.txt', 'rU').read()


# In[7]:

otuL2 = otu_L2.replace('\t',',').split('\n')[:-1]
otuL2a = [ i.split(',') for i in otuL2]
otuL2at = [ list(i) for i in zip(*otuL2a)]


# In[8]:

SM_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'SM.10wk.']
SM_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'SM.16wk.']
YT_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'YM.10wk.']
YT_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'YM.16wk.']
WT_6wk_L2 = [i for i in otuL2at if i[0][:7]== 'YI.6wk.']
WT_9wk_L2 = [i for i in otuL2at if i[0][:7]== 'WT.9wk.']
WT_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'WT.10wk.']
WT_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'WT.16wk.']
ABX_10wk_L2  = [i for i in otuL2at if i[0][:9]== 'ABX.10wk.']
ABX_16wk_L2  = [i for i in otuL2at if i[0][:9]== 'ABX.16wk.']


# In[12]:

WT16_L2 = avg(WT_16wk_L2)
wt16_L2 = WT16_L2.avg

WT6_L2 = avg(WT_6wk_L2)
wt6_L2 = WT6_L2.avg

wt_16_6_L2 = [wt16_L2[i]-wt6_L2[i] for i in range(len(wt6_L2))]


# In[13]:

plt.hist(wt_16_6_L2, bins=10)
plt.show()


# In[14]:

out2 = 'title,'+','.join([str(i) for i in wt_16_6_L2])
out2 = out2.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityL2.csv', 'w')
z.write(out2)
z.close()


# In[15]:

otu_L3 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L3.txt', 'rU').read()
otuL3 = otu_L3.replace('\t',',').split('\n')[:-1]
otuL3a = [ i.split(',') for i in otuL3]
otuL3at = [ list(i) for i in zip(*otuL3a)]
SM_10wk_L3 = [i for i in otuL3at if i[0][:8]== 'SM.10wk.']
SM_16wk_L3 = [i for i in otuL3at if i[0][:8]== 'SM.16wk.']
YT_10wk_L3 = [i for i in otuL3at if i[0][:8]== 'YM.10wk.']
YT_16wk_L3 = [i for i in otuL3at if i[0][:8]== 'YM.16wk.']
WT_6wk_L3 = [i for i in otuL3at if i[0][:7]== 'YI.6wk.']
WT_9wk_L3 = [i for i in otuL3at if i[0][:7]== 'WT.9wk.']
WT_10wk_L3 = [i for i in otuL3at if i[0][:8]== 'WT.10wk.']
WT_16wk_L3 = [i for i in otuL3at if i[0][:8]== 'WT.16wk.']
ABX_10wk_L3  = [i for i in otuL3at if i[0][:9]== 'ABX.10wk.']
ABX_16wk_L3  = [i for i in otuL3at if i[0][:9]== 'ABX.16wk.']
WT16_L3 = avg(WT_16wk_L3)
wt16_L3 = WT16_L3.avg

WT6_L3 = avg(WT_6wk_L3)
wt6_L3 = WT6_L3.avg

wt_16_6_L3 = [wt16_L3[i]-wt6_L3[i] for i in range(len(wt6_L3))]
plt.hist(wt_16_6_L3, bins=10)
plt.show()


# In[16]:

otu_L4 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L4.txt', 'rU').read()
otuL4 = otu_L4.replace('\t',',').split('\n')[:-1]
otuL4a = [ i.split(',') for i in otuL4]
otuL4at = [ list(i) for i in zip(*otuL4a)]
SM_10wk_L4 = [i for i in otuL4at if i[0][:8]== 'SM.10wk.']
SM_16wk_L4 = [i for i in otuL4at if i[0][:8]== 'SM.16wk.']
YT_10wk_L4 = [i for i in otuL4at if i[0][:8]== 'YM.10wk.']
YT_16wk_L4 = [i for i in otuL4at if i[0][:8]== 'YM.16wk.']
WT_6wk_L4 = [i for i in otuL4at if i[0][:7]== 'YI.6wk.']
WT_9wk_L4 = [i for i in otuL4at if i[0][:7]== 'WT.9wk.']
WT_10wk_L4 = [i for i in otuL4at if i[0][:8]== 'WT.10wk.']
WT_16wk_L4 = [i for i in otuL4at if i[0][:8]== 'WT.16wk.']
ABX_10wk_L4  = [i for i in otuL4at if i[0][:9]== 'ABX.10wk.']
ABX_16wk_L4  = [i for i in otuL4at if i[0][:9]== 'ABX.16wk.']
WT16_L4 = avg(WT_16wk_L4)
wt16_L4 = WT16_L4.avg

WT6_L4 = avg(WT_6wk_L4)
wt6_L4 = WT6_L4.avg

wt_16_6_L4 = [wt16_L4[i]-wt6_L4[i] for i in range(len(wt6_L4))]
plt.hist(wt_16_6_L4, bins=10)
plt.show()


# In[17]:

otu_L5 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L5.txt', 'rU').read()
otuL5 = otu_L5.replace('\t',',').split('\n')[:-1]
otuL5a = [ i.split(',') for i in otuL5]
otuL5at = [ list(i) for i in zip(*otuL5a)]
SM_10wk_L5 = [i for i in otuL5at if i[0][:8]== 'SM.10wk.']
SM_16wk_L5 = [i for i in otuL5at if i[0][:8]== 'SM.16wk.']
YT_10wk_L5 = [i for i in otuL5at if i[0][:8]== 'YM.10wk.']
YT_16wk_L5 = [i for i in otuL5at if i[0][:8]== 'YM.16wk.']
WT_6wk_L5 = [i for i in otuL5at if i[0][:7]== 'YI.6wk.']
WT_9wk_L5 = [i for i in otuL5at if i[0][:7]== 'WT.9wk.']
WT_10wk_L5 = [i for i in otuL5at if i[0][:8]== 'WT.10wk.']
WT_16wk_L5 = [i for i in otuL5at if i[0][:8]== 'WT.16wk.']
ABX_10wk_L5  = [i for i in otuL5at if i[0][:9]== 'ABX.10wk.']
ABX_16wk_L5  = [i for i in otuL5at if i[0][:9]== 'ABX.16wk.']
WT16_L5 = avg(WT_16wk_L5)
wt16_L5 = WT16_L5.avg

WT6_L5 = avg(WT_6wk_L5)
wt6_L5 = WT6_L5.avg

wt_16_6_L5 = [wt16_L5[i]-wt6_L5[i] for i in range(len(wt6_L5))]
plt.hist(wt_16_6_L5, bins=10)
plt.show()


# In[18]:

otu_L2 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L2.txt', 'rU').read()
otuL2 = otu_L2.replace('\t',',').split('\n')[:-1]
otuL2a = [ i.split(',') for i in otuL2]
otuL2at = [ list(i) for i in zip(*otuL2a)]
SM_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'SM.10wk.']
SM_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'SM.16wk.']
YT_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'YM.10wk.']
YT_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'YM.16wk.']
WT_6wk_L2 = [i for i in otuL2at if i[0][:7]== 'YI.6wk.']
WT_9wk_L2 = [i for i in otuL2at if i[0][:7]== 'WT.9wk.']
WT_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'WT.10wk.']
WT_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'WT.16wk.']
ABX_10wk_L2  = [i for i in otuL2at if i[0][:9]== 'ABX.10wk.']
ABX_16wk_L2  = [i for i in otuL2at if i[0][:9]== 'ABX.16wk.']

SM16_L2 = avg(SM_16wk_L2)
sm16_L2 = SM16_L2.avg

YT16_L2 = avg(YT_16wk_L2)
yt16_L2 = YT16_L2.avg

yt_16_sm_16 = [yt16_L2[i]-sm16_L2[i] for i in range(len(yt16_L2))]
plt.hist(yt_16_sm_16, bins=10)
plt.show()


# In[20]:

otu_L2 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L2.txt', 'rU').read()
otuL2 = otu_L2.replace('\t',',').split('\n')[:-1]
otuL2a = [ i.split(',') for i in otuL2]
otuL2at = [ list(i) for i in zip(*otuL2a)]
SM_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'SM.10wk.']
SM_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'SM.16wk.']
YT_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'YM.10wk.']
YT_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'YM.16wk.']
WT_6wk_L2 = [i for i in otuL2at if i[0][:7]== 'YI.6wk.']
WT_9wk_L2 = [i for i in otuL2at if i[0][:7]== 'WT.9wk.']
WT_10wk_L2 = [i for i in otuL2at if i[0][:8]== 'WT.10wk.']
WT_16wk_L2 = [i for i in otuL2at if i[0][:8]== 'WT.16wk.']
ABX_10wk_L2  = [i for i in otuL2at if i[0][:9]== 'ABX.10wk.']
ABX_16wk_L2  = [i for i in otuL2at if i[0][:9]== 'ABX.16wk.']

SM16_L2 = avg(SM_16wk_L2)
sm16_L2 = SM16_L2.avg

WT16_L2 = avg(WT_16wk_L2)
wt16_L2 = WT16_L2.avg

wt_16_sm_16 = [wt16_L2[i]-sm16_L2[i] for i in range(len(wt16_L2))]
plt.hist(wt_16_sm_16, bins=5)
plt.show()


# In[ ]:



