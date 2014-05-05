
# coding: utf-8

# In[4]:

lg7m = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/LGs.txt', 'rU').read()
lg7ms = lg7m.split('\n\n')[:-1]


# In[42]:

alls7m = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg7ms[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg7ms)) ]
allj7m = ','.join(alls).replace('\n,','\n')[:-1]


# In[43]:

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/LGs2.txt', 'w')
z.write(allj7m)
z.close()


# In[44]:

lg14m = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/LGs.txt', 'rU').read()
lg14ms = lg14m.split('\n\n')[:-1]
alls14m = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg14ms[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg14ms)) ]
allj14m = ','.join(alls14m).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/LGs2.txt', 'w')
z.write(allj14m)
z.close()


# In[ ]:



