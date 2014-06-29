
# coding: utf-8

#### Goal: to generate a table with cumulative segnificance for each sQTL using classes

#### Date: 25.06.2014

# In[357]:

g = open('/Volumes/group_dv/personal/DValenzano/Jun2014/all_Ggroups.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jun2014/all_AAgroups.csv', 'rU').read()


# Now I need to get the p-values for each marker, group by group.

# In[358]:

#This is the old way to do it:
#pv_g7m = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/mal/fam_7m_sqtl_sig', 'rU').read()
#g7mk = [i.split()[1] for i in pv_g7m.split('\n')[1:-1]]
#g7mv = [i.split()[-1] for i in pv_g7m.split('\n')[1:-1]]
#g7md = dict(zip(g7mk, g7mv))


# In[359]:

g7min = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/mal/fam_7m_sqtl_sig'
g7fin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/fem/fam_7f_sqtl_sig'
g14min = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/mal/fam_14m_sqtl_sig'
g14fin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/fem/fam_14f_sqtl_sig'
g8min = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/mal/fam_8m_sqtl_sig'
g8fin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/fem/fam_8f_sqtl_sig'
g1_1min = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_1.1/mal/fam_1.1m_sqtl_sig'
g1_1fin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_1.1/fem/fam_1.1f_sqtl_sig'


# In[360]:

#class Makep3(object):
#    " generates a dictionary with marker as key and p-value as value"
#    def __init__(self, inp):
#        self.inp = inp
#        self.inpu = open(inp, 'rU').read()
#    def key(self):
#        return [i.split()[1] for i in self.inpu.split('\n')[1:-1]]
#    def value(self):
#        return [i.split()[-1] for i in self.inpu.split('\n')[1:-1]]
#    def d(self):
#        return dict(zip(self.key, self.value))


# In[361]:

# And this is the new way:
class Makep(object):
    " generates a dictionary with marker as key and p-value as value"
    def __init__(self, inp):
        self.inp = inp
        self.inpu = open(inp, 'rU').read()
        self.key = [i.split()[1] for i in self.inpu.split('\n')[1:-1]]
        self.value = [float(i.split()[-1]) for i in self.inpu.split('\n')[1:-1]]
        self.d = dict(zip(self.key, self.value))


# In[362]:

g7m = Makep(g7min)
g7f = Makep(g7fin)
g14m = Makep(g14min)
g14f = Makep(g14fin)
g8m = Makep(g8min)
g8f = Makep(g8fin)
g1_1m = Makep(g1_1min)
g1_1f = Makep(g1_1fin)


##### Here the list of columns that need to be excluded as they are relative to the epistatic interacting markers, and then the list of groups that need to be considered

# In[363]:

ems = [g.split('\n')[0].split(',').index(i) for i in g.split('\n')[0].split(',') if 'e' in i]


# In[364]:

','.join([g.split('\n')[0].split(',')[i] for i in range(15) if i not in ems])


##### reg is the new g matrix, with only the markers without epistatic interaction   reg2 is the same as reg, with the names of the groups with significant markers instead of the '1'

# reg = [[j.split(',')[i] for i in range(15) if i not in ems] for j in g.split('\n')[:-1] ]

# In[365]:

reg2 = [[reg[0][i][:-2] if j[i] == '1' else j[i]  for i in range(len(reg[0])) ] for j in reg[1:]]


# In[366]:

d2 = {'g7m':g7m.d,'g7f':g7f.d,'g14m':g14m.d,'g14f':g14f.d,'g8m':g8m.d,'g8f':g8f.d,'g1_1m':g1_1m.d,'g1_1f':g1_1f.d}


# In[367]:

pvalt = [reg[0]]+[ [j[0]] + [str(d2[j[i]][j[0]]) if j[i] != '0' else '-' for i in range(1, len(reg[0])) ] for j in reg2]
pvaltab = ','.join([ ','.join(i)+'\n' for i in pvalt]).replace('\n,','\n')


# In[368]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Ggroups_pvals.csv', 'w')
z.write(pvaltab)
z.close()


#### Now the same will apply to cross AA

# In[369]:

aa1min = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_1m_sqtl_sig'
aa1fin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_1f_sqtl_sig'
aa3min = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_3m_sqtl_sig'
aa3fin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_3f_sqtl_sig'


# In[370]:

aa1m = Makep(aa1min)
aa1f = Makep(aa1fin)
aa3m = Makep(aa3min)
aa3f = Makep(aa3fin)


# In[371]:

aaems = [aa.split('\n')[0].split(',').index(i) for i in aa.split('\n')[0].split(',') if 'e' in i]


# aareg is the new aa matrix, with only the markers without epistatic interaction  
# aareg2 is the same as aareg, with the names of the groups with significant markers instead of the '1'

# In[372]:

aareg = [[j.split(',')[i] for i in range(len(aa.split('\n')[0].split(','))) if i not in ems] for j in aa.split('\n')[:-1] ]
aareg2 = [[aareg[0][i][:-2] if j[i] == '1' else j[i]  for i in range(len(aareg[0])) ] for j in aareg[1:]]


# In[373]:

aareg2[:4]


# In[374]:

aad2 = {'aa1m':aa1m.d,'aa1f':aa1f.d,'aa3m':aa3m.d,'aa3f':aa3f.d}
aapvalt = [aareg[0]]+[ [j[0]] + [str(aad2[j[i]][j[0]]) if j[i] != '0' else '-' for i in range(1, len(aareg[0])) ] for j in aareg2]
aapvaltab = ','.join([ ','.join(i)+'\n' for i in aapvalt]).replace('\n,','\n')


# In[375]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AAgroups_pvals.csv', 'w')
z.write(aapvaltab)
z.close()


#### Addition of the composite pvalue

# I need to add a column with the number of degrees of freedom, and one for the Xsquared associated 

# In[376]:

ghead = pvaltab.split('\n')[0]+',df,Chisq\n'
aahead = aapvaltab.split('\n')[0]+',df,Chisq\n'


# In[377]:

import math
import numpy


# In[378]:

#chisq = -2*sum([math.log(float(i)) if i!= '-' else 0.0 for i in pvaltab.split('\n')[8].split(',')[1:]])


##### Here below I apply Fisher's method (of Fisher's combined probability test)

# In[379]:

def xsq(row):
    ls = []
    for i in row.split(',')[1:]:
        if i != '-':
            ls.append(math.log(float(i)))
        else:
            ls.append(0.0)
    return -2*sum(ls)

def df(row):
    return 2*(len(row.split(',')[1:]) - row.split(',')[1:].count('-'))
    
def wholetab(tab):    
#    return [tab.split('\n')[j]+','+str(df(tab.split('\n')[j]))+','+str(xsq(tab.split('\n')[j]))   for j in range(1,len(tab.split('\n')))]
    ls = [tab.split('\n')[j]+','+str(df(tab.split('\n')[j]))+','+str(xsq(tab.split('\n')[j]))   for j in range(1,len(tab.split('\n')))]
    return tab.split('\n')[0]+',df,Chisq\n'+','.join([i+'\n' for i in ls]).replace('\n,','\n')
    #return ls


# In[380]:

gtab = wholetab(pvaltab)


# In[381]:

aatab = wholetab(aapvaltab)


# In[382]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Ggroups_chisq.csv','w')
z.write(gtab)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AAgroups_chisq.csv','w')
z.write(aatab)
z.close()


# In[383]:

#def addChisq(inp):
#    ls = [i + ','+ str(chisqprob(float(i.split(',')[-1]), float(i.split(',')[-2]))) for i in gtab.split('\n')[1:-1]]
#    return inp.split('\n')[0]+',pval\n'+','.join([i+'\n' for i in ls]).replace('\n,','\n')


# In[384]:

def addChisq(inp):
    ls = [i + ','+ str(chisqprob(float(i.split(',')[-1]), float(i.split(',')[-2]))) for i in inp.split('\n')[1:-1]]
    return inp.split('\n')[0]+',pval\n'+','.join([i+'\n' for i in ls]).replace('\n,','\n')


# In[385]:

gX = addChisq(gtab)
aaX = addChisq(aatab)


# In[386]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_sqtl_chisqpval.csv','w')
z.write(gX)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AA_sqtl_chisqpval.csv','w')
z.write(aaX)
z.close()


# Now for cross G, I will also calculate the p values without considering fam1_1 females, which have surprisingly too many significant markers

# In[387]:

def xsq_2(row):
    ls = []
    for i in row.split(',')[1:-1]:
        if i != '-':
            ls.append(math.log(float(i)))
        else:
            ls.append(0.0)
    return -2*sum(ls)

def df_2(row):
    return 2*(len(row.split(',')[1:-1]) - row.split(',')[1:].count('-'))
    
def wholetab_2(tab):    
#    return [tab.split('\n')[j]+','+str(df(tab.split('\n')[j]))+','+str(xsq(tab.split('\n')[j]))   for j in range(1,len(tab.split('\n')))]
    ls = [tab.split('\n')[j]+','+str(df(tab.split('\n')[j]))+','+str(xsq(tab.split('\n')[j]))   for j in range(1,len(tab.split('\n')))]
    return ','.join(tab.split('\n')[0].split(',')[:-1])+',df,Chisq\n'+','.join([i+'\n' for i in ls]).replace('\n,','\n')
    #return ls
    
gtab_2 = wholetab_2(pvaltab)
g_2X = addChisq(gtab_2)


# In[388]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_sqtl_chisqpval_2.csv','w')
z.write(g_2X)
z.close()


# In[ ]:



