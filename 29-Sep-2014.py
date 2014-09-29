
# coding: utf-8

# Goal: to generate a data file to analyze the direction of the survival QTL. By direction I mean whether
# an allele associated to longer lifespan is derived from the long-lived or from the short-lived P0
# This is a new version of 21-Sep-2014.py

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


# In[10]:

# Now I need to add the q-value from the random forest analysis
g_qvals=g_qvals.replace('X','')
aa_qvals=aa_qvals.replace('X','')


# In[11]:

# First, I need to choose the right p-vals for each group: F+M, M only and F only
g_qdays_mark = [i.split('\t')[0] for i in g_qvals.split('\n')[1:-1] ]
g_qdays_marv = [i.split('\t')[2] for i in g_qvals.split('\n')[1:-1] ]
g_qdays_d = dict(zip(g_qdays_mark,g_qdays_marv))

g_qdaysM_mark = [i.split('\t')[0] for i in g_qvals.split('\n')[1:-1] ]
g_qdaysM_marv = [i.split('\t')[-3] for i in g_qvals.split('\n')[1:-1] ]
g_qdaysM_d = dict(zip(g_qdaysM_mark,g_qdaysM_marv))

g_qdaysF_mark = [i.split('\t')[0] for i in g_qvals.split('\n')[1:-1] ]
g_qdaysF_marv = [i.split('\t')[-2] for i in g_qvals.split('\n')[1:-1] ]
g_qdaysF_d = dict(zip(g_qdaysF_mark,g_qdaysF_marv))


# In[12]:

# Now I need to add the qvals as third value to the lsg file
g1_days =[ i[:2] + [g_qdays_d[i[0]]] + i[2:] for i in g1 ]
g1_daysM =[ i[:2] + [g_qdaysM_d[i[0]]] + i[2:] for i in g1 ]
g1_daysF =[ i[:2] + [g_qdaysF_d[i[0]]] + i[2:] for i in g1 ]


# In[13]:

# I can now sort the markers by linkage group and position on the linkage group
g1_daysj = [','.join(i) for i in g1_days ]
g1_days_sorted = [ i.split(',') for i in sorted(g1_daysj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]

g1_daysMj = [','.join(i) for i in g1_daysM ]
g1_daysM_sorted = [ i.split(',') for i in sorted(g1_daysMj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]

g1_daysFj = [','.join(i) for i in g1_daysF ]
g1_daysF_sorted = [ i.split(',') for i in sorted(g1_daysFj, key=lambda x: (float(x.split(',')[1].split('_')[0]), float(x.split(',')[1].split('_')[1])))]


# In[14]:

# Now I need to add IDs, SEX, DAYS, retranspose this matrices
g2_days = [ list(i) for i in zip(*([['','']+j for j in g_gp1t[:3]]+g1_days_sorted)) ]
g2_daysM = [ list(i) for i in zip(*([['','']+j for j in g_gp1t[:3]]+g1_daysM_sorted)) ]
g2_daysF = [ list(i) for i in zip(*([['','']+j for j in g_gp1t[:3]]+g1_daysF_sorted)) ]


# In[19]:

# Now I need to remove the F1 individuals and remove females for the male file, and males from the female file
from sets import Set
gf1 = list(Set([i.split(',')[1] for i in goped7.split('\n')[1:-1] if i.split(',')[2] == 'G_M03']))

g3_days = [i for i in g2_days if i[0] not in gf1 ]
gz_days = ','.join([ ','.join(i)+'\n' for i in g3_days ]).replace('\n,','\n')

g3_daysM = [i for i in g2_daysM if i[0] not in gf1 ]
g3_daysM_1 = g2_daysM[:5] + [i for i in g2_daysM[5:] if i[1]=='1'] 
gz_daysM = ','.join([ ','.join(i)+'\n' for i in g3_daysM_1 ]).replace('\n,','\n')

g3_daysF = [i for i in g2_daysF if i[0] not in gf1 ]
g3_daysF_1 = g2_daysF[:5] + [i for i in g2_daysF[5:] if i[1]=='2'] 
gz_daysF = ','.join([ ','.join(i)+'\n' for i in g3_daysF_1 ]).replace('\n,','\n')


# In[20]:

# These matrices now have all I need: position on the linkage map, q-value, days and sex as phenotypes and marker name
# I can now use them to plot survival

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_days2.csv', 'w')
z.write(gz_days)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_daysM2.csv', 'w')
z.write(gz_daysM)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Sep2014/g_daysF2.csv', 'w')
z.write(gz_daysF)
z.close()


# In[211]:

float(1)


# In[ ]:



