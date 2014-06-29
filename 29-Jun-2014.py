
# coding: utf-8

# In[54]:

aag = open('/Volumes/group_dv/personal/DValenzano/Jun2014/alignGtoAA/AAo32014swi_mapped_to_Go32014.csv', 'rU').read()
gaa = open('/Volumes/group_dv/personal/DValenzano/Jun2014/alignGtoAA/Go32014_mapped_to_AAo32014swi.csv', 'rU').read()


# In[55]:

aag_aa = [i.split(',')[0].split('_')[-1] for i in aag.split('\n')[:-1]  if i.split(',')[1] != '*']
aag_g = [ i.split(',')[1].split('_')[-1] for i in aag.split('\n')[:-1] if i.split(',')[1] != '*' ]


# In[56]:

daag = dict(zip(aag_aa, aag_g))


# In[57]:

gaa_g = [i.split(',')[0].split('_')[-1] for i in gaa.split('\n')[:-1]  if i.split(',')[1] != '*']
gaa_aa = [ i.split(',')[1].split('_')[-1] for i in gaa.split('\n')[:-1] if i.split(',')[1] != '*' ]
dgaa = dict(zip(gaa_g, gaa_aa))


# In[58]:

gsqtl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_sqtl_chisqpval.csv','rU').read()
aasqtl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AA_sqtl_chisqpval.csv','rU').read()
gsqtl2 = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_sqtl_chisqpval_2.csv','rU').read()


# In[59]:

aasqtl.split('\n')[5]


# In[60]:

g_1 = [gsqtl.split('\n')[0]]+ [i for i in gsqtl.split('\n')[1:-1] if i.split(',')[-1] != 'nan' ]
g_2 = [gsqtl2.split('\n')[0]]+ [i for i in gsqtl2.split('\n')[1:-1] if i.split(',')[-1] != 'nan' ]
aa_1 = [aasqtl.split('\n')[0]]+ [i for i in aasqtl.split('\n')[1:-1] if i.split(',')[-1] != 'nan' ]


# In[61]:

g_1m = [ i.split(',')[0] for i in g_1 ]
g_2m = [ i.split(',')[0] for i in g_2 ]
aa_1m = [ i.split(',')[0] for i in aa_1 ]


# In[62]:

gsqtl_g = [ i for i in g_1 if i.split(',')[0] in gaa_g ]


# In[63]:

gsqtl_gaa = [ i for i in gsqtl_g if i.split(',')[0] in gaa_aa ]


# gsqtl_gaa is a list of markers that are significant in cross G, and which also map on cross AA

# In[64]:

aasqtl_aa = [ i for i in aa_1 if i.split(',')[0] in aag_aa ]
aasqtl_aag = [ i for i in aasqtl_aa if i.split(',')[0] in aag_g ]


# aasqtl_aag is a list of markers that are significant in cross AA, and which also map on cross G

#### Now I need to check if aasqtl_aag and gsqtl_gaa contain some of the same markers, i.e. if in cross G and AA there are overlapping markers

# In[65]:

from sets import Set

sG_aa = Set([dgaa[i] for i in [ j.split(',')[0] for j in gsqtl_gaa ]])
saa = Set([ j.split(',')[0] for j in aasqtl_aag ])
sG_aa & saa


# In[66]:

[aasqtl.split('\n')[0]]+[i for i in aasqtl_aag if i.split(',')[0] in list(sG_aa & saa)]


# In[70]:

[gsqtl.split('\n')[0]]+[i for i in gsqtl_gaa if i.split(',')[0] in [ daag[j]  for j in list(sG_aa & saa)]]


### <font color='red'> Conclusion 1: There is no overlap in significant markers (excluding the epistatic ones) between crosses G and AA. </font>

### Now I need to identify intervals in the various linkage maps

# In[ ]:



