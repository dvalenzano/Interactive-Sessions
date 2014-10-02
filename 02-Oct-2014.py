
# coding: utf-8

# Goal: to generate a file with markers on the left column, and p-value on the right column, for g7m and g14m
# The actual goal is to generate an input file like g_days2.csv

# In[1]:

#Phenotype and genotype data:
goped7 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped7.csv', 'rU').read()
#Position data (markers and position on consensus linkage map):
consmap = open('/Volumes/group_dv/personal/DValenzano/Sep2014/LG12_m7-14-rf_consensus.csv', 'rU').read()
#P values for fam7:
pvals7 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/mal/fam_7m_sqtl.assoc.linear', 'rU').read()
#P values for fam14:
pvals14 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/mal/fam_14m_sqtl.assoc.linear', 'rU').read()


# First, I need to split goped7 in family 7 males and family 14 males - then, I will convert the genotypes in integers

# In[36]:

goped7_2 = goped7.replace('fam', '')

gfam7 = [i for i in goped7_2.split('\n') if i.split(',')[0] == '7']
gm7 = [','.join(goped7_2.split('\n')[0].split(',')[:2]+goped7_2.split('\n')[0].split(',')[4:6]+goped7_2.split('\n')[0].split(',')[10:])]+ [','.join(i.split(',')[:2]+i.split(',')[4:6]+i.split(',')[10:]) for i in gfam7[:2]]+[','.join(i.split(',')[:2]+i.split(',')[4:6]+i.split(',')[10:]) for i in gfam7[4:] if  i.split(',')[4]=='1']
gm7_2 = ','.join([i+'\n' for i in gm7]).replace('\n,','\n').replace(',0',',na').replace(',aa', ',0').replace(',ab',',1').replace(',bb',',2')

gfam14 = [i for i in goped7_2.split('\n') if i.split(',')[0] == '14']
gm14 = [','.join(goped7_2.split('\n')[0].split(',')[:2]+goped7_2.split('\n')[0].split(',')[4:6]+goped7_2.split('\n')[0].split(',')[10:])]+ [','.join(i.split(',')[:2]+i.split(',')[4:6]+i.split(',')[10:]) for i in gfam14[:2]]+[','.join(i.split(',')[:2]+i.split(',')[4:6]+i.split(',')[10:]) for i in gfam14[4:] if  i.split(',')[4]=='1']
gm14_2 = ','.join([i+'\n' for i in gm14]).replace('\n,','\n').replace(',0',',na').replace(',aa', ',0').replace(',ab',',1').replace(',bb',',2')


# In[136]:

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/gm7_2.csv', 'w')
z.write(gm7_2)
z.close()


# Now I need to sort the genotypes by marker position on the LM and then I need to add the p-values to the short list of markers

# In[45]:

# First, I need to double check that all the markers in the newly sorted consensus map are also in the list of markers 
# genotyped in goped7
markers0 = ','.join(goped7.split('\n')[0].split(',')[10:])
markers1 = ','.join([ i.split()[1] for i in consmap.split('\n')[1:-1] ])


# In[49]:

from sets import Set
Set(markers1.split(',')) <= Set(markers0.split(','))


# In[57]:

# Now I need to build a dictionary with marker name as key, and p-value as value in both families
k7m =  [ i.split()[1] for i in pvals7.split('\n')[1:-1] ]
v7m =  [ i.split()[-1] for i in pvals7.split('\n')[1:-1] ]
d7m = dict(zip(k7m, v7m))

k14m =  [ i.split()[1] for i in pvals14.split('\n')[1:-1] ]
v14m =  [ i.split()[-1] for i in pvals14.split('\n')[1:-1] ]
d14m = dict(zip(k14m, v14m))


# In[144]:

k7_14 = list(Set(k7m)&Set(k14m))


# In[66]:

# I got to first transpose the matrices with genotypes and phenotypes
g7mt = [ list(i) for i in zip(*[i.split(',') for i in gm7_2.split('\n')[:-1]])]
g14mt = [ list(i) for i in zip(*[i.split(',') for i in gm14_2.split('\n')[:-1]])]


# In[82]:

# and I generate a dictionary with marker and genotype as value
k7m0 = [i[0] for i in g7mt]
v7m0 = [i[1:] for i in g7mt]
d7m0 = dict(zip(k7m0, v7m0))

k14m0 = [i[0] for i in g14mt]
v14m0 = [i[1:] for i in g14mt]
d14m0 = dict(zip(k14m0, v14m0))


# In[70]:

# Then I need the list of markers on the actual LG, with maker and position
kmap = [i.split()[1] for i in consmap.split('\n')[1:-1]]
vmap = [i.split()[2] for i in consmap.split('\n')[1:-1]]
dmap = dict(zip(kmap, vmap))


# In[145]:

g7m_gmatr = [i + ','+dmap[i] + ','+d7m[i] +','+ ','.join(d7m0[i]) for i in kmap if i in k7_14]
g14m_gmatr = [i + ','+dmap[i] + ','+d14m[i] +','+ ','.join(d14m0[i]) for i in kmap if i in k7_14]


# In[146]:

g7m_2 = [['','','individual']+list(g7mt[1][1:])] + [['','','sex']+list(g7mt[2][1:])] + [['','','days']+list(g7mt[3][1:])] + [i.split(',') for i in g7m_gmatr] 
g7m_3 = [list(i) for i in zip(*g7m_2)]

g14m_2 = [['','','individual']+list(g14mt[1][1:])] + [['','','sex']+list(g14mt[2][1:])] + [['','','days']+list(g14mt[3][1:])] + [i.split(',') for i in g14m_gmatr] 
g14m_3 = [list(i) for i in zip(*g14m_2)]


# In[147]:

g7m_4 = ','.join([','.join(list(i))+'\n' for i in g7m_3]).replace('\n,','\n')
g14m_4 = ','.join([','.join(list(i))+'\n' for i in g14m_3]).replace('\n,','\n')


# In[148]:

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g7mdays_2.csv', 'w')
z.write(g7m_4)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g14mdays_2.csv', 'w')
z.write(g14m_4)
z.close()


# In[ ]:




# In[ ]:




# In[61]:




# In[58]:

gm14_2.split('\n')[:4]


# In[ ]:



