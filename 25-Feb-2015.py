
# coding: utf-8

# Goal: to generate an R input file for the genotype-dependent median survival calculation for the 10000 bootstraps with equal numbers of males and females

# In[45]:

m0 = open('/Volumes/group_dv/personal/DValenzano/Feb2015/bootstrap-median_0.csv', 'rU').read()


# In[56]:

str(m0)


# In[57]:

rng = range(10000)
rng2 = [str(i) for i in rng]
rng3 = ['group=='+i for i in rng2]


# In[58]:

#cell10k = [m0]*10000


# In[59]:

prova = [ m0.replace('group==', i) for i in rng3]


# In[60]:

prova2 = ','.join([i+'\n' for i in prova ]).replace('\n,','\n')


# In[62]:

z = open('/Volumes/group_dv/personal/DValenzano/Feb2015/median-run-on-R.csv','w')
z.write(prova2)
z.close()


# In[34]:

qhat= m0.replace('group==', 'ciao')


# In[44]:

rng3[:15]


# In[ ]:



