
# coding: utf-8

#### Goal: to save a list of significant markers and translate it into a fasta file

# In[23]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/g_rqtl_thr.csv', 'rU').read()
gfa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()

aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aa_rqtl_thr.csv', 'rU').read()
aafa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()


# In[24]:

gmarkers = [i.split(',')[0] for i in g.split('\n')[1:-1] if sum(map(float, i.split(',')[-4:])) < 4]
aamarkers = [i.split(',')[0] for i in aa.split('\n')[1:-1] if sum(map(float, i.split(',')[-4:])) < 4]


# In[42]:

gv = ['_rqtl_'+ i.split(',')[14] for i in g.split('\n')[1:-1] if sum(map(float, i.split(',')[-4:])) < 4 ]
gd = dict(zip(gmarkers, gv))

aav = ['_rqtl_'+ i.split(',')[7] for i in aa.split('\n')[1:-1] if sum(map(float, i.split(',')[-4:])) < 4 ]
aad = dict(zip(aamarkers, aav))


# In[25]:

gfak = gfa.split('\n')[::2]
gfav = gfa.split('\n')[1::2]
gfad = dict(zip(gfak, gfav))

aafak = aafa.split('\n')[::2]
aafav = aafa.split('\n')[1::2]
aafad = dict(zip(aafak, aafav))


# In[43]:

gout = ','.join([ '>'+i+gd[i]+'\n'+ gfad['>'+i]+'\n' for i in gmarkers if '>'+i in gfak ]).replace('\n,','\n')
aaout = ','.join([ '>'+i+aad[i]+'\n'+ aafad['>'+i]+'\n' for i in aamarkers if '>'+i in aafak ]).replace('\n,','\n')


# In[48]:

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/g_qtl.fa', 'w')
z.write(gout)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aa_qtl.fa', 'w')
z.write(aaout)
z.close()


# In[ ]:



