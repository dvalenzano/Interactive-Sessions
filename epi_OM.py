
# coding: utf-8

# In[4]:

lg7m = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/LGs.txt', 'rU').read()
lg7ms = lg7m.split('\n\n')[:-1]


# In[69]:

alls7m = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg7ms[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg7ms)) ]
allj7m = ','.join(alls).replace('\n,','\n')[:-1]


# In[43]:

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/LGs2.txt', 'w')
z.write(allj7m)
z.close()


# In[44]:

lg14m = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/LGs.txt', 'rU').read()
lg14ms = lg14m.split('\n\n')[:-1]
alls14m = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg14ms[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg14ms)) ]
allj14m = ','.join(alls14m).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/LGs2.txt', 'w')
z.write(allj14m)
z.close()


# In[46]:

epi7m = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/fam_7m.epi.qt', 'rU').read()
epi14m = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/fam_14m.epi.qt', 'rU').read()


# In[78]:

epi7m_n =[ i  for i in epi7m.split('\n')[1:-1] if float(i.split()[-1])<(0.01/7644)]
epi14m_n =[ i  for i in epi14m.split('\n')[1:-1] if float(i.split()[-1])<(0.01/7688)]


# epi7m_n and epi14m_n are the lists of epistatic pairs of markers that are highly significant (corrected after Bonferroni)

# In[79]:

keys_7m = [ i.split(',')[0] for i in allj7m.split('\n')[:-1]]
values_7m = [ i for i in allj7m.split('\n')[:-1]]
d_7m = dict(zip(keys_7m, values_7m))

keys_14m = [ i.split(',')[0] for i in allj14m.split('\n')[:-1]]
values_14m = [ i for i in allj14m.split('\n')[:-1]]
d_14m = dict(zip(keys_14m, values_14m))


# In[109]:

head='M#1,LG_M#1,cM_M#1,M#2,LG_M#2,cm_M#2,p-val\n'


# In[105]:

ls_7m = []
for i in epi7m_n:
    if i.split()[1] in keys_7m and i.split()[3] in keys_7m:
        ls_7m.append(d_7m[i.split()[1]]+','+ d_7m[i.split()[3]] +','+ i.split()[-1]+'\n')
        
#as list comprehension (it works):
#[d_7m[i.split()[1]] +','+ d_7m[i.split()[3]] +','+ i.split()[-1]+'\n' for i in epi7m_n if i.split()[1] in keys_7m and i.split()[3] in keys_7m]


# In[110]:

fin_7m = head+','.join(ls_7m).replace('\n,','\n')[:-1]


# In[112]:

ls_14m = []
for i in epi14m_n:
    if i.split()[1] in keys_14m and i.split()[3] in keys_14m:
        ls_14m.append(d_14m[i.split()[1]]+','+ d_14m[i.split()[3]] +','+ i.split()[-1]+'\n')
fin_14m = head+','.join(ls_14m).replace('\n,','\n')[:-1]


# In[116]:

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/epistasis_7m.csv', 'w')
z.write(fin_7m)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/epistasis_14m.csv', 'w')
z.write(fin_14m)
z.close()


# In[ ]:



