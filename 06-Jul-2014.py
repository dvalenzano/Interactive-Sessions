
# coding: utf-8

# In[1]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/gQTL.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aaQTL.csv', 'rU').read()


# In[15]:

g1= [i for i in g.split('\n')[1:-1] if i.split(',')[15] != '']


# In[90]:

#g2 = [ i for i in g1 if sum(map(float, i.split(',')[15:])) < 4.0]


# Here I start considering only the QTL present on the rqtl linkage map

# In[16]:

import math
g2 = []
for i in range(len(g1)):
    if g1[i].split(',')[14] != '-':
        if -math.log10(float(g1[i].split(',')[15])) >= 0.09442141: #this is the value of the 99% quantile
            g2.append(g1[(i-10):(i+11)])
        elif -math.log10(float(g1[i].split(',')[16])) >= 0.1184394:
            g2.append(g1[(i-10):(i+11)])
        elif -math.log10(float(g1[i].split(',')[17])) >= 0.1534635:
            g2.append(g1[(i-10):(i+11)])
        elif -math.log10(float(g1[i].split(',')[18])) >= 0.09388327:
            g2.append(g1[(i-10):(i+11)])
        else:
            pass
    else:
        pass


# In[17]:

g3 = ','.join([ ','.join([ i+'\n' for i in j ]).replace('\n,','\n') for j in g2 ])


# In[23]:

from sets import Set
g4 =[i for i in list(Set(g3.split('\n')))[1:] if i.split(',')[14]!='-']


# In[99]:

g5 = sorted(g4[1:], key=lambda x: (x.split(',')[14].split('_')[0], float(x.split(',')[14].split('_')[1])))


# In[104]:

g6 = g.split('\n')[0]+'\n'+','.join([i+'\n' for i in g5 ]).replace('\n,','\n')


# In[105]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/g_rqtl_thr.csv', 'w')
z.write(g6)
z.close()


#### Now the same for cross AA

# In[6]:

import math
aa1= [i for i in aa.split('\n')[1:-1] if i.split(',')[8] != '']
aa2 = []
for i in range(len(aa1)):
    if aa1[i].split(',')[7] != '-':
        if -math.log10(float(aa1[i].split(',')[8])) >= 0.2541031: #this is the value of the 99% quantile
            aa2.append(aa1[(i-10):(i+11)])
        elif -math.log10(float(aa1[i].split(',')[9])) >= 0.2048027:
            aa2.append(aa1[(i-10):(i+11)])
        elif -math.log10(float(aa1[i].split(',')[10])) >= 0.217896:
            aa2.append(aa1[(i-10):(i+11)])
        elif -math.log10(float(aa1[i].split(',')[11])) >= 0.2591198:
            aa2.append(aa1[(i-10):(i+11)])
        else:
            pass
    else:
        pass


# In[7]:

aa3 = ','.join([ ','.join([ i+'\n' for i in j ]).replace('\n,','\n') for j in aa2 ])


# In[32]:

from sets import Set
aa4 =[i for i in list(Set(aa3.split('\n')))[1:] if i.split(',')[7] != '-']


# In[33]:

aa5 = sorted(aa4, key=lambda x: (x.split(',')[7].split('_')[0], float(x.split(',')[7].split('_')[1])))


# In[35]:

aa6 = aa.split('\n')[0]+'\n'+','.join([i+'\n' for i in aa5 ]).replace('\n,','\n')


# In[36]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aa_rqtl_thr.csv', 'w')
z.write(aa6)
z.close()

