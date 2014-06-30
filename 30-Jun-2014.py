
# coding: utf-8

### Goal: to generate a table with markers, group, linkage group.position from /Volumes/group_dv/personal/DValenzano/Jun2014/all_Ggroups.csv

# In[4]:

all_aa = open('/Volumes/group_dv/personal/DValenzano/Jun2014/all_AAgroups.csv', 'rU').read()
all_g = open('/Volumes/group_dv/personal/DValenzano/Jun2014/all_Ggroups.csv', 'rU').read()
aarqtl_map = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read()
grqtl_map = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read()


# In[63]:

g7m_map = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/f7m_om-rqtl.csv', 'rU').read()
g7em_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m7e_sorted.csv', 'rU').read()
g7f_map = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7f/f7f_om-rqtl.csv', 'rU').read()
g7ef_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f7e_sorted.csv', 'rU').read()
g14m_map = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/f14m_om-rqtl.csv', 'rU').read()
g14em_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m14e_sorted.csv', 'rU').read()
g14f_map = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14f/f14f_om-rqtl.csv', 'rU').read()
g14ef_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f14e_sorted.csv', 'rU').read()
g8m_map = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/f8m_om-rqtl.csv', 'rU').read()
g8em_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m8e_sorted.csv', 'rU').read()
g8f_map = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8f/f8f_om-rqtl.csv', 'rU').read()
g8ef_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f8e_sorted.csv', 'rU').read()
g1_1m_map = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f1.1m/f1.1m_om-rqtl.csv', 'rU').read()
## and then AA cross
aa1m_map = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_om-rqtl.csv', 'rU').read()
aa1em_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m1e_sorted.csv', 'rU').read()
aa3m_map = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_om-rqtl.csv', 'rU').read()
aa3em_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m3e_sorted.csv', 'rU').read()
aa1f_map = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_om-rqtl.csv', 'rU').read()
aa1ef_map = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_f1e_sorted.csv', 'rU').read()


# For each map I need to create a dictionary with marker name as key, and LG.position as value

# In[40]:

class makeDict_rqtl:
    def __init__(self, inp):
        self.inp = inp
        self.k = [i.split(',')[0] for i in self.inp.replace('"','').split('\n')[1:-1]]
        self.v = [i.split(',')[1]+'_'+i.split(',')[2] for i in self.inp.replace('"','').split('\n')[1:-1]]
        self.d = dict(zip(self.k, self.v))


# In[43]:

aarqtl = makeDict_rqtl(aarqtl_map)
grqtl = makeDict_rqtl(grqtl_map)


# In[12]:

#g7mk = [i.split(',')[1] for i in g7m_map.split('\n')[1:-1]]
#g7mv = [i.split(',')[0]+'_'+i.split(',')[2] for i in g7m_map.split('\n')[1:-1]]
#g7md = dict(zip(g7mk, g7mv))


# In[64]:

class makeDict:
    def __init__(self, inp):
        self.inp = inp
        self.k = [i.split(',')[1] for i in self.inp.split('\n')[1:-1]]
        self.v = [i.split(',')[0]+'_'+i.split(',')[2] for i in self.inp.split('\n')[1:-1]]
        self.d = dict(zip(self.k, self.v))


# In[65]:

g7m = makeDict(g7m_map)
g7f = makeDict(g7f_map)
g14m = makeDict(g14m_map)
g14f = makeDict(g14f_map)
g8m = makeDict(g8m_map)
g8f = makeDict(g8f_map)
g1_1m = makeDict(g1_1m_map)
#
aa1m = makeDict(aao1m_map)
aa3m = makeDict(aao3m_map)
aa1f = makeDict(aao1f_map)


# In[66]:

aa1m = makeDict(aao1m_map)
aa3m = makeDict(aao3m_map)
aa1f = makeDict(aao1f_map)


# In[73]:

class makeDicte:
    def __init__(self, inp):
        self.inp = inp
        self.k = [i.split(',')[0] for i in self.inp.split('\n')[1:-1]] + [i.split(',')[5] for i in self.inp.split('\n')[1:-1]]
        self.v = [i.split(',')[1]+'_'+i.split(',')[2] for i in self.inp.split('\n')[1:-1]] + [i.split(',')[6]+'_'+i.split(',')[7] for i in self.inp.split('\n')[1:-1]]
        self.d = dict(zip(self.k, self.v))


# In[78]:

ge7m = makeDicte(g7em_map)
ge7f = makeDicte(g7ef_map)
ge14m = makeDicte(g14em_map)
ge14f = makeDicte(g14ef_map)
ge8m = makeDicte(g8em_map)
ge8f = makeDicte(g8ef_map)
aae1m = makeDicte(aa1em_map)
aae3m = makeDicte(aa3em_map)
aae1f = makeDicte(aa1ef_map)


# In[266]:

all_g2 = all_g.replace('_l', '')
all_aa2 = all_aa.replace('_l','')


# In[267]:

gems = [all_g2.split('\n')[0].split(',').index(i) for i in all_g2.split('\n')[0].split(',') if i == 'g1_1f']
aaems = [all_g2.split('\n')[0].split(',').index(i) for i in all_aa2.split('\n')[0].split(',') if i == 'g1_1f']


# In[271]:

reg = [[j.split(',')[i] for i in range(len(all_g2.split('\n')[0].split(','))) if i not in gems] for j in all_g2.split('\n')[:-1] ]
reaa = [[j.split(',')[i] for i in range(len(all_aa2.split('\n')[0].split(',')))] for j in all_aa2.split('\n')[:-1] ]


# In[279]:

gd0 = {'g7m':g7m.d, 'ge7m':ge7m.d, 'g7f':g7f.d, 'ge7f':ge7f.d, 'g14m':g14m.d, 'ge14m':ge14m.d, 'g14f':g14f.d, 'ge14f':ge14f.d, 'g8m':g8m.d, 'ge8m':ge8m.d, 'g8f':g8f.d, 'ge8f':ge8f.d, 'g1_1m':g1_1m.d}
aad0 = {'aa1m':aa1m.d, 'aae1m':aae1m.d, 'aa3m':aa3m.d, 'aae3m':aae3m.d, 'aa1f':aa1f.d, 'aae1f':aae1f.d}


# In[274]:

reg2 = [[reg[0][i] if j[i] == '1' else j[i]  for i in range(len(reg[0])) ] for j in reg[1:]]
reaa2 = [[reaa[0][i] if j[i] == '1' else j[i]  for i in range(len(reaa[0])) ] for j in reaa[1:]]


# In[262]:

lgt = []
for j in reg2:
    ls = []
    for i in j[1:]:
        if i != '0':
            if j[0] in gd0[i].keys():
                ls.append(gd0[i][j[0]])
            else:
                ls.append('-')
        else:
            ls.append('-')
    lgt.append(','.join([j[0]] + ls)+'\n')


# In[289]:

lgtj = ','.join(reg[0])+'\n'+','.join(lgt).replace('\n,','\n')


# In[280]:

laat = []
for j in reaa2:
    ls = []
    for i in j[1:]:
        if i != '0':
            if j[0] in aad0[i].keys():
                ls.append(aad0[i][j[0]])
            else:
                ls.append('-')
        else:
            ls.append('-')
    laat.append(','.join([j[0]] + ls)+'\n')


# In[290]:

laatj = ','.join(reaa[0])+'\n'+','.join(laat).replace('\n,','\n')


# In[291]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_qtl_0.csv', 'w')
z.write(lgtj)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AA_qtl_0.csv', 'w')
z.write(laatj)
z.close()


# Now I need to add the values for rqtl

# In[316]:

g_fin =lgtj.split('\n')[0]+',rqtl\n'+ ','.join([ i+ ','+grqtl.d[i.split(',')[0]] +'\n' if i.split(',')[0] in grqtl.k else i+ ',-\n' for i in lgtj.split('\n')[1:-1] ]).replace('\n,','\n')


# In[318]:

aa_fin =laatj.split('\n')[0]+',rqtl\n'+ ','.join([ i+ ','+aarqtl.d[i.split(',')[0]] +'\n' if i.split(',')[0] in aarqtl.k else i+ ',-\n' for i in laatj.split('\n')[1:-1] ]).replace('\n,','\n')


# In[319]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_qtl_1.csv', 'w')
z.write(g_fin)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AA_qtl_1.csv', 'w')
z.write(aa_fin)
z.close()


# In[ ]:



