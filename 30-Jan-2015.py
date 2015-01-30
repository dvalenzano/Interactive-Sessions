
# Goal: to reduce the number of markers for the qvalue calculation in cross 1 and cross 2 to those that are mapped on the linkage map only


# coding: utf-8

# In[9]:

g_pq2 = open('/Volumes/group_dv/personal/DValenzano/Jan2015/go_pq2.csv', 'rU').read()
aa_pq2 = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aao_pq2.csv', 'rU').read()


# In[16]:

# These are markers with respective LG and position

gv = [i.split()[1:4] for i in g_pq2.split('\n')[1:-1]]
aav = [i.split()[1:4] for i in aa_pq2.split('\n')[1:-1]]

gk = [i[0] for i in gv]
aak = [i[0] for i in aav]

gd = dict(zip(gk, gv))
aad = dict(zip(aak, aav))


# In[18]:

# These are all the genotypes, with indexes and no LG or position information

gp = open('/Volumes/group_dv/personal/DValenzano/Dec2014/go-pval.csv', 'rU').read()
aap = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aao-pval.csv', 'rU').read()


# In[20]:

# Here we derive the markers corresponding to the indexes

gq = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/go_qval.tsv', 'rU').read()
aaq = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/aao_qval.tsv', 'rU').read()


# In[23]:

gqm = [i.split('\t')[0][1:]  for i in gq.split('\n')[1:-1] ]
aaqm = [i.split('\t')[0][1:]  for i in aaq.split('\n')[1:-1] ]


# In[31]:

# Now I need to add the markers names to the genotypes 
gp2 = [ [gqm[i]]+gp.split('\n')[1:-1][i].split()[1:] for i in range(len(gp.split('\n')[1:-1]))]
aap2 = [ [aaqm[i]]+aap.split('\n')[1:-1][i].split()[1:] for i in range(len(aap.split('\n')[1:-1]))]


# In[39]:

gp3 = [i for i in gp2 if i[0] in gk ]
aap3 = [i for i in aap2 if i[0] in aak ]


# In[40]:

g_head = 'marker,'+','.join(gq.split('\n')[0].split())+'\n'
aa_head = 'marker,'+','.join(aaq.split('\n')[0].split())+'\n'

gp4 = g_head + ','.join([','.join(i)+'\n' for i in gp3]).replace('\n,','\n')
aap4 = aa_head + ','.join([','.join(i)+'\n' for i in aap3]).replace('\n,','\n')


# In[41]:

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/cross1_pvals.csv', 'w')
z.write(gp4)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/cross2_pvals.csv', 'w')
z.write(aap4)
z.close()


# In[ ]:



