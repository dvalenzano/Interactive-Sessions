
# coding: utf-8

#### I will generate a random set of 50 markers that are homozygous - i.e. mappable on the Rqtl linkage map - to add to the   markers that are significant for survival to be able to map them on the other LM

# In[30]:

f7 = open('/Users/dvalenzano/Dropbox/tmp/inf-fam_7.csv', 'rU').read()
f7t = zip(*[ i.split(',') for i in f7.split('\n')[:-1]])
f7s = ','.join([','.join( list(i)+['\n']).replace('\n,','\n') for i in f7t ]).replace('\n,','\n')
hom7 = [i.split(',')[0] for i in f7s.split('\n')[10:] if ','.join(i.split(',')[1:3]) == 'aa,bb']


# In[31]:

f14 = open('/Users/dvalenzano/Dropbox/tmp/inf-fam_14.csv', 'rU').read()
f14t = zip(*[ i.split(',') for i in f14.split('\n')[:-1]])
f14s = ','.join([','.join( list(i)+['\n']).replace('\n,','\n') for i in f14t ]).replace('\n,','\n')
hom14 = [i.split(',')[0] for i in f14s.split('\n')[10:] if ','.join(i.split(',')[1:3]) == 'aa,bb']


# In[32]:

f8 = open('/Users/dvalenzano/Dropbox/tmp/inf-fam_8.csv', 'rU').read()
f8t = zip(*[ i.split(',') for i in f8.split('\n')[:-1]])
f8s = ','.join([','.join( list(i)+['\n']).replace('\n,','\n') for i in f8t ]).replace('\n,','\n')
hom8 = [i.split(',')[0] for i in f8s.split('\n')[10:] if ','.join(i.split(',')[1:3]) == 'aa,bb']


# In[33]:

from sets import Set
s7 = Set(hom7)
s14 = Set(hom14)
s8 = Set(hom8)


# In[45]:

len((s7&s8)&s14)


# In[47]:

print 'length Set(7): ' + str(len(s7))+'\nlength Set(14): ' + str(len(s14))+'\nlength Set(8): '+str(len(s8))


# In[48]:

homshared = list((s7&s8)&s14)


# In[52]:

import random
rhom = ','.join(random.sample(homshared, 50))


# In[53]:

z = open('/Users/dvalenzano/Dropbox/tmp/rhom', 'w')
z.write(rhom)
z.close()


# In[ ]:



