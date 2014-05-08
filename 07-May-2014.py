
# coding: utf-8

# In[1]:

lg8m = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8m/LGs.txt', 'rU').read()
lg8ms = lg8m.split('\n\n')[:-1]
alls8m = [ ','.join([ j.split()[1]+','+str(i+1)+','+j.split()[2]+'\n' for j in lg8ms[i].split('\n')]).replace('\n,','\n')    for i in range(len(lg8ms)) ]
allj8m = ','.join(alls8m).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8m/LGs2.txt', 'w')
z.write(allj8m)
z.close()


# In[2]:

epi8m = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8m/fam_8m.epi.qt', 'rU').read()


# In[3]:

epi8m_n =[ i  for i in epi8m.split('\n')[1:-1] if float(i.split()[-1])<(0.01/7694)]


# epi8m_n is the lists of epistatic pairs of markers that are highly significant (corrected after Bonferroni)

# In[4]:

keys_8m = [ i.split(',')[0] for i in allj8m.split('\n')[:-1]]
values_8m = [ i for i in allj8m.split('\n')[:-1]]
d_8m = dict(zip(keys_8m, values_8m))


# In[5]:

head='M#1,LG_M#1,cM_M#1,M#2,LG_M#2,cm_M#2,p-val\n'


# In[6]:

ls_8m = []
for i in epi8m_n:
    if i.split()[1] in keys_8m and i.split()[3] in keys_8m:
        ls_8m.append(d_8m[i.split()[1]]+','+ d_8m[i.split()[3]] +','+ i.split()[-1]+'\n')
        
#as list comprehension (it works):
#[d_7m[i.split()[1]] +','+ d_7m[i.split()[3]] +','+ i.split()[-1]+'\n' for i in epi7m_n if i.split()[1] in keys_7m and i.split()[3] in keys_7m]


# In[7]:

fin_8m = head+','.join(ls_8m).replace('\n,','\n')[:-1]


# In[8]:

z = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8m/epistasis_8m.csv', 'w')
z.write(fin_8m)
z.close()


# In[8]:



