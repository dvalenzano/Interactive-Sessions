
# coding: utf-8

# In[3]:

lg1m = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1me_LGs.txt', 'rU').read()
lg1ms = lg1m.split('\n\n')[:-1]
alls1m = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg1ms[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg1ms)) ]
allj1m = ','.join(alls1m).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1me_LGs2.txt', 'w')
z.write(allj1m)
z.close()


# In[4]:

lg3m = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3me_LGs.txt', 'rU').read()
lg3ms = lg3m.split('\n\n')[:-1]
alls3m = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg3ms[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg3ms)) ]
allj3m = ','.join(alls3m).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3me_LGs2.txt', 'w')
z.write(allj3m)
z.close()


# In[5]:

lg1f = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1fe_LGs.txt', 'rU').read()
lg1fs = lg1f.split('\n\n')[:-1]
alls1f = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg1fs[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg1fs)) ]
allj1f = ','.join(alls1f).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1fe_LGs2.txt', 'w')
z.write(allj1f)
z.close()


# In[13]:

import numpy
qtlepi_1m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_1m.epi.qt', 'rU').read()
pvals_1m = [i.split()[-1] for i in qtlepi_1m.split('\n')[1:-1]]
pvalsf_1m = map(float, pvals_1m)
thr_1m = numpy.percentile(pvalsf_1m, 1)

qtlepi_3m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_3m.epi.qt', 'rU').read()
pvals_3m = [i.split()[-1] for i in qtlepi_3m.split('\n')[1:-1]]
pvalsf_3m = map(float, pvals_3m)
thr_3m = numpy.percentile(pvalsf_3m, 1)

qtlepi_1f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_1f.epi.qt', 'rU').read()
pvals_1f = [i.split()[-1] for i in qtlepi_1f.split('\n')[1:-1]]
pvalsf_1f = map(float, pvals_1f)
thr_1f = numpy.percentile(pvalsf_1f, 1)

qtlepi_1m_n =[ i  for i in qtlepi_1m.split('\n')[1:-1] if float(i.split()[-1])<(thr_1m)]
qtlepi_3m_n =[ i  for i in qtlepi_3m.split('\n')[1:-1] if float(i.split()[-1])<(thr_3m)]
qtlepi_1f_n =[ i  for i in qtlepi_1f.split('\n')[1:-1] if float(i.split()[-1])<(thr_1f)]


# In[14]:

keys_1m = [ i.split(',')[0] for i in allj1m.split('\n')[:-1]]
values_1m = [ i for i in allj1m.split('\n')[:-1]]
d_1m = dict(zip(keys_1m, values_1m))

keys_3m = [ i.split(',')[0] for i in allj3m.split('\n')[:-1]]
values_3m = [ i for i in allj3m.split('\n')[:-1]]
d_3m = dict(zip(keys_3m, values_3m))

keys_1f = [ i.split(',')[0] for i in allj1f.split('\n')[:-1]]
values_1f = [ i for i in allj1f.split('\n')[:-1]]
d_1f = dict(zip(keys_1f, values_1f))


# In[15]:

head='M#1,LG_M#1,cM_M#1,M#2,LG_M#2,cm_M#2,p-val\n'

ls_1m = []
for i in qtlepi_1m_n:
    if i.split()[1] in keys_1m and i.split()[3] in keys_1m:
        ls_1m.append(d_1m[i.split()[1]]+','+ d_1m[i.split()[3]] +','+ i.split()[-1]+'\n')
        
ls_3m = []
for i in qtlepi_3m_n:
    if i.split()[1] in keys_3m and i.split()[3] in keys_3m:
        ls_3m.append(d_3m[i.split()[1]]+','+ d_3m[i.split()[3]] +','+ i.split()[-1]+'\n')
        
ls_1f = []
for i in qtlepi_1f_n:
    if i.split()[1] in keys_1f and i.split()[3] in keys_1f:
        ls_1f.append(d_1f[i.split()[1]]+','+ d_1f[i.split()[3]] +','+ i.split()[-1]+'\n')


# In[13]:

fin_1m = head+','.join(ls_1m).replace('\n,','\n')[:-1]
fin_3m = head+','.join(ls_3m).replace('\n,','\n')[:-1]
fin_1f = head+','.join(ls_1f).replace('\n,','\n')[:-1]


# In[14]:

z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/epistasis_1m.csv', 'w')
z.write(fin_1m)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/epistasis_3m.csv', 'w')
z.write(fin_3m)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/epistasis_1f.csv', 'w')
z.write(fin_1f)
z.close()


# In[ ]:



