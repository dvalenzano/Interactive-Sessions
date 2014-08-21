#Goal: to get cumulative q-value with Fisher's method for the aa and g random forest data.  


# coding: utf-8

# In[ ]:

import math
import numpy
import scipy
from scipy.stats import chisqprob


# In[87]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_g.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_aa.csv', 'rU').read()


# In[88]:

def chisq_rf2(input):
    st = -2*sum([math.log(i) for i in map(float, input.split(',')[-4:])])
    if st == -0.0:
        st1 = 0.0
    else:
        st1 = st
    return st1


# In[91]:

g_combined = g.split('\n')[0]+',Chisq\n'+','.join([i+ ','+ str(chisq_rf2(i)) +'\n' for i in g.split('\n')[1:-1]]).replace('\n,','\n')
aa_combined = g.split('\n')[0]+',Chisq\n'+','.join([i+ ','+ str(chisq_rf2(i)) +'\n' for i in aa.split('\n')[1:-1]]).replace('\n,','\n')


# In[95]:

def addChisq(inp):
    ls = [i + ','+ str(chisqprob(float(i.split(',')[-1]), 8)) for i in inp.split('\n')[1:-1]]
    return inp.split('\n')[0]+',comb-pval\n'+','.join([i+'\n' for i in ls]).replace('\n,','\n')


# In[96]:

g_comb_pval = addChisq(g_combined)
aa_comb_pval = addChisq(aa_combined)


# In[97]:

z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/g_rf_qval.csv', 'w')
z.write(g_comb_pval)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/aa_rf_qval.csv', 'w')
z.write(aa_comb_pval)
z.close()


# In[85]:




# In[ ]:



