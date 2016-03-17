
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


# In[5]:

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


# In[6]:

rf = reg(fpkmvsotu)


# In[39]:

Rpval = filt(rf.pvalue, 0.00001, '<')


# In[40]:

P = [otu_key[i[0]]+','+rna_key[i[1]]  for i in Rpval ]


# In[43]:

X = np.array(otu_d[P[17].split(',')[0]])
Y = np.array(rna_d[P[17].split(',')[1]])
plt.scatter(X,Y)
plt.show()


# In[52]:

pv2 = ','.join([ ','.join(map(str, i)) for i in rf.pvalue ]).split(',')
pv2a = np.asarray(pv2).astype(np.float)


# In[54]:

sns.set(color_codes=True)
#ap = np.array(rf.pvalue)
sns.distplot(pv2a); 
plt.show()


# In[ ]:

Rrsq = filt(rf.rsquare, 0.8, '>')
P = [otu_key[i[0]]+','+rna_key[i[1]]  for i in Rrsq ]


# In[93]:

P


# In[77]:

X0 = np.array(otu_d[P[0].split(',')[0]])
Y0 = np.array(rna_d[P[0].split(',')[1]])

X1 = np.array(otu_d[P[1].split(',')[0]])
Y1 = np.array(rna_d[P[1].split(',')[1]])

X2 = np.array(otu_d[P[2].split(',')[0]])
Y2 = np.array(rna_d[P[2].split(',')[1]])

X3 = np.array(otu_d[P[3].split(',')[0]])
Y3 = np.array(rna_d[P[3].split(',')[1]])

X4 = np.array(otu_d[P[4].split(',')[0]])
Y4 = np.array(rna_d[P[4].split(',')[1]])

X5 = np.array(otu_d[P[5].split(',')[0]])
Y5 = np.array(rna_d[P[5].split(',')[1]])

X6 = np.array(otu_d[P[6].split(',')[0]])
Y6 = np.array(rna_d[P[6].split(',')[1]])

X7 = np.array(otu_d[P[7].split(',')[0]])
Y7 = np.array(rna_d[P[7].split(',')[1]])

X8 = np.array(otu_d[P[8].split(',')[0]])
Y8 = np.array(rna_d[P[8].split(',')[1]])

#plt.scatter(X,Y)
#plt.show()


# In[103]:

fig = plt.figure()
fig.suptitle('Top 9 regressions based on R2 ', fontsize=14, fontweight='bold')

ax = fig.add_subplot(331)
fig.subplots_adjust(top=0.85, hspace=0.8, wspace=0.8)
#ax.set_title('axes title')
ax.set_xlabel('437_AIM1L')
ax.set_ylabel('1100972')
plt.scatter(X0,Y0)

ax = fig.add_subplot(332)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('20448_NFURG04676010003')
ax.set_ylabel('241441')
plt.scatter(X1,Y1)

ax = fig.add_subplot(333)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('20448_NFURG04676010003')
ax.set_ylabel('4327501')
plt.scatter(X2,Y2)

ax = fig.add_subplot(334)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('6338_NFURG02469020200')
ax.set_ylabel('1115975')
plt.scatter(X3,Y3)

ax = fig.add_subplot(335)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('6338_NFURG02469020200')
ax.set_ylabel('68621')
plt.scatter(X4,Y4)

ax = fig.add_subplot(336)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('13405_ZNF521(2of3)')
ax.set_ylabel('286679')
plt.scatter(X5,Y5)

ax = fig.add_subplot(337)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('12209_CRIM1(1of2)')
ax.set_ylabel('720949')
plt.scatter(X6,Y6)

ax = fig.add_subplot(338)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('2248_PCDHAC2(4of8)')
ax.set_ylabel('3202924')
plt.scatter(X7,Y7)

ax = fig.add_subplot(339)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')
ax.set_xlabel('15993_ANPEP(6of6)')
ax.set_ylabel('OTU2311')
plt.scatter(X8,Y8)

fig.savefig('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/9-top_regr.pdf')

plt.show()


# In[ ]:




# In[ ]:



