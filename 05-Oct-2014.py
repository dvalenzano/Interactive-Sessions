
# coding: utf-8

# In[1]:

# Goal: to extract the fasta of the significant sQTl for the peak QTL. 
# First, a safety mattress, in case it takes too long to get out the significant markers. 
g4 = open('/Volumes/group_dv/personal/DValenzano/Jul2014/g4_qtl.fa', 'rU').read()
g_LG3_sQTL = ','.join([g4.split('\n')[i]+'\n'+g4.split('\n')[i+1]+'\n'  for i in range(len(g4.split('\n')[:-1])) if g4.split('\n')[i][0] == '>' and  g4.split('\n')[i].split('_')[1] == 'rqtl' and g4.split('\n')[i].split('_')[2]=='3']).replace('\n,','\n')


# In[73]:

# From qqvall_g.csv I saved a smaller regio in linkage group 3, with the most significant markers
g_lg3_sig = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g_cross_LG3_sig.csv', 'rU').read()
sig_all = [i.split(',')[0] for i in g_lg3_sig.split('\n')[:-1] ]
sig_peak = [i.split(',')[0] for i in g_lg3_sig.split('\n')[6:13] ]


# In[76]:

gfa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
aafa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()


# In[87]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_g.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/qqvall_aa.csv', 'rU').read()

gLz_rqtl_k = [i.split(',')[0] for i in  g.split('\n')[1:-1]]
gLz_rqtl_v = ['_rqtl_'+i.split(',')[1][:-2]+'_'+i.split(',')[2] for i in  g.split('\n')[1:-1]]
gLz_rqtl_d = dict(zip(gLz_rqtl_k, gLz_rqtl_v))


# In[79]:

gfak = gfa.split('\n')[::2]
gfav = gfa.split('\n')[1::2]
gfad = dict(zip(gfak, gfav))


# In[92]:

gLz = sig_all
g_all_out = []
for i in gLz:
    if '>'+i in gfak:
        if i in gLz_rqtl_k:
            g_all_out.append('>'+i+gLz_rqtl_d[i]+'\n'+ gfad['>'+i]+'\n')
                
g_all_outz = ','.join(g_all_out).replace('\n,','\n')


# In[95]:

gLpz = sig_peak
g_peak_out = []
for i in gLpz:
    if '>'+i in gfak:
        if i in gLz_rqtl_k:
            g_peak_out.append('>'+i+gLz_rqtl_d[i]+'\n'+ gfad['>'+i]+'\n')

g_peak_outz = ','.join(g_peak_out).replace('\n,','\n')


# In[98]:

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g_lg3_all.fa', 'w')
z.write(g_all_outz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/g_lg3_peak.fa', 'w')
z.write(g_peak_outz)
z.close()


# In[99]:

# Now I will check whether the markers on LG3 which are significant for survival overlap with those that are significant in cross G
aa_lg3all = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aa_cross_LG3_sig.csv', 'rU').read()


# In[100]:

a_lg3m = [ i.split(',')[0] for i in  aa_lg3all.split('\n')[:-1] ]


# In[121]:

# Now I need to translate these markers to the equivalent G markers
aatog = open('/Volumes/group_dv/personal/DValenzano/Jun2014/aligGtoAA/AAo32014swi_mapped_to_Go32014.csv', 'rU').read()
aatog2 = open('/Volumes/group_dv/personal/DValenzano/Jun2014/aligGtoAA/Go32014_mapped_to_AAo32014swi.csv', 'rU').read()


# In[123]:

aatoglg3 = [i  for i in aatog.split('\n')[:-1] if i[:3]=='LG3' and '*' not in i]
aak = [i.split('_')[3].split(',')[0]  for i in aatoglg3 ]
aav = [i.split('_')[-1]  for i in aatoglg3 ]
aad = dict(zip(aak, aav))

aatoglg3_2 = [i  for i in aatog2.split('\n')[:-1] if i[:3]=='LG3' and '*' not in i]
aak_2 = [i.split('_')[3].split(',')[0]  for i in aatoglg3_2 ]
aav_2 = [i.split('_')[-1]  for i in aatoglg3_2 ]
aad_2 = dict(zip(aak_2, aav_2))


# In[125]:

from sets import Set
Set(sig_peak) & Set(aav_2)


# In[126]:

from sets import Set
Set(sig_all) & Set(aav_2)


# In[ ]:

#These markers are the markers on cross G in the peak region that map on cross AA - they are in a significant region 

