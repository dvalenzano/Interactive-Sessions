
# coding: utf-8

# Goal: to build a table with all the significant markers, in all groups, and generate sets of intersections

# In[14]:

# g stands for cross Go
g7m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/mal/fam_7m_sqtl_sig',  'rU').read()
g7f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/fem/fam_7f_sqtl_sig',  'rU').read()
g14m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/mal/fam_14m_sqtl_sig',  'rU').read()
g14f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/fem/fam_14f_sqtl_sig',  'rU').read()
g8m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/mal/fam_8m_sqtl_sig', 'rU').read()
g8f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/fem/fam_8f_sqtl_sig', 'rU').read()
g1_1m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_1.1/mal/fam_1.1m_sqtl_sig',  'rU').read()
g1_1f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_1.1/fem/fam_1.1f_sqtl_sig',  'rU').read()
# ge stands for the markers significant in epistatic interaction
ge7m = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7m/epistasis_7m.csv','rU').read()
ge7f = open('/Volumes/group_dv/personal/DValenzano/May2014/f7/f7f/epistasis_7f.csv','rU').read()
ge14m = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14m/epistasis_14m.csv','rU').read()
ge14f = open('/Volumes/group_dv/personal/DValenzano/May2014/f14/f14f/epistasis_14f.csv','rU').read()
ge8m = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8m/epistasis_8m.csv','rU').read()
ge8f = open('/Volumes/group_dv/personal/DValenzano/May2014/f8/f8f/epistasis_8f.csv','rU').read()
# aa stands for cross AAo
aa1m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_1m_sqtl_sig', 'rU').read()
aa1f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_1f_sqtl_sig', 'rU').read()
aa3m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_3m_sqtl_sig', 'rU').read()
aa3f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_3f_sqtl_sig', 'rU').read()
# aae stands for the markers significant in epistatic interaction
aae1m = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/epistasis_1m.csv', 'rU').read()
aae1f = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/epistasis_1f.csv', 'rU').read()
aae3m = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/epistasis_3m.csv', 'rU').read()


# First, the list of significant markers for each group

# In[15]:

g7m_l = [ i.split()[1] for i in g7m.split('\n')[1:-1] ]
g14m_l = [ i.split()[1] for i in g14m.split('\n')[1:-1] ]
g8m_l = [ i.split()[1] for i in g8m.split('\n')[1:-1] ]
g1_1m_l = [ i.split()[1] for i in g1_1m.split('\n')[1:-1] ]
g7f_l = [ i.split()[1] for i in g7f.split('\n')[1:-1] ]
g14f_l = [ i.split()[1] for i in g14f.split('\n')[1:-1] ]
g8f_l = [ i.split()[1] for i in g8f.split('\n')[1:-1] ]
g1_1f_l = [ i.split()[1] for i in g1_1f.split('\n')[1:-1] ]


# In[16]:

from sets import Set
ge7m_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in ge7m.split('\n')[1:]])).split(',')))
ge7f_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in ge7f.split('\n')[1:]])).split(',')))
ge14m_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in ge14m.split('\n')[1:]])).split(',')))
ge14f_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in ge14f.split('\n')[1:]])).split(',')))
ge8m_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in ge8m.split('\n')[1:]])).split(',')))
ge8f_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in ge8f.split('\n')[1:]])).split(',')))


# In[17]:

aa1m_l = [ i.split()[1] for i in aa1m.split('\n')[1:-1] ]
aa1f_l = [ i.split()[1] for i in aa1f.split('\n')[1:-1] ]
aa3m_l = [ i.split()[1] for i in aa3m.split('\n')[1:-1] ]
#
aae1m_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in aae1m.split('\n')[1:]])).split(',')))
aae1f_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in aae1f.split('\n')[1:]])).split(',')))
aae3m_l = list(Set((','.join([i.split(',')[0]+','+i.split(',')[3] for i in aae3m.split('\n')[1:]])).split(',')))


# Now I need to analyze the data cross by cross - First cross G

# In[ ]:

#import re
#def intersect(inp_name):
#    inps = str(inp_name)
#    match =  [match.group() if search.re(r'\d+', inps)]   


# Males First

# First:  
# 7m-14m-1_1m-8m  
# 7m-14m-1_1m  
# 7m-14m-8m  
# 7m-1_1m-8m
# 7m-14m  
# 7m-1_1m
# 7m-8m
# 14m-1_1m-8m  
# 14m-1_1m  
# 14m-8m  
# 1_1m-8m  

# In[74]:

gm_all = map(set, (g7m_l, g14m_l, g8m_l, g1_1m_l))
gmu_all = set.intersection(*gm_all)
print(
'overlap between 7m, 14m, 8m, 1_1m: \n' + str(len(gmu_all)) +' markers'
)


# In[65]:

gm_7_14_1 = map(set, (g7m_l, g14m_l, g1_1m_l))
gmu_7_14_1 = set.intersection(*gm_7_14_1)
print(
'overlap between 7m, 14m, 1_1m: \n' + str(len(gmu_7_14_1)) +' markers'
)


# In[66]:

gm_7_14_8 = map(set, (g7m_l, g14m_l, g8m_l))
gmu_7_14_8 = set.intersection(*gm_7_14_8)
print(
'overlap between 7m, 14m, 8m: \n' + str(len(gmu_7_14_8)) +' markers'
)


# In[71]:

gm_7_8_1 = map(set, (g7m_l, g8m_l, g1_1m_l))
gmu_7_8_1 = set.intersection(*gm_7_8_1)
print(
'overlap between 7m, 8m, 1_1m: \n' + str(len(gmu_7_8_1)) +' markers'
)


# In[82]:

gm_7_14 = map(set, (g7m_l, g14m_l))
gmu_7_14 = set.intersection(*gm_7_14)
print(
'overlap between 7m, 14m: \n' + str(len(gmu_7_14)) +' markers'
)


# In[72]:

gm_7_1 = map(set, (g7m_l, g1_1m_l))
gmu_7_1 = set.intersection(*gm_7_1)
print(
'overlap between 7m, 1_1m: \n' + str(len(gmu_7_1)) +' markers'
)


# In[73]:

gm_7_8 = map(set, (g7m_l, g8m_l))
gmu_7_8 = set.intersection(*gm_7_8)
print(
'overlap between 7m, 8m: \n' + str(len(gmu_7_8)) +' markers'
)


# In[75]:

gm_14_1_8 = map(set, (g14m_l, g8m_l, g1_1m_l))
gmu_14_1_8 = set.intersection(*gm_14_1_8)
print(
'overlap between 14m, 8m, 1_1m: \n' + str(len(gmu_14_1_8)) +' markers'
)


# In[76]:

gm_14_8 = map(set, (g14m_l, g8m_l))
gmu_14_8 = set.intersection(*gm_14_8)
print(
'overlap between 14m, 8m: \n' + str(len(gmu_14_8)) +' markers'
)


# In[77]:

gm_14_1 = map(set, (g14m_l, g1_1m_l))
gmu_14_1 = set.intersection(*gm_14_1)
print(
'overlap between 14m, 1_1m: \n' + str(len(gmu_14_1)) +' markers'
)


# In[78]:

gm_8_1 = map(set, (g8m_l, g1_1m_l))
gmu_8_1 = set.intersection(*gm_8_1)
print(
'overlap between 8m, 1_1m: \n' + str(len(gmu_8_1)) +' markers'
)


# Now the same, for females  
#   
# 7f-14f-1_1f-8f  
# 7f-14f-1_1f  
# 7f-14f-8f  
# 7f-1_1f-8f
# 7f-14f  
# 7f-1_1f
# 7f-8f
# 14f-1_1f-8f  
# 14f-1_1f  
# 14f-8f  
# 1_1f-8f  

# In[83]:

gf_all = map(set, (g7f_l, g14f_l, g8f_l, g1_1f_l))
gfu_all = set.intersection(*gf_all)

gf_7_14_1 = map(set, (g7f_l, g14f_l, g1_1f_l))
gfu_7_14_1 = set.intersection(*gf_7_14_1)

gf_7_14_8 = map(set, (g7f_l, g14f_l, g8f_l))
gfu_7_14_8 = set.intersection(*gf_7_14_8)

gf_7_8_1 = map(set, (g7f_l, g8f_l, g1_1f_l))
gfu_7_8_1 = set.intersection(*gf_7_8_1)

gf_7_14 = map(set, (g7f_l, g14f_l))
gfu_7_14 = set.intersection(*gf_7_14)

gf_7_1 = map(set, (g7f_l, g1_1f_l))
gfu_7_1 = set.intersection(*gf_7_1)

gf_7_8 = map(set, (g7f_l, g8f_l))
gfu_7_8 = set.intersection(*gf_7_8)

gf_14_1_8 = map(set, (g14f_l, g8f_l, g1_1f_l))
gfu_14_1_8 = set.intersection(*gf_14_1_8)

gf_14_8 = map(set, (g14f_l, g8f_l))
gfu_14_8 = set.intersection(*gf_14_8)

gf_14_1 = map(set, (g14f_l, g1_1f_l))
gfu_14_1 = set.intersection(*gf_14_1)

gf_8_1 = map(set, (g8f_l, g1_1f_l))
gfu_8_1 = set.intersection(*gf_8_1)

print(
'overlap between 7f, 14f, 8f, 1_1f: \n' + str(len(gfu_all)) +' markers'
)

print(
'overlap between 7f, 14f, 1_1f: \n' + str(len(gfu_7_14_1)) +' markers'
)

print(
'overlap between 7f, 14f, 8f: \n' + str(len(gfu_7_14_8)) +' markers'
)

print(
'overlap between 7f, 8f, 1_1f: \n' + str(len(gfu_7_8_1)) +' markers'
)

print(
'overlap between 7f, 14f: \n' + str(len(gfu_7_14)) +' markers'
)

print(
'overlap between 7f, 1_1f: \n' + str(len(gfu_7_1)) +' markers'
)

print(
'overlap between 7f, 8f: \n' + str(len(gfu_7_8)) +' markers'
)

print(
'overlap between 14f, 8f, 1_1f: \n' + str(len(gfu_14_1_8)) +' markers'
)

print(
'overlap between 14f, 8f: \n' + str(len(gfu_14_8)) +' markers'
)

print(
'overlap between 14f, 1_1f: \n' + str(len(gfu_14_1)) +' markers'
)

print(
'overlap between 8f, 1_1f: \n' + str(len(gfu_8_1)) +' markers'
)


# Then within each family, male and female:

# In[90]:

g7_mf = map(set, (g7m_l, g7f_l))
g7u_mf = set.intersection(*g7_mf)

g14_mf = map(set, (g7m_l, g14f_l))
g14u_mf = set.intersection(*g14_mf)

g8_mf = map(set, (g8m_l, g8f_l))
g8u_mf = set.intersection(*g8_mf)

g1_mf = map(set, (g1_1m_l, g1_1f_l))
g1u_mf = set.intersection(*g1_mf)

print(
'overlap between 7m and 7f: \n' + str(len(g7u_mf)) +' markers'
)

print(
'\noverlap between 14m and 14f: \n' + str(len(g14u_mf)) +' markers'
)

print(
'\noverlap between 8m and 8f: \n' + str(len(g8u_mf)) +' markers'
)

print(
'\noverlap between 1_1m and 1_1f: \n' + str(len(g1u_mf)) +' markers'
)


# Now the same, for cross AAo  
# First males: 

# In[92]:

aa_all = map(set, (aa1m_l, aa3m_l, aa1f_l))
aau_all = set.intersection(*aa_all)

aam_all = map(set, (aa1m_l, aa3m_l))
aamu_all = set.intersection(*aam_all)

print(
'overlap between 1m, 1f and 3m: \n' + str(len(aau_all)) +' markers'
)

print(
'\noverlap between 1m and 3m: \n' + str(len(aamu_all)) +' markers'
)


# Now the same for epistatically interacting markers

# In[98]:

gem_all = map(set, (ge7m_l, ge14m_l, ge8m_l))
gemu_all = set.intersection(*gem_all)

gem_7_14_8 = map(set, (ge7m_l, ge14m_l, ge8m_l))
gemu_7_14_8 = set.intersection(*gem_7_14_8)

gem_7_14 = map(set, (ge7m_l, ge14m_l))
gemu_7_14 = set.intersection(*gem_7_14)

gem_7_8 = map(set, (ge7m_l, ge8m_l))
gemu_7_8 = set.intersection(*gem_7_8)

gem_14_8 = map(set, (ge14m_l, ge8m_l))
gemu_14_8 = set.intersection(*gem_14_8)

print(
'overlap between 7em, 14em, 8em: \n' + str(len(gemu_7_14_8)) +' markers'
)

print(
'overlap between 7em, 14em: \n' + str(len(gemu_7_14)) +' markers'
)

print(
'overlap between 7em, 8em: \n' + str(len(gemu_7_8)) +' markers'
)
 
print(
'overlap between 14em, 8em: \n' + str(len(gemu_14_8)) +' markers'
)


# In[100]:

gef_all = map(set, (ge7f_l, ge14f_l, ge8f_l))
gefu_all = set.intersection(*gef_all)

gef_7_14_8 = map(set, (ge7f_l, ge14f_l, ge8f_l))
gefu_7_14_8 = set.intersection(*gef_7_14_8)

gef_7_14 = map(set, (ge7f_l, ge14f_l))
gefu_7_14 = set.intersection(*gef_7_14)

gef_7_8 = map(set, (ge7f_l, ge8f_l))
gefu_7_8 = set.intersection(*gef_7_8)

gef_14_8 = map(set, (ge14f_l, ge8f_l))
gefu_14_8 = set.intersection(*gef_14_8)

print(
'overlap between 7ef, 14ef, 8ef: \n' + str(len(gefu_7_14_8)) +' markers'
)

print(
'overlap between 7ef, 14ef: \n' + str(len(gefu_7_14)) +' markers'
)

print(
'overlap between 7ef, 8ef: \n' + str(len(gefu_7_8)) +' markers'
)
 
print(
'overlap between 14ef, 8ef: \n' + str(len(gefu_14_8)) +' markers'
)


# 

# In[ ]:



