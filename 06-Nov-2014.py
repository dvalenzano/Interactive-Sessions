
# coding: utf-8

# In[17]:

#Goal: to plot sex and s-QTL on the LG3 in cross AA
rf_qvals = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/aao_qval.tsv', 'rU').read()
lg3 = open('/Volumes/group_dv/personal/DValenzano/Nov2014/AA-cross/LG3.csv', 'rU').read()


# In[18]:

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


# In[19]:

lg3_rfs = []
for i in lg3.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3_rfs.append(i+','+rf_ds[i.split(',')[0]]+',sx\n')
    else:
        lg3_rfs.append(i+',1,sx\n')

lg3_rfall = []
for i in lg3.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3_rfall.append(i+','+rf_dd[i.split(',')[0]]+',all\n')
    else:
        lg3_rfall.append(i+',1,all\n')

lg3_rfm = []
for i in lg3.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3_rfm.append(i+','+rf_dm[i.split(',')[0]]+',m\n')
    else:
        lg3_rfm.append(i+',1,m\n')

lg3_rff = []
for i in lg3.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3_rff.append(i+','+rf_df[i.split(',')[0]]+',f\n')
    else:
        lg3_rff.append(i+',1,f\n')

lg3_rfRes = []
for i in lg3.split('\n')[1:-1]:
    if i.split(',')[0] in rfk:
        lg3_rfRes.append(i+','+rf_dres[i.split(',')[0]]+',Res\n')
    else:
        lg3_rfRes.append(i+',1,Res\n')


# In[20]:

rinp_lg30 = ','.join(lg3_rfs).replace('\n,','\n')+','.join(lg3_rfall).replace('\n,','\n')+','.join(lg3_rfm).replace('\n,','\n')+','.join(lg3_rff).replace('\n,','\n')+','.join(lg3_rfRes).replace('\n,','\n')


# In[21]:

import math
rinp_lg31 = [ ','.join(i.split(',')[:2])+','+str((-1)*math.log(float(i.split(',')[2])))+','+i.split(',')[-1]+'\n'  for i in rinp_lg30.split('\n')[:-1] ] 


# In[22]:

rinp_lg3='Marker,cM,neg_logpq,group\n'+','.join(rinp_lg31).replace('\n,','\n')
rinp_lg3r = rinp_lg3.replace('-0.0', '0').replace(',0,',',0.0,')

z =open('/Volumes/group_dv/personal/DValenzano/Nov2014/AA-cross/lg3_rinput_sex-surv.csv', 'w')
z.write(rinp_lg3r)
z.close()

