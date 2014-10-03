
# coding: utf-8

# Goal: to generate a data file to analyze the direction of the survival QTL in AA cross. By direction I mean whether
# an allele associated to longer lifespan is derived from the long-lived or from the short-lived P0

# In[1]:

# all the q-val from the rf analysis:
aa_qvals= open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/aao_qval.tsv', 'rU').read()
# the genotypes and phenotypes used in the final rf analysis (including those that do not map on rqtl):
aa_gp= open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/aaoGP_rf_filt.csv', 'rU').read()
# files with the rqtl positions for each marker:
aa_rqtlpos= open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_aa.csv', 'rU').read()
# orignal genotyping files to select F2 only:
aaoped7 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped7.csv', 'rU').read()
# First, I will add position on LM for each marker
aa_gp1 = aa_gp.replace(';',',').replace(',X',',')
aa_mark = [i.split(',')[0] for i in aa_rqtlpos.split('\n')[1:-2] ]
aa_marv = [i.split(',')[1]+'_'+i.split(',')[2] for i in aa_rqtlpos.split('\n')[1:-2] ]
aa_d = dict(zip(aa_mark,aa_marv))


# In[2]:

# I need to transpose the reference data matrix
aa_gp1t = [list(i) for i in zip(*[i.split(',') for i in aa_gp1.split('\n') ])]
lsaa = []
for i in aa_gp1t[3:]:
    if i[0] in aa_mark:
        lsaa.append(i)
aa1 = [[i[0]] + [aa_d[i[0]]] + i[1:] for i in lsaa ] #g1 has marker name, position on rqtl and genotypes for each marker
# Now I need to add the q-value from the random forest analysis
aa_qvals=aa_qvals.replace('X','')


# In[3]:

# First, I need to choose the right p-vals for each group: F+M, M only and F only
aa_qdays_mark = [i.split('\t')[0] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdays_marv = [i.split('\t')[2] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdays_d = dict(zip(aa_qdays_mark,aa_qdays_marv))

aa_qdaysM_mark = [i.split('\t')[0] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdaysM_marv = [i.split('\t')[-3] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdaysM_d = dict(zip(aa_qdaysM_mark,aa_qdaysM_marv))

aa_qdaysF_mark = [i.split('\t')[0] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdaysF_marv = [i.split('\t')[-2] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdaysF_d = dict(zip(aa_qdaysF_mark,aa_qdaysF_marv))

aa_qdaysRes_mark = [i.split('\t')[0] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdaysRes_marv = [i.split('\t')[-1] for i in aa_qvals.split('\n')[1:-1] ]
aa_qdaysRes_d = dict(zip(aa_qdaysRes_mark,aa_qdaysRes_marv))


# In[4]:

# Now I need to add the qvals as third value to the lsaa file
aa1_days =[ i[:2] + [aa_qdays_d[i[0]]] + i[2:] for i in aa1 ]
aa1_daysM =[ i[:2] + [aa_qdaysM_d[i[0]]] + i[2:] for i in aa1 ]
aa1_daysF =[ i[:2] + [aa_qdaysF_d[i[0]]] + i[2:] for i in aa1 ]
aa1_daysRes =[ i[:2] + [aa_qdaysRes_d[i[0]]] + i[2:] for i in aa1 ]


# In[5]:

# I can now sort the markers by linkage group and position on the linkage group
aa1_daysj = [','.join(i) for i in aa1_days ]
aa1_days_sorted = [ i.split(',') for i in sorted(aa1_daysj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]

aa1_daysMj = [','.join(i) for i in aa1_daysM ]
aa1_daysM_sorted = [ i.split(',') for i in sorted(aa1_daysMj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]

aa1_daysFj = [','.join(i) for i in aa1_daysF ]
aa1_daysF_sorted = [ i.split(',') for i in sorted(aa1_daysFj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]

aa1_daysResj = [','.join(i) for i in aa1_daysRes ]
aa1_daysRes_sorted = [ i.split(',') for i in sorted(aa1_daysResj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]


# In[6]:

# Now I need to add IDs, SEX, DAYS, retranspose this matrices
aa2_days = [ list(i) for i in zip(*([['','']+j for j in aa_gp1t[:3]]+aa1_days_sorted)) ]
aa2_daysM = [ list(i) for i in zip(*([['','']+j for j in aa_gp1t[:3]]+aa1_daysM_sorted)) ]
aa2_daysF = [ list(i) for i in zip(*([['','']+j for j in aa_gp1t[:3]]+aa1_daysF_sorted)) ]
aa2_daysRes = [ list(i) for i in zip(*([['','']+j for j in aa_gp1t[:3]]+aa1_daysRes_sorted)) ]


# In[9]:

# Now I need to remove the F1 individuals and remove females for the male file, and males from the female file
from sets import Set
aaf1 = list(Set([i.split(',')[1] for i in aaoped7.split('\n')[1:-1] if i.split(',')[2] == 'aa_M01']))

aa3_days = [i for i in aa2_days if i[0] not in aaf1 ]
aaz_days = ','.join([ ','.join(i)+'\n' for i in aa3_days ]).replace('\n,','\n')

aa3_daysM = [i for i in aa2_daysM if i[0] not in aaf1 ]
aa3_daysM_1 = aa2_daysM[:5] + [i for i in aa2_daysM[5:] if i[1]=='1'] 
aaz_daysM = ','.join([ ','.join(i)+'\n' for i in aa3_daysM_1 ]).replace('\n,','\n')

aa3_daysF = [i for i in aa2_daysF if i[0] not in aaf1 ]
aa3_daysF_1 = aa2_daysF[:5] + [i for i in aa2_daysF[5:] if i[1]=='2'] 
aaz_daysF = ','.join([ ','.join(i)+'\n' for i in aa3_daysF_1 ]).replace('\n,','\n')

aa3_daysRes = [i for i in aa2_daysRes if i[0] not in aaf1 ]
aaz_daysRes = ','.join([ ','.join(i)+'\n' for i in aa3_daysRes ]).replace('\n,','\n')


# In[10]:

# These matrices now have all I need: position on the linkage map, q-value, days and sex as phenotypes and marker name
# I can now use them to plot survival

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_days2.csv', 'w')
z.write(aaz_days)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_daysM2.csv', 'w')
z.write(aaz_daysM)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_daysF2.csv', 'w')
z.write(aaz_daysF)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_daysRes2.csv', 'w')
z.write(aaz_daysRes)
z.close()


# In[11]:

aa_days = aaz_days
aa_daysM = aaz_daysM
aa_daysF = aaz_daysF
aa_daysRes = aaz_daysRes
# I need to first transpose these matrices
aa_dayst = [list(i) for i in zip(* [ i.split(',') for i in aa_days.split('\n')[:-1]])]
aa_daysMt = [list(i) for i in zip(* [ i.split(',') for i in aa_daysM.split('\n')[:-1]])]
aa_daysFt = [list(i) for i in zip(* [ i.split(',') for i in aa_daysF.split('\n')[:-1]])]
aa_daysRest = [list(i) for i in zip(* [ i.split(',') for i in aa_daysRes.split('\n')[:-1]])]
import numpy
import scipy
import math


# In[14]:

# Now I will calculate median and standard deviation for each marker, for each different file
med_aad_0 = [numpy.median([int(aa_dayst[2][5:][k])  for k in [i for i, j in enumerate(aa_dayst[n][5:]) if j == '0'] ])   for n in range(3,len(aa_dayst))]
std_aad_0 = [numpy.std([int(aa_dayst[2][5:][k])  for k in [i for i, j in enumerate(aa_dayst[n][5:]) if j == '0'] ])   for n in range(3,len(aa_dayst))]
med_aad_1 = [numpy.median([int(aa_dayst[2][5:][k])  for k in [i for i, j in enumerate(aa_dayst[n][5:]) if j == '1'] ])   for n in range(3,len(aa_dayst))]
std_aad_1 = [numpy.std([int(aa_dayst[2][5:][k])  for k in [i for i, j in enumerate(aa_dayst[n][5:]) if j == '1'] ])   for n in range(3,len(aa_dayst))]
med_aad_2 = [numpy.median([int(aa_dayst[2][5:][k])  for k in [i for i, j in enumerate(aa_dayst[n][5:]) if j == '2'] ])   for n in range(3,len(aa_dayst))]
std_aad_2 = [numpy.std([int(aa_dayst[2][5:][k])  for k in [i for i, j in enumerate(aa_dayst[n][5:]) if j == '2'] ])   for n in range(3,len(aa_dayst))]

med_aaMd_0 = [numpy.median([int(aa_daysMt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysMt[n][5:]) if j == '0'] ])   for n in range(3,len(aa_daysMt))]
std_aaMd_0 = [numpy.std([int(aa_daysMt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysMt[n][5:]) if j == '0'] ])   for n in range(3,len(aa_daysMt))]
med_aaMd_1 = [numpy.median([int(aa_daysMt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysMt[n][5:]) if j == '1'] ])   for n in range(3,len(aa_daysMt))]
std_aaMd_1 = [numpy.std([int(aa_daysMt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysMt[n][5:]) if j == '1'] ])   for n in range(3,len(aa_daysMt))]
med_aaMd_2 = [numpy.median([int(aa_daysMt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysMt[n][5:]) if j == '2'] ])   for n in range(3,len(aa_daysMt))]
std_aaMd_2 = [numpy.std([int(aa_daysMt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysMt[n][5:]) if j == '2'] ])   for n in range(3,len(aa_daysMt))]


# In[15]:

med_aaFd_0 = [numpy.median([int(aa_daysFt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysFt[n][5:]) if j == '0'] ])   for n in range(3,len(aa_daysFt))]
std_aaFd_0 = [numpy.std([int(aa_daysFt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysFt[n][5:]) if j == '0'] ])   for n in range(3,len(aa_daysFt))]
med_aaFd_1 = [numpy.median([int(aa_daysFt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysFt[n][5:]) if j == '1'] ])   for n in range(3,len(aa_daysFt))]
std_aaFd_1 = [numpy.std([int(aa_daysFt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysFt[n][5:]) if j == '1'] ])   for n in range(3,len(aa_daysFt))]
med_aaFd_2 = [numpy.median([int(aa_daysFt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysFt[n][5:]) if j == '2'] ])   for n in range(3,len(aa_daysFt))]
std_aaFd_2 = [numpy.std([int(aa_daysFt[2][5:][k])  for k in [i for i, j in enumerate(aa_daysFt[n][5:]) if j == '2'] ])   for n in range(3,len(aa_daysFt))]

