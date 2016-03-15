
# coding: utf-8

# **Calculation of correlation coefficients between OTUs and fpkm values from microbiome data**

# In[15]:

import numpy as np
from scipy.stats.stats import pearsonr


# In[1]:

rna = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_fpkm_genes_sorted.csv', 'rU').read()
otu = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_merged_otu_table_sorted.csv','rU').read()


# In[2]:

rna1 = map(float, [ i.split(',')[1] for i in rna.split('\n') ][1:]) #that's a "1" as in "one"
otu1 = map(float, [ i.split(',')[1] for i in otu.split('\n') ][1:])


# In[4]:

rnal = [i.split(',') for i in rna.split('\n')] #that's a "l" as in "L"
otul = [i.split(',') for i in otu.split('\n')]


# In[11]:

rnat = [ list(i) for i in zip(*rnal)][1:] 
otut = [list(i) for i in zip(*otul) ][1:]

rnaT = [map(float, i[1:]) for i in rnat]
otuT = [map(float, i[1:]) for i in otut]


# In[53]:

def loop_one(m1,otu): # this returns all the correlation coefficients between m1 and a given otu (otu)
    ls = []
    for i in m1:
        ls.append(np.corrcoef(i, otu)[0][1])    
    return ','.join(map(str, ls))+'\n'


# In[54]:

def loop_two(m1, m2):
    ls = []
    for j in m2:
        ls.append(loop_one(m1, j))
    return ','.join(ls).replace('\n,','\n')


# In[62]:

fpkmvsotu = loop_two(rnaT, otuT)


# Now I build the header (column name) and row name, as the transcripts and OTU IDs, respectively

# In[89]:

col = rnal[0][1:]
row = otul[0][1:]

drow = dict(zip(row, fpkmvsotu.split('\n')[:-1]))
dcol = dict(zip(col, [ list(i) for i in zip(*fpkmvsotu.split('\n')[:-1])]))


# In[104]:

fpkmvsotu_str = ','.join([','.join(map(str, i.split(',')))+'\n' for i in fpkmvsotu.split('\n')[:-1]]).replace('\n,','\n')[:-1]


# In[112]:

col_fpkmvsotu_str = ','.join(col)+'\n'+fpkmvsotu_str
row2 = ['OTU'] + row

len(row2) == len(col_fpkmvsotu_str.split('\n'))


# In[114]:

tab1 = [row2[i]+','+col_fpkmvsotu_str.split('\n')[i] for i in range(len(row2))]

# In[115]:

tab2 = ','.join([ i+'\n' for i in tab1]).replace('\n,','\n') 
z = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/correlation.csv', 'w')
z.write(tab2)
z.close()


# In[131]:

prova = [ i for i in range(len(drow[row[0]].split(','))) if abs(float(drow[row[0]].split(',')[i])) > 0.7]


# First, I want to check the distribution of all the correlation coefficients.

# In[135]:

import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt


# In[136]:

import seaborn as sns
sns.set(color_codes=True)


# In[145]:

fpkmvsotu_l = fpkmvsotu.replace('\n', ',').split(',')[:-1]


# In[148]:

fpkmvsotu_a = np.asarray(fpkmvsotu_l).astype(np.float)


# In[150]:

# Following instructions from: https://stanford.edu/~mwaskom/software/seaborn/tutorial/distributions.html
get_ipython().magic(u'matplotlib inline')
sns.distplot(fpkmvsotu_a); 
# sns.distplot(fpkmvsotu_a, hist=False, rug=True);


# Not very convincing distribution - somehow positive and negative correlations have highly different distributions

# Now I need a function that, given a correlation coefficient threshold - set as input - returns a list with all the matching pairs and allows for plotting the fpkm/OTU that are correlated, with the right title too.  
# Something like: pos(0.8), which would return a table with all the fpkm/otu that have r value > than 0.8.  neg(0.8) would return a table with all the fpkm/otu that have r value < than -0.8. all(0.8) would return a table with all the fpkm/otu that have |r value| > than 0.8.

# In[ ]:

fpkmvsotu_l2 = fpkmvsotu.split('\n')[:-1]


# In[ ]:

def rindex(row, thr):
    ls = list('%s') % str(row)
    for i in range(len(fpkmvsotu_l2[row].split(','))):
        if abs(float(fpkmvsotu_l2[row].split(',')[i])) > thr:
            ls.append(i)
    return ls

