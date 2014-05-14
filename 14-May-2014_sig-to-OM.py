
# coding: utf-8

# In[15]:

AAolm = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read()


# In[16]:

markers = [ i.split(',')[0].replace('"','') for i in AAolm.split('\n')[1:-1]]


# In[21]:

import random
rm = random.sample(markers,50)
','.join(rm)


# In[ ]:

gender = raw_input('What gender are you interested in processing [fem, mal]?\n')
gender_init = gender[0]
family = raw_input('What family are you interested in processing?\n')
omin = '/Volumes/group_dv/personal/DValenzano/May2014/AAo/%s/fam_%s%s_OneMap.txt' %(gender, family, gender_init)
om = open(omin, 'rU').read()
assig = '/Volumes/group_dv/personal/DValenzano/May2014/AAo/%s/fam_%s%s_sqtl_sig' %(gender, family, gender_init)
sig = open(assig, 'rU').read()
s = ','.join([ i.split()[1]+','+i.split()[-1]+'\n'  for i in sig.split('\n')[:-1] ]).replace('\n,','\n')
sigmark = [ i.split(',')[0] for i in s.split('\n')[1:-1]]
om_sig0 = ','.join([ i+'\n'  for i in om.split('\n')[:-1] if i.split('\t')[0][1:] in sigmark ]).replace('\n,','\n')
#om_sig1 = str(len(om_sig0.split('\n')[0].split('\t')[2].split(',')))+' '+str(len(om_sig0.split('\n')[:-1])+50)+'\n'+om_sig0
rmj = '11308,5250,27689,12362,8364,2169,19335,13760,27195,17433,32322,29970,24252,15437,46541,42030,32851,8490,8579,35457,31403,22521,29102,16189,42343,42545,18150,14071,19227,30500,11124,15541,26725,13152,11673,40457,43783,22973,9868,12843,24013,15650,37697,37721,6997,29134,33650,21001,5391,10279'
#here add the random choice of markers
#om_sig2 = ','.join([ i+'\n'  for i in om.split('\n')[:-1] if i.split('\t')[0][1:] in rm and i.split('\t')[0][1:] not in sigmark]).replace('\n,','\n')
om_sig1 = ','.join([ i+'\n'  for i in om.split('\n')[:-1] if i.split('\t')[0][1:] in rmj and i.split('\t')[0][1:] not in sigmark]).replace('\n,','\n')
#om_sig3 = om_sig1 + om_sig2
om_sig2 = om_sig0 + om_sig1
om_sig3 = str(len(om_sig0.split('\n')[0].split('\t')[2].split(',')))+' '+str(len(om_sig2.split('\n')[:-1]))+'\n'+om_sig2

out = '/Volumes/group_dv/personal/DValenzano/May2014/AAo/%s/fam_%s%s_omsig_new.txt' %(gender, family, gender_init)
z = open(out, 'w')
z.write(om_sig3)
z.close()

