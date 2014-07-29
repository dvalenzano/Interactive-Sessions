
# coding: utf-8

#### Goal: To extract a subset of significant markers from g and aa cross

# In[4]:

import numpy


# In[5]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_g.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_aa.csv', 'rU').read()


# In[6]:

g.split('\n')[0].split(',')


# In[77]:

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


# In[78]:

g_sig = getSig(g)
g1 = g_sig.lm(1)
g3 = g_sig.lm(3)[:7]
g6 = g_sig.lm(6)
g8 = g_sig.lm(8)[-4:]
g9 = g_sig.lm(9)[:6]
g14 = g_sig.lm(14)[5:-8]


# In[9]:

gL = g1+g3+g6+g8+g9+g14


# In[10]:

aa_sig = getSig(aa)
aa2 = aa_sig.lm(2)[3:]
aa5 = aa_sig.lm(5)[1:-2]
aa7 = aa_sig.lm(7)[3:]
aa13 = aa_sig.sel(13)[3:]


# In[11]:

aaL = aa2 + aa5 + aa7 + aa13


### Below the selection of the markers from the onemap 

# In[12]:

gom_7m = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g7m.csv', 'rU').read()
gom_14m = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g14m.csv', 'rU').read()
gom_8m = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g8m.csv', 'rU').read()
gom_7f = open('/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_g7f.csv', 'rU').read()


# In[161]:

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


# In[162]:

gom_7ms = om_sig(gom_7m)
gom_14ms = om_sig(gom_14m)
gom_8ms = om_sig(gom_8m)
gom_7fs = om_sig(gom_7f)


# In[16]:

gL2 = gom_7ms.lm(3)[10:-2]+gom_14ms.lm(3)[12:19]+gom_14ms.lm(5)+gom_8ms.lm(19)+gom_7fs.lm(1)[11:-5]


# In[17]:

from sets import Set
gL3 = list(Set(gL2))


# In[18]:

gLz = list(Set(gL)| Set(gL3)) #union of the two sets
aaLz = aaL


# In[21]:

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


# Now I need to export to fasta

# In[23]:

gfa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
aafa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()


# In[61]:

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


# In[62]:

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

# In[102]:

def chisq_rf(input):
    ls = []
    for i in input:
        ls.append(-2*sum([math.log(i) for i in map(float, i.split(',')[-4:])]))
    return ls


# Then I get the index of the most significant marker

# In[101]:

chisq_rf(g_sig.sel(1)).index(max(chisq_rf(g_sig.sel(1))))


# In[104]:

m_rf_1 = [i.split(',')[0] for i in g_sig.sel(1)] #this is the list of markers


# In[108]:

mg1_sig = m_rf_1[chisq_rf(g_sig.sel(1)).index(max(chisq_rf(g_sig.sel(1))))] #this is the most significant one


# Now the same for all the rest of the linkage groups

# In[139]:

mg1_sig_ind = chisq_rf(g_sig.sel(1)).index(max(chisq_rf(g_sig.sel(1))))
m_rf_1 = [i.split(',')[0] for i in g_sig.sel(1)] #this is the list of markers
mg1_sig = m_rf_1[mg1_sig_ind] #this is the most significant one
mg1_sig


# In[111]:

mg3_sig_ind = chisq_rf(g_sig.sel(3)[:7]).index(max(chisq_rf(g_sig.sel(3)[:7])))
m_rf_3 = [i.split(',')[0] for i in g_sig.sel(3)[:7]] #this is the list of markers
mg3_sig = m_rf_3[mg3_sig_ind] #this is the most significant one


# In[125]:

mg6_sig_ind = chisq_rf(g_sig.sel(6)).index(max(chisq_rf(g_sig.sel(6))))
m_rf_6 = [i.split(',')[0] for i in g_sig.sel(6)] #this is the list of markers
mg6_sig = m_rf_6[mg6_sig_ind] #this is the most significant one
mg6_sig


# In[127]:

mg8_sig_ind = chisq_rf(g_sig.sel(8)[-4:]).index(max(chisq_rf(g_sig.sel(8)[-4:])))
m_rf_8 = [i.split(',')[0] for i in g_sig.sel(8)[-4:]] #this is the list of markers
mg8_sig = m_rf_8[mg8_sig_ind] #this is the most significant one
mg8_sig


# In[129]:

mg9_sig_ind = chisq_rf(g_sig.sel(9)[:6]).index(max(chisq_rf(g_sig.sel(9)[:6])))
m_rf_9 = [i.split(',')[0] for i in g_sig.sel(9)[:6]] #this is the list of markers
mg9_sig = m_rf_9[mg9_sig_ind] #this is the most significant one
mg9_sig


# In[131]:

mg14_sig_ind = chisq_rf(g_sig.sel(14)[5:-8]).index(max(chisq_rf(g_sig.sel(14)[5:-8])))
m_rf_14 = [i.split(',')[0] for i in g_sig.sel(14)[5:-8]] #this is the list of markers
mg14_sig = m_rf_14[mg14_sig_ind] #this is the most significant one
mg14_sig


# In[141]:

rf_sig = [str(mg1_sig)+','+str(mg3_sig) +','+ str(mg6_sig)+','+str(mg8_sig)+','+str(mg9_sig)+','+str(mg14_sig)]
rf_sig


# These above are the most significant markers for cross G, random forest only.

# Now I need to do the same for the OneMap files and for the AA cross. 

# In[ ]:

#gom_7ms.sel(3)[10:-2]+gom_14ms.sel(3)[12:19]+gom_14ms.sel(5)+gom_8ms.sel(19)+gom_7fs.sel(1)[11:-5]


# In[163]:

def om_Sig(inp):
    head = [ i.split(',')[0] for i in inp ]
    ind = [float(i.split(',')[-2]) for i in inp ].index(min([float(i.split(',')[-2]) for i in inp ]))
    return head[ind]


# In[164]:

om_Sig(gom_14ms.sel(3)[12:19])


# In[160]:

dict = {}
dict['gom_7ms.sel(3)[10:-2]'] = gom_7ms.sel(3)[10:-2]
dict['gom_14ms.sel(3)[12:19]'] = gom_14ms.sel(3)[12:19]
dict['gom_14ms.sel(5)'] = gom_14ms.sel(5)
dict['gom_8ms.sel(19)'] = gom_8ms.sel(19)
dict['gom_7fs.sel(1)[11:-5]'] = gom_7fs.sel(1)[11:-5]


# In[165]:

om_siG = ['gom_7ms.sel(3)[10:-2]','gom_14ms.sel(3)[12:19]','gom_14ms.sel(5)','gom_8ms.sel(19)','gom_7fs.sel(1)[11:-5]']


# In[171]:

om_list = [om_Sig(dict[i]) for i in om_siG]
om_list


# Above are the most significant markers in the G-cross one-map analysis

# In[ ]:




# In[ ]:




# In[122]:

class most_sig(object): in progress
    
    """ this class returns the most significant marker in for each cluster of QTL in the random forest analysis, using the Fisher method for compound significance """  
    
    def __init__(self, group):
        self.group = group
        
    def chisq_rf(self, inp): #inp is the output of getSig.sel()
        self.inp = inp
        self.ls = []
        
        for i in self.inp:
            self.ls.append(-2*sum([math.log(i) for i in map(float, i.split(',')[-4:])]))
        return self.ls
            
#    def sig(self, lg):
#        self.sig_ind = 


# In[120]:




# In[121]:




# In[ ]:



