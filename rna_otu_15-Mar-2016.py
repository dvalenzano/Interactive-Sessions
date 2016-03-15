
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns


# In[43]:

fp_tu = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/correlation.csv', 'rU').read()


# In[3]:

rna = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_fpkm_genes_sorted.csv', 'rU').read()
otu = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_merged_otu_table_sorted.csv','rU').read()

rnal = [i.split(',') for i in rna.split('\n')] #that's a "l" as in "L"
otul = [i.split(',') for i in otu.split('\n')]

rnat = [ list(i) for i in zip(*rnal)][1:] 
otut = [list(i) for i in zip(*otul) ][1:]

rnaT = [map(float, i[1:]) for i in rnat]
otuT = [map(float, i[1:]) for i in otut]


# In[48]:

fpkmvsotu = fp_tu
fpkmvsotu_l = fpkmvsotu.split('\n')[:-1]


# In[78]:

col = rnal[0][1:]
row = otul[0][1:]


# In[86]:

otu_key = otu.split('\n')[0].split(',')[1:]
otu_value = otuT
otu_d = dict(zip(otu_key, otu_value))

rna_key = rna.split('\n')[0].split(',')[1:]
rna_value = rnaT
rna_d = dict(zip(rna_key, rna_value))


# In[59]:

def rindex(row, thr):
    ts = '%s' % str(row)
    ls = list(ts)
    for i in range(1, len(fpkmvsotu_l[row].split(','))):
        if abs(float(fpkmvsotu_l[row].split(',')[i])) > thr:
            ls.append(i)
    return ls


# In[3]:

plt.scatter(rna_d[rna_key[1408]], otu_d[otu_key[0]])


# In[ ]:

plt.show()


# In[98]:

len(rna_key)


# In[7]:

from scipy import stats
import numpy as np
x = np.random.random(10)
y = np.random.random(10)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# To get coefficient of determination (r_squared)

print "p-value:", p_value


# In[8]:

prova =  stats.linregress(x,y)


# In[12]:

list(prova)+['f']


# In[ ]:



