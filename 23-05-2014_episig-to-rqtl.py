
# coding: utf-8

# In[22]:

Go_m7e = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/epistasis_7m.csv', 'rU').read()
Go_m14e = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/epistasis_14m.csv', 'rU').read()
Go_m8e = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8m/epistasis_8m.csv', 'rU').read()

Go_f7e = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7f/epistasis_7f.csv', 'rU').read()
Go_f14e = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14f/epistasis_14f.csv', 'rU').read()
Go_f8e = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8f/epistasis_8f.csv', 'rU').read()

AAo_m1e = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/epistasis_1m.csv', 'rU').read()
AAo_m3e = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/epistasis_3m.csv', 'rU').read()
AAo_f1e = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/epistasis_1f.csv', 'rU').read()

Go_rqtl = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read().replace('"','')
AAo_rqtl = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read().replace('"','')


# In[86]:

head2 = 'M#1,LG_M#1,cM_M#1,LG_M#1rqtl,cM_M#1rqtl,M#2,LG_M#2,cm_M#2,LG_M#2rqtl,cM_M#2rqtl,p-val\n'


# In[31]:

keys_Go = [ i.split(',')[0]   for i in Go_rqtl.split('\n')[:-1]]
values_Go = [ ','.join(i.split(',')[1:])   for i in Go_rqtl.split('\n')[:-1]]
dGo = dict(zip(keys_Go, values_Go))

keys_AAo = [ i.split(',')[0]   for i in AAo_rqtl.split('\n')[:-1]]
values_AAo = [ ','.join(i.split(',')[1:])   for i in AAo_rqtl.split('\n')[:-1]]
dAAo = dict(zip(keys_AAo, values_AAo))


# In[104]:

Go_m7e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in Go_m7e.split('\n')]).replace('\n,','\n')
Go_m7e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in Go_m7e.split('\n')]).replace('\n,','\n')

Go_m14e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in Go_m14e.split('\n')]).replace('\n,','\n')
Go_m14e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in Go_m14e.split('\n')]).replace('\n,','\n')

Go_m8e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in Go_m8e.split('\n')]).replace('\n,','\n')
Go_m8e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in Go_m8e.split('\n')]).replace('\n,','\n')

Go_f7e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in Go_f7e.split('\n')]).replace('\n,','\n')
Go_f7e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in Go_f7e.split('\n')]).replace('\n,','\n')

Go_f14e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in Go_f14e.split('\n')]).replace('\n,','\n')
Go_f14e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in Go_f14e.split('\n')]).replace('\n,','\n')

Go_f8e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in Go_f8e.split('\n')]).replace('\n,','\n')
Go_f8e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in Go_f8e.split('\n')]).replace('\n,','\n')

AAo_m1e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in AAo_m1e.split('\n')]).replace('\n,','\n')
AAo_m1e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in AAo_m1e.split('\n')]).replace('\n,','\n')

AAo_m3e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in AAo_m3e.split('\n')]).replace('\n,','\n')
AAo_m3e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in AAo_m3e.split('\n')]).replace('\n,','\n')

AAo_f1e_0 = ','.join([','.join(i.split(',')[:3])+'\n'  for i in AAo_f1e.split('\n')]).replace('\n,','\n')
AAo_f1e_1 = ','.join([','.join(i.split(',')[3:])+'\n'  for i in AAo_f1e.split('\n')]).replace('\n,','\n')


# In[115]:

ls_Go_m7e_0 = []
for i in Go_m7e.split('\n')[1:]:
    if i.split(',')[0] in keys_Go:
        ls_Go_m7e_0.append(i.split(',')[:3]+dGo[i.split(',')[0]].split(','))
    else:
        ls_Go_m7e_0.append(i.split(',')[:3]+['-','-'])

ls_Go_m7e_1 = []
for i in Go_m7e.split('\n')[1:]:
    if i.split(',')[3] in keys_Go:
        ls_Go_m7e_1.append(i.split(',')[3:-1]+dGo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_Go_m7e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_Go_m7e = ','.join([head2]+[','.join(ls_Go_m7e_0[i] + ls_Go_m7e_1[i])+'\n'   for i in range(len(ls_Go_m7e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m7e.csv', 'w')
z.write(ls_Go_m7e)
z.close()


# In[116]:

ls_Go_m14e_0 = []
for i in Go_m14e.split('\n')[1:]:
    if i.split(',')[0] in keys_Go:
        ls_Go_m14e_0.append(i.split(',')[:3]+dGo[i.split(',')[0]].split(','))
    else:
        ls_Go_m14e_0.append(i.split(',')[:3]+['-','-'])

ls_Go_m14e_1 = []
for i in Go_m14e.split('\n')[1:]:
    if i.split(',')[3] in keys_Go:
        ls_Go_m14e_1.append(i.split(',')[3:-1]+dGo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_Go_m14e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_Go_m14e = ','.join([head2]+[','.join(ls_Go_m14e_0[i] + ls_Go_m14e_1[i])+'\n'   for i in range(len(ls_Go_m14e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m14e.csv', 'w')
z.write(ls_Go_m14e)
z.close()


# In[117]:

ls_Go_m8e_0 = []
for i in Go_m8e.split('\n')[1:]:
    if i.split(',')[0] in keys_Go:
        ls_Go_m8e_0.append(i.split(',')[:3]+dGo[i.split(',')[0]].split(','))
    else:
        ls_Go_m8e_0.append(i.split(',')[:3]+['-','-'])

ls_Go_m8e_1 = []
for i in Go_m8e.split('\n')[1:]:
    if i.split(',')[3] in keys_Go:
        ls_Go_m8e_1.append(i.split(',')[3:-1]+dGo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_Go_m8e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_Go_m8e = ','.join([head2]+[','.join(ls_Go_m8e_0[i] + ls_Go_m8e_1[i])+'\n'   for i in range(len(ls_Go_m8e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m8e.csv', 'w')
z.write(ls_Go_m8e)
z.close()


# In[118]:

ls_Go_f7e_0 = []
for i in Go_f7e.split('\n')[1:]:
    if i.split(',')[0] in keys_Go:
        ls_Go_f7e_0.append(i.split(',')[:3]+dGo[i.split(',')[0]].split(','))
    else:
        ls_Go_f7e_0.append(i.split(',')[:3]+['-','-'])

ls_Go_f7e_1 = []
for i in Go_f7e.split('\n')[1:]:
    if i.split(',')[3] in keys_Go:
        ls_Go_f7e_1.append(i.split(',')[3:-1]+dGo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_Go_f7e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_Go_f7e = ','.join([head2]+[','.join(ls_Go_f7e_0[i] + ls_Go_f7e_1[i])+'\n'   for i in range(len(ls_Go_f7e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f7e.csv', 'w')
z.write(ls_Go_f7e)
z.close()


# In[119]:

ls_Go_f14e_0 = []
for i in Go_f14e.split('\n')[1:]:
    if i.split(',')[0] in keys_Go:
        ls_Go_f14e_0.append(i.split(',')[:3]+dGo[i.split(',')[0]].split(','))
    else:
        ls_Go_f14e_0.append(i.split(',')[:3]+['-','-'])

ls_Go_f14e_1 = []
for i in Go_f14e.split('\n')[1:]:
    if i.split(',')[3] in keys_Go:
        ls_Go_f14e_1.append(i.split(',')[3:-1]+dGo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_Go_f14e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_Go_f14e = ','.join([head2]+[','.join(ls_Go_f14e_0[i] + ls_Go_f14e_1[i])+'\n'   for i in range(len(ls_Go_f14e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f14e.csv', 'w')
z.write(ls_Go_f14e)
z.close()


# In[120]:

ls_Go_f8e_0 = []
for i in Go_f8e.split('\n')[1:]:
    if i.split(',')[0] in keys_Go:
        ls_Go_f8e_0.append(i.split(',')[:3]+dGo[i.split(',')[0]].split(','))
    else:
        ls_Go_f8e_0.append(i.split(',')[:3]+['-','-'])

ls_Go_f8e_1 = []
for i in Go_f8e.split('\n')[1:]:
    if i.split(',')[3] in keys_Go:
        ls_Go_f8e_1.append(i.split(',')[3:-1]+dGo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_Go_f8e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_Go_f8e = ','.join([head2]+[','.join(ls_Go_f8e_0[i] + ls_Go_f8e_1[i])+'\n'   for i in range(len(ls_Go_f8e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f8e.csv', 'w')
z.write(ls_Go_f8e)
z.close()


# In[122]:

ls_AAo_m1e_0 = []
for i in AAo_m1e.split('\n')[1:]:
    if i.split(',')[0] in keys_AAo:
        ls_AAo_m1e_0.append(i.split(',')[:3]+dAAo[i.split(',')[0]].split(','))
    else:
        ls_AAo_m1e_0.append(i.split(',')[:3]+['-','-'])

ls_AAo_m1e_1 = []
for i in AAo_m1e.split('\n')[1:]:
    if i.split(',')[3] in keys_AAo:
        ls_AAo_m1e_1.append(i.split(',')[3:-1]+dAAo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_AAo_m1e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_AAo_m1e = ','.join([head2]+[','.join(ls_AAo_m1e_0[i] + ls_AAo_m1e_1[i])+'\n'   for i in range(len(ls_AAo_m1e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m1e.csv', 'w')
z.write(ls_AAo_m1e)
z.close()


# In[123]:

ls_AAo_m3e_0 = []
for i in AAo_m3e.split('\n')[1:]:
    if i.split(',')[0] in keys_AAo:
        ls_AAo_m3e_0.append(i.split(',')[:3]+dAAo[i.split(',')[0]].split(','))
    else:
        ls_AAo_m3e_0.append(i.split(',')[:3]+['-','-'])

ls_AAo_m3e_1 = []
for i in AAo_m3e.split('\n')[1:]:
    if i.split(',')[3] in keys_AAo:
        ls_AAo_m3e_1.append(i.split(',')[3:-1]+dAAo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_AAo_m3e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_AAo_m3e = ','.join([head2]+[','.join(ls_AAo_m3e_0[i] + ls_AAo_m3e_1[i])+'\n'   for i in range(len(ls_AAo_m3e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m3e.csv', 'w')
z.write(ls_AAo_m3e)
z.close()


# In[124]:

ls_AAo_f1e_0 = []
for i in AAo_f1e.split('\n')[1:]:
    if i.split(',')[0] in keys_AAo:
        ls_AAo_f1e_0.append(i.split(',')[:3]+dAAo[i.split(',')[0]].split(','))
    else:
        ls_AAo_f1e_0.append(i.split(',')[:3]+['-','-'])

ls_AAo_f1e_1 = []
for i in AAo_f1e.split('\n')[1:]:
    if i.split(',')[3] in keys_AAo:
        ls_AAo_f1e_1.append(i.split(',')[3:-1]+dAAo[i.split(',')[3]].split(',')+[i.split(',')[-1]])
    else:
        ls_AAo_f1e_1.append(i.split(',')[3:-1]+['-','-']+[i.split(',')[-1]])
        
ls_AAo_f1e = ','.join([head2]+[','.join(ls_AAo_f1e_0[i] + ls_AAo_f1e_1[i])+'\n'   for i in range(len(ls_AAo_f1e_0)) ]).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_f1e.csv', 'w')
z.write(ls_AAo_f1e)
z.close()


# In[ ]:



