
# Goal: to add the log-likelihood ratio test values to the LG3 QTL analysis

# In[28]:

g_ = open('/Volumes/group_dv/personal/DValenzano/Oct2014/gdays3_tab.csv', 'rU').read()
g_3 =  [g_.split('\n')[0]]+[i for i in g_.split('\n')[:-1] if i.split(',')[1]=='3.0']


# In[59]:

lgrank = open('/Volumes/group_dv/personal/DValenzano/Dec2014/surv-sig.csv', 'rU').read()
lgrank = lgrank.replace('NA', '1')


# In[101]:

import math
g_k = [i.split(',')[0] for i in g_3[1:]]
g_v = [i.split(',')[1:] for i in g_3[1:]]
g_d = dict(zip(g_k, g_v))

lrk = [i.split(',')[0] for i in lgrank.split('\n')[1:-1]]
#lrv = [i.split(',')[-1] for i in lgrank.split('\n')[1:-1]]
lrv = [str((-1)*math.log(float(i.split(',')[-1]))) for i in lgrank.split('\n')[1:-1]]
lrd = dict(zip(lrk, lrv))


# In[102]:

from sets import Set
mk = Set(g_k)&Set(lrk)


# In[110]:

final = ','.join([g_.split('\n')[0]+',log-rank\n']+[i+','+ ','.join(g_d[i])+','+ lrd[i] +'\n' for i in g_k ]).replace('\n,','\n').replace('-0.0','NA')


# In[111]:

gf = open('/Volumes/group_dv/personal/DValenzano/Dec2014/surv-sex-logrank.csv', 'w')
gf.write(final)
gf.close()


# In[ ]:



