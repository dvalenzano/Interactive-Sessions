
# coding: utf-8

#### Goal: to identify qtl that are shared between the random forest method and plink's method

# In[2]:

rf_aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/aao_qval.tsv', 'rU').read()
rf_g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/go_qval.tsv', 'rU').read()


# In[3]:

aa_qtl = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aarqtl.csv', 'rU').read()
g_qtl = open('/Volumes/group_dv/personal/DValenzano/Jul2014/grqtl.csv', 'rU').read()


# In[7]:

rf_aas = [  i.split('\t') for i in rf_aa.split('\n')[:-1]]
rf_gs = [  i.split('\t') for i in rf_g.split('\n')[:-1]]


# In[55]:

aaqk = [i.split(',')[0] for i in aa_qtl.split('\n')[1:-1] ]
aaqv = [i for i in aa_qtl.split('\n')[1:-1] ]
aaqd = dict(zip(aaqk, aaqv))

gqk = [i.split(',')[0] for i in g_qtl.split('\n')[1:-1] ]
gqv = [i for i in g_qtl.split('\n')[1:-1] ]
gqd = dict(zip(gqk, gqv))

aarfk = [i.split('\t')[0][1:] for i in rf_aa.split('\n')[1:-1] ]
aarfv = [','+','.join([i.split('\t')[2]]+i.split('\t')[9:]) for i in rf_aa.split('\n')[1:-1] ]
aarfd = dict(zip(aarfk, aarfv))

grfk = [i.split('\t')[0][1:] for i in rf_g.split('\n')[1:-1] ]
grfv = [','+','.join([i.split('\t')[2]]+i.split('\t')[10:]) for i in rf_g.split('\n')[1:-1] ]
grfd = dict(zip(grfk, grfv))


# In[56]:

aa_hat = ','+','.join([rf_aa.split('\n')[0].split('\t')[2]]+rf_aa.split('\n')[0].split('\t')[9:]) 
g_hat = ','+','.join([rf_g.split('\n')[0].split('\t')[2]]+rf_g.split('\n')[0].split('\t')[10:]) 


# In[62]:

aaQTL = [aaqd[i] + aarfd[i] if i in aarfk else aaqd[i]+',,,,'for i in aaqk ]
gQTL = [gqd[i] + grfd[i] if i in grfk else gqd[i]+',,,,'for i in gqk ]


# In[67]:

aaQTLj = aa_qtl.split('\n')[0]+aa_hat+'\n'+','.join([ i+'\n' for i in aaQTL ]).replace('\n,','\n')
gQTLj = g_qtl.split('\n')[0]+g_hat+'\n'+','.join([ i+'\n' for i in gQTL ]).replace('\n,','\n')


# In[68]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aaQTL.csv', 'w')
z.write(aaQTLj)
z.close()
z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/gQTL.csv', 'w')
z.write(gQTLj)
z.close()


# In[125]:

aa1 = aaQTLj.replace(',,,,',',1,1,1,1')

prova = [i for i in aa1.split('\n')[1:-1] if min(i.split(',')[-4:]) < '0.4']


# In[132]:

aarfqtl = [i for i in rf_aa.split('\n')[1:-1] if min([i.split('\t')[2]]+i.split('\t')[9:]) < '0.1' ]

grfqtl = [i for i in rf_g.split('\n')[1:-1] if min([i.split('\t')[2]]+i.split('\t')[9:]) < '0.1' ]


# In[133]:

grfqtl


# In[ ]:



