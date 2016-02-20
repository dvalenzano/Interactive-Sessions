# This is connected to the OTU_density.R file
# coding: utf-8

# In[ ]:

import numpy as np
import matplotlib
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt


# In[10]:

class avg(object):
    
    """ Takes groups of individuals sequenced within a
    given category and returs the average values for each OTU """
    
    def __init__(self, cl):
        self.cl = [ list(i) for i in zip(*cl)]
        self.avg = [ np.mean(map(float, i)) for i in self.cl[1:]]   


# In[4]:

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


# BELOW, USING THE OTUs INSTEAD OF THE PHYLA

# In[19]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

WT6 = avg(WT_6wk)
wt6 = WT6.avg

wt_16_wt_6_f = [float(wt16[i])/float(wt6[i]) for i in range(len(wt16)) if wt6[i] != 0.0]
inp = [i for i in np.log2(wt_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_wt16_wt6 = 'wt16_wt6_otu,'+','.join([str(i) for i in inp])
out_wt16_wt6 = out_wt16_wt6.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityOTU_wt16_wt6.csv', 'w')
z.write(out_wt16_wt6)
z.close()


# In[20]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

YT16 = avg(YT_16wk)
yt16 = YT16.avg

wt_16_yt_16_f = [float(wt16[i])/float(yt16[i]) for i in range(len(wt16)) if yt16[i] != 0.0]
inp = [i for i in np.log2(wt_16_yt_16_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_wt16_yt16 = 'wt16_yt16_otu,'+','.join([str(i) for i in inp])
out_wt16_yt16 = out_wt16_yt16.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityOTU_wt16_yt16.csv', 'w')
z.write(out_wt16_yt16)
z.close()


# In[21]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

SM16 = avg(SM_16wk)
sm16 = SM16.avg

wt_16_sm_16_f = [float(wt16[i])/float(sm16[i]) for i in range(len(wt16)) if sm16[i] != 0.0]
inp = [i for i in np.log2(wt_16_sm_16_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_wt16_sm16 = 'wt16_sm16_otu,'+','.join([str(i) for i in inp])
out_wt16_sm16 = out_wt16_sm16.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityOTU_wt16_sm16.csv', 'w')
z.write(out_wt16_sm16)
z.close()


# In[22]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

ABX16 = avg(ABX_16wk)
abx16 = ABX16.avg

wt_16_abx_16_f = [float(wt16[i])/float(abx16[i]) for i in range(len(wt16)) if abx16[i] != 0.0]
inp = [i for i in np.log2(wt_16_abx_16_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_wt16_abx16 = 'wt16_abx16_otu,'+','.join([str(i) for i in inp])
out_wt16_abx16 = out_wt16_abx16.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityOTU_wt16_abx16.csv', 'w')
z.write(out_wt16_abx16)
z.close()


# In[33]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

YT16 = avg(YT_16wk)
yt16 = YT16.avg

wt_16_yt_16_f = [float(wt16[i])/float(yt16[i]) for i in range(len(wt16)) if yt16[i] != 0.0]
inp = [i for i in np.log2(wt_16_yt_16_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_wt16_yt16 = 'wt16_yt16_otu,'+','.join([str(i) for i in inp])
out_wt16_yt16 = out_wt16_yt16.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityOTU_wt16_yt16.csv', 'w')
z.write(out_wt16_yt16)
z.close()


# DOWN TO LEVEL 6

# In[23]:

otu_L6 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_tables/table_mc4000_sorted_L6.txt', 'rU').read()


# In[7]:

otuL6 = otu_L6.replace('\t',',').split('\n')[:-1]
otuL6a = [ i.split(',') for i in otuL6]
otuL6at = [ list(i) for i in zip(*otuL6a)]


# In[8]:

SM_10wk_L6 = [i for i in otuL6at if i[0][:8]== 'SM.10wk.']
SM_16wk_L6 = [i for i in otuL6at if i[0][:8]== 'SM.16wk.']
YT_10wk_L6 = [i for i in otuL6at if i[0][:8]== 'YM.10wk.']
YT_16wk_L6 = [i for i in otuL6at if i[0][:8]== 'YM.16wk.']
WT_6wk_L6 = [i for i in otuL6at if i[0][:7]== 'YI.6wk.']
WT_9wk_L6 = [i for i in otuL6at if i[0][:7]== 'WT.9wk.']
WT_10wk_L6 = [i for i in otuL6at if i[0][:8]== 'WT.10wk.']
WT_16wk_L6 = [i for i in otuL6at if i[0][:8]== 'WT.16wk.']
ABX_10wk_L6  = [i for i in otuL6at if i[0][:9]== 'ABX.10wk.']
ABX_16wk_L6  = [i for i in otuL6at if i[0][:9]== 'ABX.16wk.']


# In[12]:

WT16_L6 = avg(WT_16wk_L6)
wt16_L6 = WT16_L6.avg

WT6_L6 = avg(WT_6wk_L6)
wt6_L6 = WT6_L6.avg

wt_16_6_L6 = [wt16_L6[i]-wt6_L6[i] for i in range(len(wt6_L6))]


# In[24]:

WT16_L6 = avg(WT_16wk_L6)
wt16_L6 = WT16_L6.avg

WT6_L6 = avg(WT_6wk_L6)
wt6_L6 = WT6_L6.avg

L6wt_16_wt_6_f = [float(wt16_L6[i])/float(wt6_L6[i]) for i in range(len(wt16_L6)) if wt6_L6[i] != 0.0]
inp = [i for i in np.log2(L6wt_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

L6out_wt16_wt6 = 'L6wt16_wt6_otu,'+','.join([str(i) for i in inp])
L6out_wt16_wt6 = L6out_wt16_wt6.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityL6_wt16_wt6.csv', 'w')
z.write(L6out_wt16_wt6)
z.close()


# In[30]:

WT16_L6 = avg(WT_16wk_L6)
wt16_L6 = WT16_L6.avg

YT16_L6 = avg(YT_16wk_L6)
yt16_L6 = YT16_L6.avg

L6wt_16_wt_6_f = [float(wt16_L6[i])/float(yt16_L6[i]) for i in range(len(wt16_L6)) if yt16_L6[i] != 0.0]
inp = [i for i in np.log2(L6wt_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
#inp = [ i for i in inp if i != '-inf']
#inp = map(float, inp)
len(inp)
#plt.hist(inp, bins = 5)
#plt.show()

#L6out_wt16_yt16 = 'L6wt16_yt16_otu,'+','.join([str(i) for i in inp])
#L6out_wt16_yt16 = L6out_wt16_yt16.replace(',','\n')

#z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/densityL6_wt16_yt16.csv', 'w')
#z.write(L6out_wt16_yt16)
#z.close()


# In[ ]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

WT6 = avg(WT_6wk)
wt6 = WT6.avg

wt_16_wt_6_f = [float(wt16[i])/float(wt6[i]) for i in range(len(wt16)) if wt6[i] != 0.0]
inp = [i for i in np.log2(wt_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_wt16_wt6 = 'wt16_wt6_otu,'+','.join([str(i) for i in inp])
out_wt16_wt6 = out_wt16_wt6.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_wt16_wt6.csv', 'w')
z.write(out_wt16_wt6)
z.close()


# Now against the wt young, no more against the old, OTU

# In[40]:

WT6 = avg(YT_16wk)
wt6 = WT6.avg

yt_16_wt_6_f = [float(yt16[i])/float(wt6[i]) for i in range(len(yt16)) if wt6[i] != 0.0]
inp = [i for i in np.log2(yt_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_yt_16_wt_6_f = 'yt_16_wt_6_f,'+','.join([str(i) for i in inp])
out_yt_16_wt_6_f = out_yt_16_wt_6_f.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_yt_16_wt_6_f.csv', 'w')
z.write(out_yt_16_wt_6_f)
z.close()


# In[41]:

WT16 = avg(WT_16wk)
wt16 = WT16.avg

WT6 = avg(WT_6wk)
wt6 = WT6.avg

wt_16_wt_6_f = [float(wt16[i])/float(wt6[i]) for i in range(len(wt16)) if wt6[i] != 0.0]
inp = [i for i in np.log2(wt_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_wt16_wt6 = 'wt16_wt6_otu,'+','.join([str(i) for i in inp])
out_wt16_wt6 = out_wt16_wt6.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_wt16_wt6.csv', 'w')
z.write(out_wt16_wt6)
z.close()


# In[44]:

SM16 = avg(WT_16wk)
sm16 = SM16.avg

WT6 = avg(SM_16wk)
wt6 = WT6.avg

sm_16_wt_6_f = [float(sm16[i])/float(wt6[i]) for i in range(len(sm16)) if wt6[i] != 0.0]
inp = [i for i in np.log2(sm_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
inp
#plt.hist(inp, bins = 5)
#plt.show()

out_sm16_wt6 = 'sm16_wt6_otu,'+','.join([str(i) for i in inp])
out_sm16_wt6 = out_sm16_wt6.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_sm16_wt6.csv', 'w')
z.write(out_sm16_wt6)
z.close()


# In[45]:

ABX16 = avg(ABX_16wk)
abx16 = ABX16.avg

abx_16_wt_6_f = [float(abx16[i])/float(wt6[i]) for i in range(len(abx16)) if wt6[i] != 0.0]
inp = [i for i in np.log2(abx_16_wt_6_f).tolist()]
inp = [str(i) for i in inp]
inp = [ i for i in inp if i != '-inf']
inp = map(float, inp)
#inp
#plt.hist(inp, bins = 5)
#plt.show()

out_abx16_wt6 = 'abx16_wt6_otu,'+','.join([str(i) for i in inp])
out_abx16_wt6 = out_abx16_wt6.replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/OTU_abx16_wt6.csv', 'w')
z.write(out_abx16_wt6)
z.close()


# In[47]:




# In[ ]:



