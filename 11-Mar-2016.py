
## GOAL: reformat fkpm and OTU tables for microbiome study - these generate R input files to compute multiple regression
# coding: utf-8

# In[3]:

get_ipython().system(u'/macqiime/anaconda/bin/normalize_table.py -i /Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/RNASeq_merged_otu_table.biom -a CSS -o /Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/RNASeq_merged_otu_tablen.biom')

get_ipython().system(u'biom convert -i /Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/RNASeq_merged_otu_tablen.biom -o /Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/RNASeq_merged_otu_tablen.txt --to-tsv')

t = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/RNASeq_merged_otu_tablen.txt', 'rU').read()

t = t.replace('\t',',')
z = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/RNASeq_merged_otu_tablen.csv', 'w')
z.write(t)
z.close()


# In[25]:

t = t.replace('Nex.Reference', '')
t2 = t.split('\n')[1:]
t3 = [ i.split(',') for i in t2 ]
tt = zip(*t3)
tT = [ list(i) for i in tt ]


# In[8]:

u = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_fpkm_genes.csv', 'rU').read()
u2 = u.split('\n')


# In[26]:

u3 = [ i.split(',') for i in u2]
ut = zip(*u3)
uT = [ list(i) for i in ut ]


# In[44]:

uTs = [uT[0]] + sorted(uT[1:], key = lambda x: (x[0]))
tTs = [tT[0]] + sorted(tT[1:], key = lambda x: (x[0]))


# In[45]:

[i[0] for i in uTs][1:] == [i[0] for i in tTs][1:] # this tests whether the two matrices have headers in same order


# In[68]:

uj = ','.join([','.join(i)+'\n' for i in uTs]).replace('\n,','\n')[:-1]
tj = ','.join([','.join(i)+'\n' for i in tTs]).replace('\n,','\n')[:-1]


# In[69]:

zu = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_fpkm_genes_sorted.csv', 'w')
zu.write(uj)
zu.close()

zt = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/data/rnaseq_merged_otu_table_sorted.csv', 'w')
zt.write(tj)
zt.close()


# In[ ]:



