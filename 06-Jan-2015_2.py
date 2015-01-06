
# GOAL: to plot independently logrank and random forest in cross AA in LG3.

aa_ = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aadays3_tab.csv', 'rU').read()


# In[2]:

aa_3 =  [aa_.split('\n')[0]]+[i for i in aa_.split('\n')[:-1] if i.split(',')[1]=='3.0']


# In[4]:

import math
aa_k = [i.split(',')[0] for i in aa_3[1:]]
aa_v = [i.split(',')[1:] for i in aa_3[1:]]
aa_d = dict(zip(aa_k, aa_v))


# In[6]:

len(aa_k)


# In[24]:

line = 'a <- survdiff(Surv(time, status) ~ X_mrk, data=subset(aa3, aa3$X_mrk !=1))\nb <- c(1-pchisq(a$chisq, length(a$n)-1), b)\n__'
mline = line*186
mline = mline.split('__')


# In[25]:

prova = [mline[i].replace('_mrk', aa_k[i]) for i in range(186)]


# In[32]:

provaj = ','.join(prova).replace('\n,','\n')


# In[33]:

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aalrt_rinput.csv', 'w')
z.write(provaj)
z.close()


# In[36]:

# Goal: now I need to generate a file with marker, LG, position and p-value
# SNP and p-value come from /Volumes/group_dv/personal/DValenzano/Jan2015/aa_m_pval.csv
# SNP and position come from /Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv or from aa_3


# In[45]:

pvaltab = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aa_m_pval.csv', 'rU').read()
pvaltab = pvaltab.replace('"', '')


# In[47]:

kpv = [i.split()[1] for i in pvaltab.split('\n')[1:-1]]
vpv = [i.split()[2] for i in pvaltab.split('\n')[1:-1]]
dpv = dict(zip(kpv, vpv))


# In[65]:

aafin = 'SNP,LG,pos,pval\n'+','.join([','.join([i]+aa_d[i][:2]+[dpv[i]])+'\n' for i in aa_k]).replace('\n,','\n')


# In[66]:

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aa_surv-sig.csv', 'w')
z.write(aafin)
z.close()


# In[70]:

lrk = [i.split(',')[0] for i in aafin.split('\n')[1:-1]]
#lrv = [i.split(',')[-1] for i in lgrank.split('\n')[1:-1]]
lrv = [str((-1)*math.log(float(i.split(',')[-1]))) for i in aafin.split('\n')[1:-1]]
lrd = dict(zip(lrk, lrv))


# In[71]:

from sets import Set
mk = Set(aa_k)&Set(lrk)


# In[72]:

final = ','.join([aa_.split('\n')[0]+',log-rank\n']+[i+','+ ','.join(aa_d[i])+','+ lrd[i] +'\n' for i in aa_k ]).replace('\n,','\n').replace('-0.0','NA')


# In[73]:

aaf = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aa_surv-sex-logrank.csv', 'w')
aaf.write(final)
aaf.close()


# In[76]:

mpval = pvaltab
mpk = [i.split()[1].replace('"','').replace('X','') for i in mpval.split('\n')[1:-1]]
mpv = [str((-1)*math.log(float(i.split()[2].replace('"','')))) for i in mpval.split('\n')[1:-1]]
mpd = dict(zip(mpk, mpv))


# In[77]:

final2 = ','.join([aa_.split('\n')[0]+',log-rank\n']+[i+','+ ','.join(aa_d[i])+','+mpd[i] +'\n' for i in aa_k ]).replace('\n,','\n')


# In[229]:

aaf2 = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aa_surv-sex-logrank2.csv', 'w')
aaf2.write(final2)
aaf2.close()



