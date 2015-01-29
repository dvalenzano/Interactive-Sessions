
# This is ongoing

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


# In[19]:

Here we derive the markers 

gq =
aaq = 


# In[ ]:



