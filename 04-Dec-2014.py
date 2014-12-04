# Updated version of 02-Dec-2014.py

g_ = open('/Volumes/group_dv/personal/DValenzano/Oct2014/gdays3_tab.csv', 'rU').read()
g_3 =  [g_.split('\n')[0]]+[i for i in g_.split('\n')[:-1] if i.split(',')[1]=='3.0']


# In[231]:

lgrank = open('/Volumes/group_dv/personal/DValenzano/Dec2014/surv-sig.csv', 'rU').read()
lgrank = lgrank.replace('NA', '1')


# In[101]:

import math
g_k = [i.split(',')[0] for i in g_3[1:]]
g_v = [i.split(',')[1:] for i in g_3[1:]]
g_d = dict(zip(g_k, g_v))

lrk = [i.split(',')[0] for i in lgrank.split('\n')[1:-1]]
#lrv = [i.split(',')[-1] for i in lgrank.split('\n')[1:-1]]
lrv = [str((-1)*math.log(float(i.split(',')[-1]))) for i in lgrank.split('\n')[1:-1]]
lrd = dict(zip(lrk, lrv))


# In[102]:

from sets import Set
mk = Set(g_k)&Set(lrk)


# In[110]:

final = ','.join([g_.split('\n')[0]+',log-rank\n']+[i+','+ ','.join(g_d[i])+','+ lrd[i] +'\n' for i in g_k ]).replace('\n,','\n').replace('-0.0','NA')


# In[111]:

gf = open('/Volumes/group_dv/personal/DValenzano/Dec2014/surv-sex-logrank.csv', 'w')
gf.write(final)
gf.close()


# In[169]:

### 04-Dec-2014 Goal: to redo the mapping of logrank p-values across LG3 both in all individuals and in females (het vs homozygous short-lived)


# In[160]:

tbr = 'a <- survdiff(Surv(time, status) ~ X, data=subset(g2, g2$X !=1)) \nb <- c(1-pchisq(a$chisq, length(a$n)-1), b);'
tbr2 = tbr*242


# In[162]:

g_lg3 = [tbr2.split(';')[i].replace('X','X'+str(g_k[i]))+'\n' for i in range(len(tbr2.split(';')[:-1]))]


# In[163]:

glg3fin = ','.join(g_lg3).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Dec2014/g_lg3_nohet.txt', 'w')
z.write(glg3fin)
z.close()


# In[174]:

xg_k = ','.join(['X'+i for i in g_k ])


# In[220]:

mpval = open('/Volumes/group_dv/personal/DValenzano/Dec2014/m_pval.csv', 'rU').read()


# In[221]:

#These contain -log of the new p-val
mpk = [i.split()[1].replace('"','').replace('X','') for i in mpval.split('\n')[1:-1]]
mpv = [str((-1)*math.log(float(i.split()[2].replace('"','')))) for i in mpval.split('\n')[1:-1]]
mpd = dict(zip(mpk, mpv))


# In[228]:

final2 = ','.join([g_.split('\n')[0]+',log-rank\n']+[i+','+ ','.join(g_d[i])+','+mpd[i] +'\n' for i in g_k ]).replace('\n,','\n')


# In[229]:

gf = open('/Volumes/group_dv/personal/DValenzano/Dec2014/surv-sex-logrank2.csv', 'w')
gf.write(final2)
gf.close()


# In[232]:

mfpval = open('/Volumes/group_dv/personal/DValenzano/Dec2014/mf_pval.csv', 'rU').read()


# In[233]:

mfpk = [i.split()[1].replace('"','').replace('X','') for i in mfpval.split('\n')[1:-1]]
mfpv = [str((-1)*math.log(float(i.split()[2].replace('"','')))) for i in mfpval.split('\n')[1:-1]]
mfpd = dict(zip(mfpk, mfpv))


# In[234]:

final3 = ','.join([g_.split('\n')[0]+',log-rank,log-rankf\n']+[i+','+ ','.join(g_d[i])+','+mpd[i] +','+mfpd[i]+'\n' for i in g_k ]).replace('\n,','\n')


# In[235]:

gf = open('/Volumes/group_dv/personal/DValenzano/Dec2014/surv-sex-logrank3.csv', 'w')
gf.write(final3)
gf.close()


# In[236]:

mmpval = open('/Volumes/group_dv/personal/DValenzano/Dec2014/mm_pval.csv', 'rU').read()
mmpk = [i.split()[1].replace('"','').replace('X','') for i in mmpval.split('\n')[1:-1]]
mmpv = [str((-1)*math.log(float(i.split()[2].replace('"','')))) for i in mmpval.split('\n')[1:-1]]
mmpd = dict(zip(mmpk, mmpv))
final4 = ','.join([g_.split('\n')[0]+',log-rank,log-rankf,log-rankm\n']+[i+','+ ','.join(g_d[i])+','+mpd[i] +','+mfpd[i]+','+mmpd[i]+'\n' for i in g_k ]).replace('\n,','\n')
gm = open('/Volumes/group_dv/personal/DValenzano/Dec2014/surv-sex-logrank4.csv', 'w')
gm.write(final4)
gm.close()


# In[ ]:



