
# coding: utf-8

# In[1]:

import numpy


# In[2]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_g.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_aa.csv', 'rU').read()
g.split('\n')[0].split(',')


# In[3]:

class getSig(object):

    def __init__(self, cross):
        self.cross = cross
        self.gs = [list(i) for i in zip(*[ j.split(',') for j in self.cross.split('\n')[:-1]])]
        self.dp = numpy.percentile(map(float, self.gs[3][1:]), .99)
        self.dMp = numpy.percentile(map(float, self.gs[4][1:]), .99)
        self.dFp = numpy.percentile(map(float, self.gs[5][1:]), .99)
        self.dSp = numpy.percentile(map(float, self.gs[6][1:]), .99)
    
    def sel(self, lg):  
        self.ls = []
        self.lg = str(lg)+'.0'
        for i in self.cross.split('\n')[1:-1]:
            if i.split(',')[1] == self.lg:
                if float(i.split(',')[3]) < self.dp:
                    self.ls.append(i)
                else:
                    if float(i.split(',')[4]) < self.dMp:
                        self.ls.append(i)
                    else:
                        if float(i.split(',')[5])< self.dFp:
                            self.ls.append(i)
                        else:
                            if float(i.split(',')[6]) < self.dSp:
                                self.ls.append(i)
        return self.ls
        
    def lm(self, lg):
        return [i.split(',')[0] for i in getSig.sel(self, lg)] #this extracts just the markers


# In[4]:

g_sig = getSig(g)
g1 = g_sig.lm(1)
g3 = g_sig.lm(3)[:7]
g6 = g_sig.lm(6)
g8 = g_sig.lm(8)[-4:]
g9 = g_sig.lm(9)[:6]
g14 = g_sig.lm(14)[5:-8]


# In[5]:

gL = g1+g3+g6+g8+g9+g14


# In[6]:

aa_sig = getSig(aa)
aa2 = aa_sig.lm(2)[3:]
aa5 = aa_sig.lm(5)[1:-2]
aa7 = aa_sig.lm(7)[3:]
aa13 = aa_sig.sel(13)[3:]

aaL = aa2 + aa5 + aa7 + aa13


### Below the selection of the markers from the onemap 

# In[7]:

gom_7m = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g7m.csv', 'rU').read()
gom_14m = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g14m.csv', 'rU').read()
gom_8m = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g8m.csv', 'rU').read()
gom_7f = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g7f.csv', 'rU').read()


# In[8]:

class om_sig(object):
    
    def __init__(self, group):
        self.group = group
        
    def sel(self, lg):
        self.lg = str(lg)
        self.ls = []
        for i in self.group.split('\n')[1:-1]:
            if i.split(',')[1] == self.lg:
                if float(i.split(',')[-2]) < 0.001:
                    self.ls.append(i)
        return self.ls
    
    def lm(self, lg):
        return [i.split(',')[0] for i in om_sig.sel(self, lg)] #this extracts just the markers


# In[9]:

gom_7ms = om_sig(gom_7m)
gom_14ms = om_sig(gom_14m)
gom_8ms = om_sig(gom_8m)
gom_7fs = om_sig(gom_7f)


# In[10]:

gL2 = gom_7ms.lm(3)[10:-2]+gom_14ms.lm(3)[12:19]+gom_14ms.lm(5)+gom_8ms.lm(19)+gom_7fs.lm(1)[11:-5]


# In[11]:

from sets import Set
gL3 = list(Set(gL2))

gLz = list(Set(gL)| Set(gL3)) #union of the two sets
aaLz = aaL


# In[13]:

gLz_rqtl_k = [i.split(',')[0] for i in  g.split('\n')[1:-1]]
gLz_rqtl_v = ['_rqtl_'+i.split(',')[1][:-2]+'_'+i.split(',')[2] for i in  g.split('\n')[1:-1]]
gLz_rqtl_d = dict(zip(gLz_rqtl_k, gLz_rqtl_v)) 

aaLz_rqtl_k = [i.split(',')[0] for i in  aa.split('\n')[1:-1]]
aaLz_rqtl_v = ['_rqtl_'+i.split(',')[1][:-2]+'_'+i.split(',')[2] for i in  aa.split('\n')[1:-1]]
aaLz_rqtl_d = dict(zip(aaLz_rqtl_k, aaLz_rqtl_v)) 

gom7m_k = [i.split(',')[0] for i in  gom_7m.split('\n')[1:-1]]
gom7m_v = ['_om7m_'+i.split(',')[1]+'_'+i.split(',')[2] for i in  gom_7m.split('\n')[1:-1]]
gom7m_d = dict(zip(gom7m_k, gom7m_v)) 

gom14m_k = [i.split(',')[0] for i in  gom_14m.split('\n')[1:-1]]
gom14m_v = ['_om14m_'+i.split(',')[1]+'_'+i.split(',')[2] for i in  gom_14m.split('\n')[1:-1]]
gom14m_d = dict(zip(gom14m_k, gom14m_v)) 

gom8m_k = [i.split(',')[0] for i in  gom_8m.split('\n')[1:-1]]
gom8m_v = ['_om8m_'+i.split(',')[1]+'_'+i.split(',')[2] for i in  gom_8m.split('\n')[1:-1]]
gom8m_d = dict(zip(gom8m_k, gom8m_v)) 

gom7f_k = [i.split(',')[0] for i in  gom_7f.split('\n')[1:-1]]
gom7f_v = ['_om7f_'+i.split(',')[1]+'_'+i.split(',')[2] for i in  gom_7f.split('\n')[1:-1]]
gom7f_d = dict(zip(gom7f_k, gom7f_v)) 


#### Now I need to export to fasta

# In[14]:

gfa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
aafa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()


# In[15]:

gfak = gfa.split('\n')[::2]
gfav = gfa.split('\n')[1::2]
gfad = dict(zip(gfak, gfav))

aafak = aafa.split('\n')[::2]
aafav = aafa.split('\n')[1::2]
aafad = dict(zip(aafak, aafav))

gout = []

for i in gLz:
    
    if i in gL:
        if '>'+i in gfak:
            if i in gLz_rqtl_k:
                gout.append('>'+i+gLz_rqtl_d[i]+'\n'+ gfad['>'+i]+'\n')
    
    else:
                    
        if i in gom_7ms.lm(3)[10:-2]:
            if i in gom7m_k:
                gout.append('>'+i+gom7m_d[i]+'\n'+ gfad['>'+i]+'\n')

        elif i in gom_14ms.lm(3)[12:19]:
            if i in gom14m_k:
                gout.append('>'+i+gom14m_d[i]+'\n'+ gfad['>'+i]+'\n')

        elif i in gom_14ms.lm(5):
            if i in gom14m_k:
                gout.append('>'+i+gom14m_d[i]+'\n'+ gfad['>'+i]+'\n')

        elif i in gom_8ms.lm(19):
            if i in gom8m_k:
                gout.append('>'+i+gom8m_d[i]+'\n'+ gfad['>'+i]+'\n')

        elif i in gom_7fs.lm(1)[11:-5]:
            if i in gom7f_k:
                gout.append('>'+i+gom7f_d[i]+'\n'+ gfad['>'+i]+'\n')
            
aaout = []
for i in aaLz:
    if '>'+i in aafak:
        if i in aaLz_rqtl_k:
            aaout.append('>'+i+aaLz_rqtl_d[i]+'\n'+ aafad['>'+i]+'\n')
            
goutz = ','.join(gout).replace('\n,','\n')
aaoutz = ','.join(aaout).replace('\n,','\n')


# In[16]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/g4_qtl.fa', 'w')
z.write(goutz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aa4_qtl.fa', 'w')
z.write(aaoutz)
z.close()


# g4_qtl.fa and aa4_qtl.fa contain a more complete version of markers, from rf and om - the markers header are now   
# consistent with the ppt figure /Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/RF_sQTL.pptx

# Now, from each peak in /Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/RF_sQTL.pptx  
# I got to get the most significant marker and re-derive a fasta file for both aa and g crosses
# 
# I need to combine the q-values with the Fisher test

# In[19]:

import math
def chisq_rf(input):
    ls = []
    for i in input:
        ls.append(-2*sum([math.log(i) for i in map(float, i.split(',')[-4:])]))
    return ls


# Then I get the index of the most significant marker

# In[20]:

chisq_rf(g_sig.sel(1)).index(max(chisq_rf(g_sig.sel(1))))


# In[21]:

m_rf_1 = [i.split(',')[0] for i in g_sig.sel(1)] #this is the list of markers


# In[22]:

mg1_sig = m_rf_1[chisq_rf(g_sig.sel(1)).index(max(chisq_rf(g_sig.sel(1))))] #this is the most significant one


# Now the same for all the rest of the linkage groups - I can write a function that does the job:

# In[23]:

def rf_Sig(inp):
    head = [ i.split(',')[0] for i in inp ] 
    ind = chisq_rf(inp).index(max(chisq_rf(inp)))
    return head[ind]


# In[24]:

mg1_sig = rf_Sig(g_sig.sel(1))
mg1_sig


# In[25]:

mg3_sig = rf_Sig(g_sig.sel(3)[:7])
mg3_sig


# In[26]:

mg6_sig = rf_Sig(g_sig.sel(6))
mg6_sig


# In[27]:

mg8_sig = rf_Sig(g_sig.sel(8)[-4:])
mg8_sig


# In[28]:

mg9_sig = rf_Sig(g_sig.sel(9)[:6])
mg9_sig


# In[29]:

mg14_sig = rf_Sig(g_sig.sel(14)[5:-8])
mg14_sig


# In[30]:

g_rf_sig = str(mg1_sig)+','+str(mg3_sig) +','+ str(mg6_sig)+','+str(mg8_sig)+','+str(mg9_sig)+','+str(mg14_sig)
g_rf_sig


# These above are the most significant markers for cross G, random forest only.

#### Now I need to do the same for the OneMap files and for the AA cross. 

# In[31]:

#gom_7ms.sel(3)[10:-2]+gom_14ms.sel(3)[12:19]+gom_14ms.sel(5)+gom_8ms.sel(19)+gom_7fs.sel(1)[11:-5]
def om_Sig(inp):
    head = [ i.split(',')[0] for i in inp ]
    ind = [float(i.split(',')[-2]) for i in inp ].index(min([float(i.split(',')[-2]) for i in inp ]))
    return head[ind]


# In[32]:

om_Sig(gom_14ms.sel(3)[12:19])


# In[33]:

dic = {}
dic['gom_7ms.sel(3)[10:-2]'] = gom_7ms.sel(3)[10:-2]
dic['gom_14ms.sel(3)[12:19]'] = gom_14ms.sel(3)[12:19]
dic['gom_14ms.sel(5)'] = gom_14ms.sel(5)
dic['gom_8ms.sel(19)'] = gom_8ms.sel(19)
dic['gom_7fs.sel(1)[11:-5]'] = gom_7fs.sel(1)[11:-5]


# In[34]:

gom_8ms.sel(19)


# In[41]:

g_om_siG = ['gom_7ms.sel(3)[10:-2]','gom_14ms.sel(3)[12:19]','gom_14ms.sel(5)','gom_8ms.sel(19)','gom_7fs.sel(1)[11:-5]']


# In[44]:

g_om_list0 = [om_Sig(dic[i]) for i in g_om_siG]
g_om_list0


#### marker '29875' is the top scoring marker in two analyses: gom_7ms.sel(3) and gom_14ms.sel(5)

# In[45]:

g_om_list = g_om_list0[:2]+g_om_list0[3:]
g_om_list


# Above are the most significant markers in the G-cross one-map analysis  
# Below, the complete list of g most-significant markers

# In[46]:

G_top = g_rf_sig.split(',') + g_om_list
G_top


# Finally, I have to compile a new fasta file with the new list of top markers

# In[47]:

G_top_out = []

for i in g_rf_sig.split(','):
    
    if i in gL:
        if '>'+i in gfak:
            if i in gLz_rqtl_k:
                G_top_out.append('>'+i+gLz_rqtl_d[i]+'\n'+ gfad['>'+i]+'\n')

for i in g_om_list:
                    
    if i in gom_7ms.lm(3)[10:-2]:
        if i in gom7m_k:
            G_top_out.append('>'+i+gom7m_d[i]+'\n'+ gfad['>'+i]+'\n')

    elif i in gom_14ms.lm(3)[12:19]:
        if i in gom14m_k:
            G_top_out.append('>'+i+gom14m_d[i]+'\n'+ gfad['>'+i]+'\n')

    elif i in gom_14ms.lm(5):
        if i in gom14m_k:
            G_top_out.append('>'+i+gom14m_d[i]+'\n'+ gfad['>'+i]+'\n')

    elif i in gom_8ms.lm(19):
        if i in gom8m_k:
            G_top_out.append('>'+i+gom8m_d[i]+'\n'+ gfad['>'+i]+'\n')

    elif i in gom_7fs.lm(1)[11:-5]:
        if i in gom7f_k:
            G_top_out.append('>'+i+gom7f_d[i]+'\n'+ gfad['>'+i]+'\n')

G_topz = ','.join(G_top_out).replace('\n,','\n') 


# Now, I need to get all the most significant markers for AA cross

# In[48]:

maa2_sig = rf_Sig(aa_sig.sel(2)[3:])
maa2_sig


# In[49]:

maa5_sig = rf_Sig(aa_sig.sel(5)[1:-2])
maa5_sig


# In[50]:

maa7_sig = rf_Sig(aa_sig.sel(7)[3:])
maa7_sig


# In[51]:

maa13_sig = rf_Sig(aa_sig.sel(13)[3:])
maa13_sig


# In[52]:

aa_rf_sig = maa2_sig+','+maa5_sig+','+maa7_sig+','+maa13_sig
AA_top = aa_rf_sig.split(',')
AA_top


# In[53]:

AA_top_out = []

for i in aa_rf_sig.split(','):
    
    if '>'+i in aafak:
        if i in aaLz_rqtl_k:
            AA_top_out.append('>'+i+aaLz_rqtl_d[i]+'\n'+ aafad['>'+i]+'\n')

AA_topz = ','.join(AA_top_out).replace('\n,','\n') 


# In[54]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/top_g_qtl.fa', 'w')
z.write(G_topz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/top_aa_qtl.fa', 'w')
z.write(AA_topz)
z.close()


# In[ ]:



