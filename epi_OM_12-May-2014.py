
# coding: utf-8

# In[3]:

lg7f = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7f/LGes.txt', 'rU').read()
lg7fs = lg7f.split('\n\n')[:-1]


# In[69]:

alls7f = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg7fs[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg7fs)) ]
allj7f = ','.join(alls7f).replace('\n,','\n')[:-1]


z = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7f/LGs2.txt', 'w')
z.write(allj7f)
z.close()


# In[5]:

lg14f = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14f/LGes.txt', 'rU').read()
lg14fs = lg14f.split('\n\n')[:-1]
alls14f = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg14fs[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg14fs)) ]
allj14f = ','.join(alls14f).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14f/LGs2.txt', 'w')
z.write(allj14f)
z.close()


# In[6]:

lg8f = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8f/LGes.txt', 'rU').read()
lg8fs = lg8f.split('\n\n')[:-1]
alls8f = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg8fs[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg8fs)) ]
allj8f = ','.join(alls8f).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8f/LGs2.txt', 'w')
z.write(allj8f)
z.close()


# In[8]:

epi7f = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7f/fam_7f.epi.qt', 'rU').read()
epi14f = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14f/fam_14f.epi.qt', 'rU').read()
epi8f = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8f/fam_8f.epi.qt', 'rU').read()


# In[9]:

epi7f_n =[ i  for i in epi7f.split('\n')[1:-1] if float(i.split()[-1])<(0.01/7644)]
epi14f_n =[ i  for i in epi14f.split('\n')[1:-1] if float(i.split()[-1])<(0.01/7688)]
epi8f_n =[ i  for i in epi8f.split('\n')[1:-1] if float(i.split()[-1])<(0.01/7694)]


# In[10]:

keys_7f = [ i.split(',')[0] for i in allj7f.split('\n')[:-1]]
values_7f = [ i for i in allj7f.split('\n')[:-1]]
d_7f = dict(zip(keys_7f, values_7f))

keys_14f = [ i.split(',')[0] for i in allj14f.split('\n')[:-1]]
values_14f = [ i for i in allj14f.split('\n')[:-1]]
d_14f = dict(zip(keys_14f, values_14f))

keys_8f = [ i.split(',')[0] for i in allj8f.split('\n')[:-1]]
values_8f = [ i for i in allj8f.split('\n')[:-1]]
d_8f = dict(zip(keys_8f, values_8f))


# In[11]:

head='M#1,LG_M#1,cM_M#1,M#2,LG_M#2,cm_M#2,p-val\n'


# In[12]:

ls_7f = []
for i in epi7f_n:
    if i.split()[1] in keys_7f and i.split()[3] in keys_7f:
        ls_7f.append(d_7f[i.split()[1]]+','+ d_7f[i.split()[3]] +','+ i.split()[-1]+'\n')
        
ls_14f = []
for i in epi14f_n:
    if i.split()[1] in keys_14f and i.split()[3] in keys_14f:
        ls_14f.append(d_14f[i.split()[1]]+','+ d_14f[i.split()[3]] +','+ i.split()[-1]+'\n')
        
ls_8f = []
for i in epi8f_n:
    if i.split()[1] in keys_8f and i.split()[3] in keys_8f:
        ls_8f.append(d_8f[i.split()[1]]+','+ d_8f[i.split()[3]] +','+ i.split()[-1]+'\n')


# In[13]:

fin_7f = head+','.join(ls_7f).replace('\n,','\n')[:-1]
fin_14f = head+','.join(ls_14f).replace('\n,','\n')[:-1]
fin_8f = head+','.join(ls_8f).replace('\n,','\n')[:-1]


# In[14]:

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7f/epistasis_7f.csv', 'w')
z.write(fin_7f)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14f/epistasis_14f.csv', 'w')
z.write(fin_14f)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8f/epistasis_8f.csv', 'w')
z.write(fin_8f)
z.close()


# In[ ]:



