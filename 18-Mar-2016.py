
# coding: utf-8

# In[1]:

import numpy as np
from scipy.stats.stats import pearsonr
from scipy import stats
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:

rna = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_fpkm_genes_sorted.csv', 'rU').read()
otu = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_merged_otu_table_sorted.csv','rU').read()

rnal = [i.split(',') for i in rna.split('\n')] #that's a "l" as in "L"
otul = [i.split(',') for i in otu.split('\n')]

rnat = [ list(i) for i in zip(*rnal)]
otut = [list(i) for i in zip(*otul) ]

rnat_z = [ map(float, i[1:]) for i in rnat[1:] if i.count('0') < 8]
otut_z = [ map(float, i[1:]) for i in otut[1:] if i.count('0.0') < 8]


# In[10]:

rna_key = [i[0] for i in rnat[1:] if i.count('0') < 8]
otu_key = [ i[0] for i in otut[1:] if i.count('0.0') < 8]

rna_value = rnat_z
otu_value = otut_z

rna_d = dict(zip(rna_key, rna_value))
otu_d = dict(zip(otu_key, otu_value))


# In[4]:

fpkmvsotu = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/regr.csv','rU').read()


# In[336]:

class reg(object):
    
    """
    This class uses as input a linear regression file obtained by the loop_two function and returns 
    regression tables and plots, given specific parameteres, such as R-squared value, p-value, OTU or 
    transcript
    """
    
    version = 0.1
    
    def __init__(self, inp):
        self.inp = inp 
        self.inp2 = [ i.split('(') for i in self.inp.split('\n')[:-1]] 
    
        def loop1(inp, n):
            ls = []
            for i in inp[1:]:
                ls.append(i.split(',')[n])
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
        self.stderr = [map(float, i.split(',')) for i in loop2(self.inp2, 4)  ]     
        
        
# def filt(inp, thr, sign): #filter p-values, r-values and so forth based on a chosen threshold
#     ar = np.array(inp)
#     ls = []
#     if sign == '>':
#         ls = zip(*np.where(ar > thr))
#     elif sign == '<':
#         ls = zip(*np.where(ar < thr))
#     else: 
#         print "Error: check your input file"
#     return ls

def filt_(inp, thr, sign): #filter p-values, r-values and so forth based on a chosen threshold
    ar = np.array(inp)
    li = []
    lp = []
    if sign == '>':
        lp = np.where(ar > thr)
    elif sign == '<':
        lp = np.where(ar < thr)
    else: 
        print "Error: check your input file"
    p1_l = [ list(i) for i in lp]
    la = list(ar[p1_l])
    p2 = p1_l+[la]
    p3 = [ list(i) for i in zip(*p2)]
    p4 = sorted(p3, key=lambda x: x[2])
    return ','.join([ ','.join(map(str, i))+'\n' for i in p4]).replace('\n,','\n')[:-1]
    


# In[161]:

rf = reg(fpkmvsotu)


# In[340]:

rpval = filt_(rf.rsquare, 0.7, '>')
P2 = [otu_key[int(i.split(',')[0])]+','+rna_key[int(i.split(',')[1])] +','+i.split(',')[2] for i in rpval.split('\n') ]
P3 = ','.join([ i+'\n' for i in P2]).replace('\n,','\n')[:-1]
len(P3.split('\n'))


# In[346]:

rpval = filt_(rf.pvalue, 0.001, '<')
P2 = [otu_key[int(i.split(',')[0])]+','+rna_key[int(i.split(',')[1])] +','+i.split(',')[2] for i in rpval.split('\n') ]
P3 = ','.join([ i+'\n' for i in P2]).replace('\n,','\n')[:-1]
len(P3.split('\n'))


# In[347]:

zpvalue = 'OTU,transcr,value\n'+','.join([i+'\n'for i in P3.split('\n')[:100]]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/TOP_otu-tr_pvalue.csv', 'w')
z.write(zpvalue)
z.close()


# In[ ]:




# In[ ]:



