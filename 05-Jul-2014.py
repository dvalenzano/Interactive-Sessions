
# coding: utf-8

#### Goal: to plot the q-values in the random forest QTL linkage group by linkage group  First with the rqtl map, then with the others

# In[1]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/gQTL.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aaQTL.csv', 'rU').read()


# In[8]:

g2= [g.split('\n')[0]]+  [i  for i in g.split('\n')[1:-1] if i.split(',')[15]!= "" ] 


# In[35]:

g3 = [i for i in g2 if i.split(',')[14]!='-']
g4 = [g3[0].split(',')[:14]+['LG','cM']+g3[0].split(',')[15:]]+[i.split(',')[:14]+i.split(',')[14].split('_')+i.split(',')[15:] for i in g3[1:]]


# In[97]:

import math
g5 = [g4[0]]+[i[:16]+map(str, [ -1*x if x != 0 else x for x in map(math.log, map(float, i[16:]))]) for i in g4[1:]]


# In[98]:

g6 = ','.join([','.join(i)+'\n' for i in g5 ]).replace('\n,','\n')


# In[103]:

aa2 = [aa.split('\n')[0]]+  [i  for i in aa.split('\n')[1:-1] if i.split(',')[8]!= "" ] 
aa3 = [i for i in aa2 if i.split(',')[7]!='-']
aa4 = [aa3[0].split(',')[:7]+['LG','cM']+aa3[0].split(',')[8:]]+[i.split(',')[:7]+i.split(',')[7].split('_')+i.split(',')[8:] for i in aa3[1:]]


# In[104]:

aa5 = [aa4[0]]+[i[:9]+map(str, [ -1*x if x != 0 else x for x in map(math.log, map(float, i[9:]))]) for i in aa4[1:]]


# In[105]:

aa6 = ','.join([','.join(i)+'\n' for i in aa5 ]).replace('\n,','\n')


# In[108]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qval_g.csv','w')
z.write(g6)
z.close()
z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qval_aa.csv','w')
z.write(aa6)
z.close()


# Now I need to do the same thing for ALL the markers analyzed by random forest, rather than those that are signficant   
# for random forest and for my analysis

# In[109]:

aarqtl = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read()
grqtl = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read()
aarf = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/aao_qval.tsv', 'rU').read()
grf = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/go_qval.tsv', 'rU').read()


# In[129]:

aarf2 =[ [i.split('\t')[0].replace('X','')]+[i.split('\t')[2]]+i.split('\t')[-3:] for i in aarf.split('\n')[:-1]]
grf2 =[ [i.split('\t')[0].replace('X','')]+[i.split('\t')[2]]+i.split('\t')[-3:] for i in grf.split('\n')[:-1]]


# In[169]:

from sets import Set

krf_aa = [i[0] for i in aarf2[1:]]
krq_aa = [i.split(',')[0] for i in aarqtl.replace('"','').split('\n')[1:-1]]
k_aa = list(Set(krf_aa)&Set(krq_aa))

krf_g = [i[0] for i in grf2[1:]]
krq_g = [i.split(',')[0] for i in grqtl.replace('"','').split('\n')[1:-1]]
k_g = list(Set(krf_g)&Set(krq_g))

vrf_aa = [i[1:] for i in aarf2[1:]]
vrq_aa = [i.split(',')[1:] for i in aarqtl.replace('"','').split('\n')[1:-1]]

vrf_g = [i[1:] for i in grf2[1:]]
vrq_g = [i.split(',')[1:] for i in grqtl.replace('"','').split('\n')[1:-1]]

drf_aa = dict(zip(krf_aa, vrf_aa))
drq_aa = dict(zip(krq_aa, vrq_aa))

drf_g = dict(zip(krf_g, vrf_g))
drq_g= dict(zip(krq_g, vrq_g))


# In[191]:

aa0_sorted = [[i]+map(float, drq_aa[i])+map(float, drf_aa[i]) for i in k_aa ]
aa1_sorted = sorted(aa0_sorted, key= lambda x: (x[1], x[2]))
aa2_sorted = [[i[0]] +map(str, i[1:3])+ map(str, [-1*j if j!=0 else j for j in map(math.log, map(float, i[3:]) )] ) for i in aa1_sorted ]
aa_fin = 'Marker,LG,cM,days,daysM,daysF,daysRes\n'+ ','.join([ ','.join(i)+'\n' for i in aa2_sorted ]).replace('\n,','\n')


# In[192]:

g0_sorted = [[i]+map(float, drq_g[i])+map(float, drf_g[i]) for i in k_g ]
g1_sorted = sorted(g0_sorted, key= lambda x: (x[1], x[2]))
g2_sorted = [[i[0]] +map(str, i[1:3])+ map(str, [-1*j if j!=0 else j for j in map(math.log, map(float, i[3:]) )] ) for i in g1_sorted ]
g_fin = 'Marker,LG,cM,days,daysM,daysF,daysRes\n'+ ','.join([ ','.join(i)+'\n' for i in g2_sorted ]).replace('\n,','\n')


# In[193]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qvall_g.csv','w')
z.write(g_fin)
z.close()
z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qvall_aa.csv','w')
z.write(aa_fin)
z.close()


# In[181]:




# In[ ]:



