
# coding: utf-8

# Goal: to generate two input file to calculate explained variance in survival QTL marker 46347

# In[3]:

top=open('/Volumes/group_dv/personal/DValenzano/Feb2015/46347.csv', 'rU').read()
top = top.replace('\t',',')


# In[7]:

top2 = [i+'\n' for i in top.split('\n') if i.split(',')[-1] != '0']


# In[13]:

top3 = ','.join(top2).replace('\n,','\n')
top4 = top3.replace('aa', '0').replace('ab','1').replace('bb', '2')


# In[15]:

z = open('/Volumes/group_dv/personal/DValenzano/Feb2015/46347_2.csv', 'w')
z.write(top4)
z.close()


# In[16]:

top4.split('\n')[0]


# In[19]:

top5 = [i for i in top2 if i.split(',')[-1]!='ab\n']


# In[21]:

top6 = ','.join(top5).replace('\n,','\n')
top7 = top6.replace('aa', '0').replace('bb', '2')


# In[22]:

z = open('/Volumes/group_dv/personal/DValenzano/Feb2015/46347_3.csv', 'w')
z.write(top7)
z.close()


# In[ ]:



