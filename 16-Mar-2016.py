
# coding: utf-8

# In[1]:

import numpy as np
from scipy.stats.stats import pearsonr
from scipy import stats
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:

rna = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_fpkm_genes_sorted.csv', 'rU').read()
otu = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_merged_otu_table_sorted.csv','rU').read()

rnal = [i.split(',') for i in rna.split('\n')] #that's a "l" as in "L"
otul = [i.split(',') for i in otu.split('\n')]

rnat = [ list(i) for i in zip(*rnal)]
otut = [list(i) for i in zip(*otul) ]

rnat_z = [ map(float, i[1:]) for i in rnat[1:] if i.count('0') < 8]
otut_z = [ map(float, i[1:]) for i in otut[1:] if i.count('0') < 8]


# In[32]:

rna_key = [i[0] for i in rnat[1:] if i.count('0') < 8]
otu_key = [ i[0] for i in otut[1:] if i.count('0') < 8]

rna_value = rnat_z
otu_value = otut_z

rna_d = dict(zip(rna_key, rna_value))
otu_d = dict(zip(otu_key, otu_value))


# In[26]:

def loop_one(m1,otu): # this returns all the correlation coefficients between m1 and a given otu (otu)
    ls = []
    for i in m1:
        ls.append(stats.linregress(i, otu))    
    return ','.join(map(str, ls))+'\n'

def loop_two(m1, m2):
    ls = []
    for j in m2:
        ls.append(loop_one(m1, j))
    return ','.join(ls).replace('\n,','\n')


# In[27]:

fpkmvsotu = loop_two(rnat_z, otut_z)


# In[ ]:

z = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/regr.csv','w')
z.write(fpkmvsotu)
z.close()


# In[33]:

class reg(object):
    
    """
    This class uses as input a linear regression file obtained by the loop_two function and returns 
    regression tables and plots, given specific parameteres, such as R-squared value, p-value, OTU or 
    transcript
    """
    
    version = 0.1
    
    def __init__(self, inp):
        self.inp = inp 
        self.inp2 = [ i.split('LinregressResult')[1:] for i in self.inp.split('\n')[:-1]] 
        def loop1(inp, n):
            ls = []
            for i in inp:
                ls.append(i.split(',')[n].split('=')[1])
            return ','.join(ls).replace(')', '')
        def loop2(inp, n):
            ls = []
            for i in inp:
                ls.append(loop1(i, n))
            return ls
        self.slope =  [map(float, i.split(',')) for i in loop2(self.inp2, 0)]
        self.intercept = [map(float, i.split(',')) for i in loop2(self.inp2, 1)]
        self.rvalue = [map(float, i.split(',')) for i in loop2(self.inp2, 2)]
        self.rsquare = [ map(lambda x: x**2, i) for i in self.rvalue]
        self.pvalue = [map(float, i.split(',')) for i in loop2(self.inp2, 3)]
        self.stderr0 = [map(float, i.split(',')) for i in loop2(self.inp2, 4)  ]     
        
        
def filt(inp, thr, sign): #filter p-values, r-values and so forth based on a chosen threshold
    ar = np.array(inp)
    ls = []
    if sign == '>':
        ls = zip(*np.where(ar > thr))
    elif sign == '<':
        ls = zip(*np.where(ar < thr))
    else: 
        print "Error: check your input file"
    return ls


# In[34]:

Fc = reg(fpkmvsotu)


# In[35]:

Fr2 = Fc.rsquare
Fr2_thr07 = filt(Fr2, 0.7, '>')


# In[36]:

P = [otu_key[i[0]]+','+rna_key[i[1]]  for i in Fr2_thr07 ]


# In[42]:

X = np.array(otu_d[P[0].split(',')[0]])
Y = np.array(rna_d[P[0].split(',')[1]])
plt.scatter(X,Y)


# In[ ]:

plt.show()


# In[40]:

P[:15]


# I want to now check the distribution of the p-values 

# In[ ]:



