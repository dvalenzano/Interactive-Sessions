
# coding: utf-8

# In[1]:

gsurv = open('/Volumes/group_dv/personal/DValenzano/Aug2014/G_cross_surv.txt', 'rU').read()
aasurv = open('/Volumes/group_dv/personal/DValenzano/Aug2014/AA_cross_surv.txt', 'rU').read()


# In[15]:

SL = [float(i.split('\t')[0].replace(',','.')) for i in gsurv.split('\n') if i.split('\t')[-1]=='1'] + [float(i.split('\t')[0].replace(',','.')) for i in aasurv.split('\n')[1:-2] if i.split('\t')[-2]=='1']


# In[18]:

import math
import numpy as np
np.percentile(SL, 90)


# 21 weeks is the max lifespan for the Short-lived fish in both cross AA and G

# In[22]:

float((21.0*7.0)/365.0) #translated in years


# In[23]:

#Here follows the measure of max-lifespan for the long-lived strains independently in both crosses


# In[29]:

gsurv.split('\n')[-2]


# In[30]:

GLL = [float(i.split('\t')[0].replace(',','.')) for i in gsurv.split('\n')[:-1] if i.split('\t')[-2]=='1']
AALL = [float(i.split('\t')[0].replace(',','.')) for i in aasurv.split('\n')[:-2] if i.split('\t')[-1]=='1']


# In[40]:

print (
'max-lifespan for MZM-0703 strain is: ' + str(np.percentile(GLL, 90) )+' weeks or ' + str(float(7.0*np.percentile(GLL, 90)/365))+' years'
'\nmax-lifespan for Soveia strain is: ' + str(np.percentile(AALL, 90) )+' weeks or ' + str(float(7.0*np.percentile(AALL, 90)/365))+' years'
)


# In[ ]:



