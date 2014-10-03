# Goal: To analyze the sex-residuals on G cross, based on the random-forest analysis
# coding: utf-8

# In[1]:

# all the q-val from the rf analysis:
g_qvals= open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/go_qval.tsv', 'rU').read()
aa_qvals= open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/aao_qval.tsv', 'rU').read()


# In[2]:

# the genotypes and phenotypes used in the final rf analysis (including those that do not map on rqtl):
g_gp= open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/goGP_rf_filt.csv', 'rU').read()
aa_gp= open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/aaoGP_rf_filt.csv', 'rU').read()


# In[3]:

# files with the rqtl positions for each marker:
g_rqtlpos= open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_g.csv', 'rU').read()
aa_rqtlpos= open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_aa.csv', 'rU').read()


# In[4]:

# orignal genotyping files to select F2 only:
goped7 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped7.csv', 'rU').read()
aaoped7 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped7.csv', 'rU').read()


# In[5]:

# First, I will add position on LM for each marker
g_gp1 = g_gp.replace(';',',').replace(',X',',')
aa_gp1 = aa_gp.replace(';',',').replace(',X',',')


# In[6]:

g_mark = [i.split(',')[0] for i in g_rqtlpos.split('\n')[1:-2] ]
g_marv = [i.split(',')[1]+'_'+i.split(',')[2] for i in g_rqtlpos.split('\n')[1:-2] ]
g_d = dict(zip(g_mark,g_marv))


# In[7]:

# I need to transpose the reference data matrix
g_gp1t = [list(i) for i in zip(*[i.split(',') for i in g_gp1.split('\n') ])]


# In[8]:

lsg = []
for i in g_gp1t[3:]:
    if i[0] in g_mark:
        lsg.append(i)


# In[9]:

g1 = [[i[0]] + [g_d[i[0]]] + i[1:] for i in lsg ] #g1 has marker name, position on rqtl and genotypes for each marker


# In[11]:

# Now I need to add the q-value from the random forest analysis
g_qvals=g_qvals.replace('X','')
aa_qvals=aa_qvals.replace('X','')


# In[17]:

# First, I need to choose the right p-vals for the Sex-Res group
g_qdaysRes_mark = [i.split('\t')[0] for i in g_qvals.split('\n')[1:-1] ]
g_qdaysRes_marv = [i.split('\t')[-1] for i in g_qvals.split('\n')[1:-1] ]
g_qdaysRes_d = dict(zip(g_qdaysRes_mark,g_qdaysRes_marv))


# In[18]:

# Now I need to add the qvals as third value to the lsg file
g1_daysRes =[ i[:2] + [g_qdaysRes_d[i[0]]] + i[2:] for i in g1 ]


# In[19]:

# I can now sort the markers by linkage group and position on the linkage group
g1_daysResj = [','.join(i) for i in g1_daysRes ]
g1_daysRes_sorted = [ i.split(',') for i in sorted(g1_daysResj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]


# In[20]:

# Now I need to add IDs, SEX, DAYS, retranspose this matrices
g2_daysRes = [ list(i) for i in zip(*([['','']+j for j in g_gp1t[:3]]+g1_daysRes_sorted)) ]


# In[21]:

# Now I need to remove the F1 individuals and remove females for the male file, and males from the female file
from sets import Set

gf1 = list(Set([i.split(',')[1] for i in goped7.split('\n')[1:-1] if i.split(',')[2] == 'G_M03']))
g3_daysRes = [i for i in g2_daysRes if i[0] not in gf1 ]
gz_daysRes = ','.join([ ','.join(i)+'\n' for i in g3_daysRes ]).replace('\n,','\n')


# In[22]:

# This matrices now has all I need: position on the linkage map, q-value, days and sex as phenotypes and marker name
# I can now use them to plot survival

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g_daysRes2.csv', 'w')
z.write(gz_daysRes)
z.close()


# In[23]:

g_daysRes = gz_daysRes
# I need to first transpose this matrix
g_daysRest = [list(i) for i in zip(* [ i.split(',') for i in g_daysRes.split('\n')[:-1]])]
import numpy
import scipy
import math
med_gResd_0 = [numpy.median([int(g_daysRest[2][5:][k])  for k in [i for i, j in enumerate(g_daysRest[n][5:]) if j == '0'] ])   for n in range(3,len(g_daysRest))]
std_gResd_0 = [numpy.std([int(g_daysRest[2][5:][k])  for k in [i for i, j in enumerate(g_daysRest[n][5:]) if j == '0'] ])   for n in range(3,len(g_daysRest))]
med_gResd_1 = [numpy.median([int(g_daysRest[2][5:][k])  for k in [i for i, j in enumerate(g_daysRest[n][5:]) if j == '1'] ])   for n in range(3,len(g_daysRest))]
std_gResd_1 = [numpy.std([int(g_daysRest[2][5:][k])  for k in [i for i, j in enumerate(g_daysRest[n][5:]) if j == '1'] ])   for n in range(3,len(g_daysRest))]
med_gResd_2 = [numpy.median([int(g_daysRest[2][5:][k])  for k in [i for i, j in enumerate(g_daysRest[n][5:]) if j == '2'] ])   for n in range(3,len(g_daysRest))]
std_gResd_2 = [numpy.std([int(g_daysRest[2][5:][k])  for k in [i for i, j in enumerate(g_daysRest[n][5:]) if j == '2'] ])   for n in range(3,len(g_daysRest))]


# In[25]:

# I will now make a new file with marker name, median and std for each genotype
gzh = 'Marker, LG, cM, neg_log(qval), med0, std0, med1, std1, med2, std2\n'
gz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in g_daysRest[3:]]
gzz = [gzh]+[ gz0[i]+','+str(med_gResd_0[i])+','+str(std_gResd_0[i])+','+str(med_gResd_1[i])+','+str(std_gResd_1[i])+','+str(med_gResd_2[i])+','+str(std_gResd_2[i])+'\n' for i in range(len(gz0))]  
gzzz = ','.join(gzz).replace('-0.0','0.0').replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/gdaysRes2_tab.csv', 'w')
z.write(gzzz)
z.close()


# In[ ]:



