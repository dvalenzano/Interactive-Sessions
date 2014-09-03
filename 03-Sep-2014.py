
# coding: utf-8

# Goal: to generate a new input file for LPmerge, which will allow to sort the markers on g7m, g14m and the random forest markers

# In[1]:

grf = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_g.csv', 'rU').read()


# In[29]:

import math
import numpy
grf_2 = ['M_ID,grf']+[ i.split(',')[0]+','+i.split(',')[1][:-2]+'_'+str(round(float(i.split(',')[2]), 2)) for i in grf.split('\n')[1:-1]]
grf_3 = ','.join([i+'\n' for i in grf_2 ]).replace('\n,','\n')


# In[30]:

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_rf.csv', 'w')
z.write(grf_3)
z.close()


# In[ ]:



