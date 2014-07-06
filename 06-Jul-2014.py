
# coding: utf-8

# In[1]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/gQTL.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aaQTL.csv', 'rU').read()


# In[89]:

g1= [i for i in g.split('\n')[1:-1] if i.split(',')[15] != '']


# In[90]:

#g2 = [ i for i in g1 if sum(map(float, i.split(',')[15:])) < 4.0]


# Here I start considering only the QTL present on the rqtl linkage map

# In[91]:

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


# In[92]:

g3 = ','.join([ ','.join([ i+'\n' for i in j ]).replace('\n,','\n') for j in g2 ])


# In[93]:

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


# In[ ]:



