
# coding: utf-8

# In[1]:

# Goal: To generate a plot where the median lifespan +/- the sd is plotted at each position for the AA, AB, BB genotypes. 
# Additionally, I will also plot the manhattan plot 
# This is an adapted version of 29-Sep-2014_2.py
g_days7m = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g7mdays_2.csv', 'rU').read()
g_days14m = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g14mdays_2.csv', 'rU').read()


# In[2]:

# I need to first transpose this matrix
g_days7mt = [list(i) for i in zip(* [ i.split(',') for i in g_days7m.split('\n')[:-1]])]
g_days14mt = [list(i) for i in zip(* [ i.split(',') for i in g_days14m.split('\n')[:-1]])]


# In[3]:

import numpy
import scipy
import math


# In[10]:

med_g7md_0 = [numpy.median([int(g_days7mt[2][5:][k])  for k in [i for i, j in enumerate(g_days7mt[n][5:]) if j == '0'] ])   for n in range(3,len(g_days7mt))]
std_g7md_0 = [numpy.std([int(g_days7mt[2][5:][k])  for k in [i for i, j in enumerate(g_days7mt[n][5:]) if j == '0'] ])   for n in range(3,len(g_days7mt))]
med_g7md_1 = [numpy.median([int(g_days7mt[2][5:][k])  for k in [i for i, j in enumerate(g_days7mt[n][5:]) if j == '1'] ])   for n in range(3,len(g_days7mt))]
std_g7md_1 = [numpy.std([int(g_days7mt[2][5:][k])  for k in [i for i, j in enumerate(g_days7mt[n][5:]) if j == '1'] ])   for n in range(3,len(g_days7mt))]
med_g7md_2 = [numpy.median([int(g_days7mt[2][5:][k])  for k in [i for i, j in enumerate(g_days7mt[n][5:]) if j == '2'] ])   for n in range(3,len(g_days7mt))]
std_g7md_2 = [numpy.std([int(g_days7mt[2][5:][k])  for k in [i for i, j in enumerate(g_days7mt[n][5:]) if j == '2'] ])   for n in range(3,len(g_days7mt))]


# In[11]:

med_g14md_0 = [numpy.median([int(g_days14mt[2][5:][k])  for k in [i for i, j in enumerate(g_days14mt[n][5:]) if j == '0'] ])   for n in range(3,len(g_days14mt))]
std_g14md_0 = [numpy.std([int(g_days14mt[2][5:][k])  for k in [i for i, j in enumerate(g_days14mt[n][5:]) if j == '0'] ])   for n in range(3,len(g_days14mt))]
med_g14md_1 = [numpy.median([int(g_days14mt[2][5:][k])  for k in [i for i, j in enumerate(g_days14mt[n][5:]) if j == '1'] ])   for n in range(3,len(g_days14mt))]
std_g14md_1 = [numpy.std([int(g_days14mt[2][5:][k])  for k in [i for i, j in enumerate(g_days14mt[n][5:]) if j == '1'] ])   for n in range(3,len(g_days14mt))]
med_g14md_2 = [numpy.median([int(g_days14mt[2][5:][k])  for k in [i for i, j in enumerate(g_days14mt[n][5:]) if j == '2'] ])   for n in range(3,len(g_days14mt))]
std_g14md_2 = [numpy.std([int(g_days14mt[2][5:][k])  for k in [i for i, j in enumerate(g_days14mt[n][5:]) if j == '2'] ])   for n in range(3,len(g_days14mt))]


# In[24]:

# I will now make a new file with marker name, median and std for each genotype
g7mzh = 'Marker, LG, cM, neg_log(pval), med0, std0, med1, std1, med2, std2\n'
g7mz0 = [i[0] + ','+ '7'+','+i[1]+','+str((-1)*math.log(float(i[2]))) for i in g_days7mt[3:]]
g7mzz = [g7mzh]+[ g7mz0[i]+','+str(med_g7md_0[i])+','+str(std_g7md_0[i])+','+str(med_g7md_1[i])+','+str(std_g7md_1[i])+','+str(med_g7md_2[i])+','+str(std_g7md_2[i])+'\n' for i in range(len(g7mz0))]  
g7mzzz = ','.join(g7mzz).replace('-0.0','0.0').replace('\n,','\n')


# In[25]:

# I will now make a new file with marker name, median and std for each genotype
g14mzh = 'Marker, LG, cM, neg_log(pval), med0, std0, med1, std1, med2, std2\n'
g14mz0 = [i[0] + ','+ '14'+','+i[1]+','+str((-1)*math.log(float(i[2]))) for i in g_days14mt[3:]]
g14mzz = [g14mzh]+[ g14mz0[i]+','+str(med_g14md_0[i])+','+str(std_g14md_0[i])+','+str(med_g14md_1[i])+','+str(std_g14md_1[i])+','+str(med_g14md_2[i])+','+str(std_g14md_2[i])+'\n' for i in range(len(g14mz0))]  
g14mzzz = ','.join(g14mzz).replace('-0.0','0.0').replace('\n,','\n')


# In[26]:

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g7mdays2_tab.csv', 'w')
z.write(g7mzzz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g14mdays2_tab.csv', 'w')
z.write(g14mzzz)
z.close()


# In[ ]:



