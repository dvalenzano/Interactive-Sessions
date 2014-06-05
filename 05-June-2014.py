
# coding: utf-8

# In[20]:

f14m = open('/Volumes/group_dv/personal/DValenzano/Jun2014/f14m_LG9.csv', 'rU').read()
f7m = open('/Volumes/group_dv/personal/DValenzano/Jun2014/f7m_LG9.csv', 'rU').read()
head = 'marker,chr,cM\n'


# In[29]:

f14m_2 = head+','.join([str(i.split()[1])+',9,'+str(i.split()[2]+'\n') for i in f14m.split('\n')[:-1]]).replace('\n,','\n')[:-1]
f7m_2 = head+','.join([str(i.split()[1])+',9,'+str(i.split()[2]+'\n') for i in f7m.split('\n')[:-1]]).replace('\n,','\n')[:-1]


# In[30]:

# m_f14m = [ i.split(',')[0] for i in f14m_2.split('\n')[1:]]
# m_f7m = [ i.split(',')[0] for i in f7m_2.split('\n')[1:]]


# In[31]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/f14m_LG9_f.csv', 'w')
z.write(f14m_2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/f7m_LG9_f.csv', 'w')
z.write(f7m_2)
z.close()