med_aaResd_0 = [numpy.median([int(aa_daysRest[2][5:][k])  for k in [i for i, j in enumerate(aa_daysRest[n][5:]) if j == '0'] ])   for n in range(3,len(aa_daysRest))]
std_aaResd_0 = [numpy.std([int(aa_daysRest[2][5:][k])  for k in [i for i, j in enumerate(aa_daysRest[n][5:]) if j == '0'] ])   for n in range(3,len(aa_daysRest))]
med_aaResd_1 = [numpy.median([int(aa_daysRest[2][5:][k])  for k in [i for i, j in enumerate(aa_daysRest[n][5:]) if j == '1'] ])   for n in range(3,len(aa_daysRest))]
std_aaResd_1 = [numpy.std([int(aa_daysRest[2][5:][k])  for k in [i for i, j in enumerate(aa_daysRest[n][5:]) if j == '1'] ])   for n in range(3,len(aa_daysRest))]
med_aaResd_2 = [numpy.median([int(aa_daysRest[2][5:][k])  for k in [i for i, j in enumerate(aa_daysRest[n][5:]) if j == '2'] ])   for n in range(3,len(aa_daysRest))]
std_aaResd_2 = [numpy.std([int(aa_daysRest[2][5:][k])  for k in [i for i, j in enumerate(aa_daysRest[n][5:]) if j == '2'] ])   for n in range(3,len(aa_daysRest))]


# In[17]:

# I will now make a new file with marker name, median and std for each genotype
aazh = 'Marker, LG, cM, neg_log(qval), med0, std0, med1, std1, med2, std2\n'
aaz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in aa_dayst[3:]]
aazz = [aazh]+[ aaz0[i]+','+str(med_aad_0[i])+','+str(std_aad_0[i])+','+str(med_aad_1[i])+','+str(std_aad_1[i])+','+str(med_aad_2[i])+','+str(std_aad_2[i])+'\n' for i in range(len(aaz0))]  
aazzz = ','.join(aazz).replace('-0.0','0.0').replace('\n,','\n')

aaMzh = 'Marker, LG, cM, neg_log(qval), med0, std0, med1, std1, med2, std2\n'
aaMz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in aa_daysMt[3:]]
aaMzz = [aaMzh]+[ aaMz0[i]+','+str(med_aaMd_0[i])+','+str(std_aaMd_0[i])+','+str(med_aaMd_1[i])+','+str(std_aaMd_1[i])+','+str(med_aaMd_2[i])+','+str(std_aaMd_2[i])+'\n' for i in range(len(aaMz0))]  
aaMzzz = ','.join(aaMzz).replace('-0.0','0.0').replace('\n,','\n')

aaFzh = 'Marker, LG, cM, neg_log(qval), med0, std0, med1, std1, med2, std2\n'
aaFz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in aa_daysFt[3:]]
aaFzz = [aaFzh]+[ aaFz0[i]+','+str(med_aaFd_0[i])+','+str(std_aaFd_0[i])+','+str(med_aaFd_1[i])+','+str(std_aaFd_1[i])+','+str(med_aaFd_2[i])+','+str(std_aaFd_2[i])+'\n' for i in range(len(aaFz0))]  
aaFzzz = ','.join(aaFzz).replace('-0.0','0.0').replace('\n,','\n')

aaReszh = 'Marker, LG, cM, neg_log(qval), med0, std0, med1, std1, med2, std2\n'
aaResz0 = [i[0] + ','+ i[1].split('_')[0]+','+i[1].split('_')[1]+','+str((-1)*math.log(float(i[2]))) for i in aa_daysRest[3:]]
aaReszz = [aaReszh]+[ aaResz0[i]+','+str(med_aaResd_0[i])+','+str(std_aaResd_0[i])+','+str(med_aaResd_1[i])+','+str(std_aaResd_1[i])+','+str(med_aaResd_2[i])+','+str(std_aaResd_2[i])+'\n' for i in range(len(aaResz0))]  
aaReszzz = ','.join(aaReszz).replace('-0.0','0.0').replace('\n,','\n')


# In[18]:

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/aadays2_tab.csv', 'w')
z.write(aazzz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/aadaysM2_tab.csv', 'w')
z.write(aaMzzz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/aadaysF2_tab.csv', 'w')
z.write(aaFzzz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aadaysRes2_tab.csv', 'w')
z.write(aaReszzz)
z.close()


# In[ ]:



