# This script allows to filter QTL by their p/q value and is an adaptation of the 30-Jul-2014.py script. 
# coding: utf-8

# In[9]:

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
        self.dp = numpy.percentile(map(float, self.gs[3][1:]), .9995)
        self.dMp = numpy.percentile(map(float, self.gs[4][1:]), .9995)
        self.dFp = numpy.percentile(map(float, self.gs[5][1:]), .9995)
        self.dSp = numpy.percentile(map(float, self.gs[6][1:]), .9995)
    
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
                if float(i.split(',')[-2]) < 0.00005:
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

z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/g_09995_qtl.fa', 'w')
z.write(goutz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/aa_09995_qtl.fa', 'w')
z.write(aaoutz)
z.close()


# In[ ]:



