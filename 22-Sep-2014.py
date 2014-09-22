
# coding: utf-8

# In[46]:

# Goal: To generate a plot where the median lifespan +/- the sd is plotted at each position for the AA, AB, BB genotypes. 
# Additionally, I will also plot the manhattan plot 
g_days = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_days.csv', 'rU').read()
g_daysM = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_daysM.csv', 'rU').read()
g_daysF = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_daysF.csv', 'rU').read()


# In[47]:

# I need to first transpose this matrix
g_dayst = [list(i) for i in zip(* [ i.split(',') for i in g_days.split('\n')[:-1]])]
g_daysMt = [list(i) for i in zip(* [ i.split(',') for i in g_daysM.split('\n')[:-1]])]
g_daysFt = [list(i) for i in zip(* [ i.split(',') for i in g_daysF.split('\n')[:-1]])]


# In[45]:

import numpy
import scipy
import math


# In[42]:

# Now I will calculate median and standard deviation for each marker, for each different file
med_gd_0 = [numpy.median([int(g_dayst[2][5:][k])  for k in [i for i, j in enumerate(g_dayst[n][5:]) if j == '0'] ])   for n in range(3,len(g_dayst))]
std_gd_0 = [numpy.std([int(g_dayst[2][5:][k])  for k in [i for i, j in enumerate(g_dayst[n][5:]) if j == '0'] ])   for n in range(3,len(g_dayst))]


# In[43]:

med_gd_1 = [numpy.median([int(g_dayst[2][5:][k])  for k in [i for i, j in enumerate(g_dayst[n][5:]) if j == '1'] ])   for n in range(3,len(g_dayst))]
std_gd_1 = [numpy.std([int(g_dayst[2][5:][k])  for k in [i for i, j in enumerate(g_dayst[n][5:]) if j == '1'] ])   for n in range(3,len(g_dayst))]


# In[44]:

med_gd_2 = [numpy.median([int(g_dayst[2][5:][k])  for k in [i for i, j in enumerate(g_dayst[n][5:]) if j == '2'] ])   for n in range(3,len(g_dayst))]
std_gd_2 = [numpy.std([int(g_dayst[2][5:][k])  for k in [i for i, j in enumerate(g_dayst[n][5:]) if j == '2'] ])   for n in range(3,len(g_dayst))]


# In[88]:

med_gMd_0 = [numpy.median([int(g_daysMt[2][5:][k])  for k in [i for i, j in enumerate(g_daysMt[n][5:]) if j == '0'] ])   for n in range(3,len(g_daysMt))]
std_gMd_0 = [numpy.std([int(g_daysMt[2][5:][k])  for k in [i for i, j in enumerate(g_daysMt[n][5:]) if j == '0'] ])   for n in range(3,len(g_daysMt))]
med_gMd_1 = [numpy.median([int(g_daysMt[2][5:][k])  for k in [i for i, j in enumerate(g_daysMt[n][5:]) if j == '1'] ])   for n in range(3,len(g_daysMt))]
std_gMd_1 = [numpy.std([int(g_daysMt[2][5:][k])  for k in [i for i, j in enumerate(g_daysMt[n][5:]) if j == '1'] ])   for n in range(3,len(g_daysMt))]
med_gMd_2 = [numpy.median([int(g_daysMt[2][5:][k])  for k in [i for i, j in enumerate(g_daysMt[n][5:]) if j == '2'] ])   for n in range(3,len(g_daysMt))]
std_gMd_2 = [numpy.std([int(g_daysMt[2][5:][k])  for k in [i for i, j in enumerate(g_daysMt[n][5:]) if j == '2'] ])   for n in range(3,len(g_daysMt))]


# In[89]:

med_gFd_0 = [numpy.median([int(g_daysFt[2][5:][k])  for k in [i for i, j in enumerate(g_daysFt[n][5:]) if j == '0'] ])   for n in range(3,len(g_daysFt))]
std_gFd_0 = [numpy.std([int(g_daysFt[2][5:][k])  for k in [i for i, j in enumerate(g_daysFt[n][5:]) if j == '0'] ])   for n in range(3,len(g_daysFt))]
med_gFd_1 = [numpy.median([int(g_daysFt[2][5:][k])  for k in [i for i, j in enumerate(g_daysFt[n][5:]) if j == '1'] ])   for n in range(3,len(g_daysFt))]
std_gFd_1 = [numpy.std([int(g_daysFt[2][5:][k])  for k in [i for i, j in enumerate(g_daysFt[n][5:]) if j == '1'] ])   for n in range(3,len(g_daysFt))]
med_gFd_2 = [numpy.median([int(g_daysFt[2][5:][k])  for k in [i for i, j in enumerate(g_daysFt[n][5:]) if j == '2'] ])   for n in range(3,len(g_daysFt))]
std_gFd_2 = [numpy.std([int(g_daysFt[2][5:][k])  for k in [i for i, j in enumerate(g_daysFt[n][5:]) if j == '2'] ])   for n in range(3,len(g_daysFt))]


# In[94]:

# I will now make a new file with marker name, median and std for each genotype
gzh = 'Marker, LG, cM, neg_log(qval), med0, std0, med1, std1, med2, std2\n'
gz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in g_dayst[3:]]
gzz = [gzh]+[ gz0[i]+','+str(med_gd_0[i])+','+str(std_gd_0[i])+','+str(med_gd_1[i])+','+str(std_gd_1[i])+','+str(med_gd_2[i])+','+str(std_gd_2[i])+'\n' for i in range(len(gz0))]  
gzzz = ','.join(gzz).replace('-0.0','0.0').replace('\n,','\n')


# In[95]:

# I will now make a new file with marker name, median and std for each genotype
gMzh = 'Marker, LG, cM, -log(qval), med0, std0, med1, std1, med2, std2\n'
gMz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in g_daysMt[3:]]
gMzz = [gMzh]+[ gMz0[i]+','+str(med_gMd_0[i])+','+str(std_gMd_0[i])+','+str(med_gMd_1[i])+','+str(std_gMd_1[i])+','+str(med_gMd_2[i])+','+str(std_gMd_2[i])+'\n' for i in range(len(gMz0))]  
gMzzz = ','.join(gMzz).replace('-0.0','0.0').replace('\n,','\n')


# In[96]:

# I will now make a new file with marker name, median and std for each genotype
gFzh = 'Marker, LG, cM, -log(qval), med0, std0, med1, std1, med2, std2\n'
gFz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in g_daysFt[3:]]
gFzz = [gFzh]+[ gFz0[i]+','+str(med_gFd_0[i])+','+str(std_gFd_0[i])+','+str(med_gFd_1[i])+','+str(std_gFd_1[i])+','+str(med_gFd_2[i])+','+str(std_gFd_2[i])+'\n' for i in range(len(gFz0))]  
gFzzz = ','.join(gFzz).replace('-0.0','0.0').replace('\n,','\n')


# In[97]:

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/gdays_tab.csv', 'w')
z.write(gzzz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/gdaysM_tab.csv', 'w')
z.write(gMzzz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/gdaysF_tab.csv', 'w')
z.write(gFzzz)
z.close()


# In[ ]:



