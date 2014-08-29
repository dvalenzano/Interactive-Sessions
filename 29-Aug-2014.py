

# coding: utf-8

#### In the first part, I will get the values of max-lifespan for GRZ, MZM-0703 and Soveia

# In[41]:

gsurv = open('/Volumes/group_dv/personal/DValenzano/Aug2014/G_cross_surv.txt', 'rU').read()
aasurv = open('/Volumes/group_dv/personal/DValenzano/Aug2014/AA_cross_surv.txt', 'rU').read()


# In[15]:

SL = [float(i.split('\t')[0].replace(',','.')) for i in gsurv.split('\n') if i.split('\t')[-1]=='1'] + [float(i.split('\t')[0].replace(',','.')) for i in aasurv.split('\n')[1:-2] if i.split('\t')[-2]=='1']


# In[18]:

import math
import numpy as np
np.percentile(SL, 90)


# 21 weeks is the max lifespan for the Short-lived fish in both cross AA and G

# In[22]:

float((21.0*7.0)/365.0) #translated in years


# In[23]:

#Here follows the measure of max-lifespan for the long-lived strains independently in both crosses


# In[29]:

gsurv.split('\n')[-2]


# In[30]:

GLL = [float(i.split('\t')[0].replace(',','.')) for i in gsurv.split('\n')[:-1] if i.split('\t')[-2]=='1']
AALL = [float(i.split('\t')[0].replace(',','.')) for i in aasurv.split('\n')[:-2] if i.split('\t')[-1]=='1']


# In[40]:

print (
'max-lifespan for MZM-0703 strain is: ' + str(np.percentile(GLL, 90) )+' weeks or ' + str(float(7.0*np.percentile(GLL, 90)/365))+' years'
'\nmax-lifespan for Soveia strain is: ' + str(np.percentile(AALL, 90) )+' weeks or ' + str(float(7.0*np.percentile(AALL, 90)/365))+' years'
)


# In[ ]:

Here, I will sort G_qtl_1.csv by g7m


# In[44]:

aaqtl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AA_qtl_1.csv', 'rU').read()
gqtl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_qtl_1.csv', 'rU').read()


# In[72]:

class sortColumn(object):
    def __init__(self, inp, col):
        self.inp = [i.split(',') for i in inp.replace('-','0_0').split('\n')[:-1]]
        self.col = self.inp[0].index(col)
        self.srt = sorted(self.inp[1:], key=lambda row: (int(row[self.col].split('_')[0]), float(row[self.col].split('_')[1])))
        self.tosave = (','.join(self.inp[0])+'\n'+','.join([','.join(i)+'\n' for i in self.srt ])).replace('\n,','\n').replace('0_0','-')


# In[15]:

#prova = sorted([i.split(',') for i in aaqtl.replace('-','0_0').split('\n')[1:-1]], key=lambda row: (int(row[-1].split('_')[0]), float(row[-1].split('_')[1])))


# In[73]:

#aaq_rqtl = sortColumn(aaqtl, 'rqtl')
gq_g7m = sortColumn(gqtl, 'g7m')
gq_g14m = sortColumn(gqtl, 'g14m')

#z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aarqtl.csv', 'w')
#z.write(aaq_rqtl.tosave)
#z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/g7m.csv', 'w')
z.write(gq_g7m.tosave)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/g14m.csv', 'w')
z.write(gq_g14m.tosave)
z.close()


# In[65]:

grqtl_top = '4981,21654,22839,42490,18256,8227,12365,25691, 50773, 22598, 39113, 45030, 47481, 19200, 36373, 32893, 29875, 20068, 46159, 44832, 50653, 25035, 6098, 53870, 23538' 
g7m_top = '46159, 48952, 20068, 44832, 29875, 6098, 53870, 23538'
g14m_top = '39113, 45030, 47481, 19200, 29875, 20068, 36373'
from sets import Set
g_top = list(Set(grqtl_top.replace(' ', '').split(',')+g7m_top.replace(' ','').split(',')+g14m_top.replace(' ','').split(',')))
#g_top is the merged list of markers around the significant g7m, which is around marker 29875


# In[50]:

# Now I need to generate a fasta file from these markers
gfa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()


# In[66]:

gfak = gfa.split('\n')[::2]
gfav = gfa.split('\n')[1::2]
gfad = dict(zip(gfak, gfav))


# In[71]:

gout = []
for i in g_top:
    if '>'+i in gfak:
        gout.append('>'+i+'\n'+gfad['>'+i]+'\n')
            
goutz = ','.join(gout).replace('\n,','\n')


# In[75]:

#['>'+i in gfak for i in g_top ]
z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/Top_qtl.fa', 'w')
z.write(goutz)
z.close()


# In[76]:

#['>'+i in gfak for i in g_top ]


# In[ ]:



