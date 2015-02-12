Goal: to measure heterozygosity in GRZ


# In[1]:

c1 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped7.csv', 'rU').read()
c2 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped7.csv', 'rU').read()


# In[25]:

c1_aa = c1.split('\n')[1].split(',')[10:].count('aa')
c1_bb = c1.split('\n')[1].split(',')[10:].count('bb')
c1_ab = c1.split('\n')[1].split(',')[10:].count('ab')
c1_length = len(c1.split('\n')[1].split(',')[10:])


# In[26]:

from sets import Set
Set(c1.split('\n')[1].split(',')[10:])


# In[27]:

c1_length == c1_aa + c1_ab


# In[30]:

fc1_aa = float(c1_aa)/float(c1_length)
fc1_ab = float(c1_ab)/float(c1_length)


# In[31]:

fc1_ab


# the above value is the heterozygosity for females (GRZ) for cross 1
# Now we need to find the value for males (cross 2)

# In[34]:

c2_aa = c2.split('\n')[2].split(',')[10:].count('aa')
c2_bb = c2.split('\n')[2].split(',')[10:].count('bb')
c2_ab = c2.split('\n')[2].split(',')[10:].count('ab')
c2_length = len(c2.split('\n')[1].split(',')[10:])

from sets import Set
Set(c2.split('\n')[2].split(',')[10:])


# In[36]:

fc2_ab = float(c2_ab)/float(c2_length)
fc2_ab


# heterozygosity MZM-0703 from cross 1:

# In[37]:

c1_aa_ll = c1.split('\n')[2].split(',')[10:].count('aa')
c1_bb_ll = c1.split('\n')[2].split(',')[10:].count('bb')
c1_ab_ll = c1.split('\n')[2].split(',')[10:].count('ab')
c1_length = len(c1.split('\n')[1].split(',')[10:])

from sets import Set
Set(c1.split('\n')[2].split(',')[10:])


# In[38]:

fc1_ab_ll = float(c1_ab_ll)/float(c1_length)


# In[39]:

fc1_ab_ll


# In[43]:

c2_aa_ll = c2.split('\n')[1].split(',')[10:].count('aa')
c2_bb_ll = c2.split('\n')[1].split(',')[10:].count('bb')
c2_ab_ll = c2.split('\n')[1].split(',')[10:].count('ab')
c2_length = len(c2.split('\n')[1].split(',')[10:])

from sets import Set
Set(c2.split('\n')[1].split(',')[10:])


# In[44]:

fc2_ab_ll = float(c2_ab_ll)/float(c2_length)


# In[45]:

fc2_ab_ll




