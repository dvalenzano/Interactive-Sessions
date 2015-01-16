# Goal: to generate a table with Marker, position (LG and cM) and qvalues (based on the random forest analysis) for survival in cross AAo


# In[2]:

aa = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/aao_qval.tsv' ,'rU').read()
aa = aa.replace('X', '')
aak = [ i.split()[0] for i in aa.split('\n')[1:-1]]
aav = [ i.split()[1:3]+i.split()[-3:] for i in aa.split('\n')[1:-1]]
aad = dict(zip(aak, aav))


# In[6]:

aamap = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read()


# In[10]:

aamap = aamap.replace('"', '')
aamk = [ i.split(',')[0] for i in aamap.split('\n')[1:-1]]
aamv = [ i.split(',')[1:] for i in aamap.split('\n')[1:-1]]
aamd = dict(zip(aamk, aamv))


# In[22]:

from sets import Set
aa2 = Set(aak) & Set(aamk)
aaj = [[i]+aamd[i] + aad[i] for i in aa2]


# In[24]:

aaj2 = [','.join(i) for i in aaj ]


# In[30]:

aajs = sorted(aaj2, key=lambda x:(float(x.split(',')[1]), float(x.split(',')[2])))


# In[34]:

aajs2 = 'Marker,LG,cM,sex,sQTL_all,sQTL_males,sQTL_females,sQTL_sexregr\n'+ ','.join([i+'\n' for i in aajs ] ).replace('\n,','\n')


# In[37]:

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/AAo_qvals.csv', 'w')
z.write(aajs2)
z.close()


# In[45]:

# Same file as above, just surv for all
aajs3 = 'Marker,LG,cM,sQTL_all\n'+','.join([','.join(i)+'\n' for i in [i.split(',')[:3]+[i.split(',')[-4]] for i in aajs ] ]).replace('\n,','\n')


# In[48]:

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/AAo_qvals_survall.csv', 'w')
z.write(aajs3)
z.close()


# In[ ]:



