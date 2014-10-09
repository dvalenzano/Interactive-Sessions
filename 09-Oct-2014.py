
# coding: utf-8

# In[1]:

#Goal: to plot sex and s-QTL on the consensus LG3
rf_qvals = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/go_qval.tsv', 'rU').read()
lg3c = open('/Volumes/group_dv/personal/DValenzano/Oct2014/LG3merge/LG3c.csv', 'rU').read()


# In[7]:

rfk = [ i.split('\t')[0][1:] for i in rf_qvals.split('\n')[1:-1] ]
rf_sval = [ i.split('\t')[1] for i in rf_qvals.split('\n')[1:-1] ]
rf_dval = [ i.split('\t')[2] for i in rf_qvals.split('\n')[1:-1] ]
rf_mval = [ i.split('\t')[-3] for i in rf_qvals.split('\n')[1:-1] ]
rf_fval = [ i.split('\t')[-2] for i in rf_qvals.split('\n')[1:-1] ]
rf_resval = [ i.split('\t')[-1] for i in rf_qvals.split('\n')[1:-1] ]

rf_ds = dict(zip(rfk, rf_sval))
rf_dd = dict(zip(rfk, rf_dval))
rf_dm = dict(zip(rfk, rf_mval))
rf_df = dict(zip(rfk, rf_fval))
rf_dres = dict(zip(rfk, rf_resval))


# In[31]:

lg3c_rfs = []
for i in lg3c.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3c_rfs.append(i+','+rf_ds[i.split(',')[0]]+',sx\n')
    else:
        lg3c_rfs.append(i+',1,sx\n')


# In[32]:

lg3c_rfall = []
for i in lg3c.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3c_rfall.append(i+','+rf_dd[i.split(',')[0]]+',all\n')
    else:
        lg3c_rfall.append(i+',1,all\n')


# In[33]:

lg3c_rfm = []
for i in lg3c.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3c_rfm.append(i+','+rf_dm[i.split(',')[0]]+',m\n')
    else:
        lg3c_rfm.append(i+',1,m\n')


# In[34]:

lg3c_rff = []
for i in lg3c.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3c_rff.append(i+','+rf_df[i.split(',')[0]]+',f\n')
    else:
        lg3c_rff.append(i+',1,f\n')


# In[35]:

lg3c_rfRes = []
for i in lg3c.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3c_rfRes.append(i+','+rf_dres[i.split(',')[0]]+',Res\n')
    else:
        lg3c_rfRes.append(i+',1,Res\n')


# In[36]:

rinp_lg3c0 = ','.join(lg3c_rfs).replace('\n,','\n')+','.join(lg3c_rfall).replace('\n,','\n')+','.join(lg3c_rfm).replace('\n,','\n')+','.join(lg3c_rff).replace('\n,','\n')+','.join(lg3c_rfRes).replace('\n,','\n')


# In[37]:

import math
rinp_lg3c1 = [ ','.join(i.split(',')[:2])+','+str((-1)*math.log(float(i.split(',')[2])))+','+i.split(',')[-1]+'\n'  for i in rinp_lg3c0.split('\n')[:-1] ] 


# In[38]:

rinp_lg3c='Marker,cM,neg_logpq,group\n'+','.join(rinp_lg3c1).replace('\n,','\n')
rinp_lg3cr = rinp_lg3c.replace('-0.0', '0').replace(',0,',',0.0,')


# In[39]:

z =open('/Volumes/group_dv/personal/DValenzano/Oct2014/LG3merge/lg3c_rinput_sex-surv.csv', 'w')
z.write(rinp_lg3cr)
z.close()


# In[ ]:



