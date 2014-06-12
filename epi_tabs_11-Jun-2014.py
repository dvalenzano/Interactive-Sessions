
# coding: utf-8

# First, cross Go

# In[78]:

go_map = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read().replace('"","chr","pos"\n','').replace('"','')
epi_7m = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m7e_sorted.csv', 'rU').read()
epi_14m = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m14e_sorted.csv', 'rU').read()
epi_8m = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m8e_sorted.csv', 'rU').read()
epi_7f = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f7e_sorted.csv', 'rU').read()
epi_14f = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f14e_sorted.csv', 'rU').read()
epi_8f = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f8e_sorted.csv', 'rU').read()


# In[79]:

from sets import Set
epi_7mk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_7m.split('\n')[1:-1]]).split(',')))
epi_14mk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_14m.split('\n')[1:-1]]).split(',')))
epi_8mk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_8m.split('\n')[1:-1]]).split(',')))
epi_7fk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_7f.split('\n')[1:-1]]).split(',')))
epi_14fk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_14f.split('\n')[1:-1]]).split(',')))
epi_8fk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_8f.split('\n')[1:-1]]).split(',')))


# In[80]:

head = 'marker,LG,pos,7me,14me,8me,7fe,14me,8fe\n'


# In[81]:

epi_7mk_yn = [ '1' if i.split(',')[0] in epi_7mk else '0' for i in go_map.split('\n')[:-1] ]
epi_14mk_yn = [ '1' if i.split(',')[0] in epi_14mk else '0' for i in go_map.split('\n')[:-1] ]
epi_8mk_yn = [ '1' if i.split(',')[0] in epi_8mk else '0' for i in go_map.split('\n')[:-1] ]
epi_7fk_yn = [ '1' if i.split(',')[0] in epi_7fk else '0' for i in go_map.split('\n')[:-1] ]
epi_14fk_yn = [ '1' if i.split(',')[0] in epi_14fk else '0' for i in go_map.split('\n')[:-1] ]
epi_8fk_yn = [ '1' if i.split(',')[0] in epi_8fk else '0' for i in go_map.split('\n')[:-1] ]


# In[82]:

go_mapt =  [list(i) for i in zip(*[ i.split(',') for i in go_map.split('\n')[:-1]])]


# In[83]:

gm2 = go_mapt+[epi_7mk_yn,epi_14mk_yn,epi_8mk_yn,epi_7fk_yn,epi_14fk_yn,epi_8fk_yn]


# In[84]:

gm2t = head+','.join([','.join(list(i))+'\n' for i in zip(*gm2)]).replace('\n,','\n')


# In[85]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/epiGotab.csv', 'w')
z.write(gm2t)
z.close()


# Then, cross AAo

# In[86]:

aao_map = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read().replace('"","chr","pos"\n','').replace('"','')
epi_1m = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m1e_sorted.csv', 'rU').read()
epi_3m = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m3e_sorted.csv', 'rU').read()
epi_1f = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_f1e_sorted.csv', 'rU').read()

epi_1mk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_1m.split('\n')[1:-1]]).split(',')))
epi_3mk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_3m.split('\n')[1:-1]]).split(',')))
epi_1fk = list(Set(','.join([ i.split(',')[0]+','+i.split(',')[5]   for i in epi_1f.split('\n')[1:-1]]).split(',')))

head = 'marker,LG,pos,1me,3me,1fe\n'

epi_1mk_yn = [ '1' if i.split(',')[0] in epi_1mk else '0' for i in aao_map.split('\n')[:-1] ]
epi_3mk_yn = [ '1' if i.split(',')[0] in epi_3mk else '0' for i in aao_map.split('\n')[:-1] ]
epi_1fk_yn = [ '1' if i.split(',')[0] in epi_1fk else '0' for i in aao_map.split('\n')[:-1] ]

aao_mapt =  [list(i) for i in zip(*[ i.split(',') for i in aao_map.split('\n')[:-1]])]

aam2 = aao_mapt+[epi_1mk_yn,epi_3mk_yn,epi_1fk_yn]

aam2t = head+','.join([','.join(list(i))+'\n' for i in zip(*aam2)]).replace('\n,','\n')


# In[87]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/epiAAotab.csv', 'w')
z.write(aam2t)
z.close()


# In[77]:




# In[ ]:



