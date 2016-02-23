
# coding: utf-8

# **TURNING THE LEfSe TABLE IN A BETTER LOOKING PLOT - GENERATING AN R INPUT FILE**

# In[3]:

l = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure2/LEfSe.txt', 'rU').read()
l = l.replace('\t',',')


# In[6]:

l1 = [ i  for i in l.split('\n')[:-1] if i.split(',')[2] != '']


# In[20]:

l1_old = [i for i in l1 if i.split(',')[2][0] == 'o']
l1_young = [i for i in l1 if i.split(',')[2][0] == 'y']


# In[21]:

l1_old_s = sorted(l1_old, key = lambda x: (x.split(',')[-2]))
l1_young_s = sorted(l1_young, key = lambda x: (x.split(',')[-2]))[::-1]


# In[30]:

l2 = 'GO,value1,group,LDA,p-value\n'+','.join([ i+'\n' for i in l1_young_s]).replace('\n,','\n')+','.join([ i+'\n' for i in l1_old_s]).replace('\n,','\n')


# In[31]:

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure2/lefse.csv', 'w')
z.write(l2)
z.close()


# Now the same, for figure 4

# In[70]:

l_4 = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/LEfSe.txt', 'rU').read()
l_4 = l_4.replace('\t',',')
l_4_1 = [ i  for i in l_4.split('\n')[:-1] if i.split(',')[2] != '']


# In[73]:

l_4_1_old = [i for i in l_4_1 if i.split(',')[2].split('_')[1][-1] == 'd']
l_4_1_young = [i for i in l_4_1 if i.split(',')[2].split('_')[1][-1] == 'g']
l411_old_s = sorted(l_4_1_old, key = lambda x: (x.split(',')[-2]))
l411_young_s = sorted(l_4_1_young, key = lambda x: (x.split(',')[-2]))[::-1]


# In[74]:

l42 = 'GO,value1,group,LDA,p-value\n'+','.join([ i+'\n' for i in l411_young_s]).replace('\n,','\n')+','.join([ i+'\n' for i in l411_old_s]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure4/lefse.csv', 'w')
z.write(l42)
z.close()


# In[ ]:



