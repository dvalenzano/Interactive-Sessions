
# coding: utf-8

# In[84]:

# Goal: to generate a fasta file for the linkage map built on cross G, and one for the linkage map built on cross AA

gfa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
aafa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()

glm = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read()
aalm = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read()


# In[85]:

glm = glm.replace('"','')
aalm = aalm.replace('"','')


# In[86]:

glm = [ i for i in glm.split('\n')[:-1] if i[0] != ',']
aalm = [ i for i in aalm.split('\n')[:-1] if i[0] != ',']

glm = sorted(glm, key=lambda x:(float(x.split(',')[1])))
aalm = sorted(aalm, key=lambda x:(float(x.split(',')[1])))


# In[87]:

kg = [i.split(',')[0] for i in glm]
vg = [','.join(i.split(',')[1:]) for i in glm]

kaa = [i.split(',')[0] for i in aalm]
vaa = [','.join(i.split(',')[1:]) for i in aalm]

dg = dict(zip(kg, vg))
daa = dict(zip(kaa,vaa))


# In[88]:

kfg = [i[1:] for i in gfa.split('\n')[:-1][:-1:2]]
vfg = gfa.split('\n')[:-1][1::2]
dfg = dict(zip(kfg, vfg))

kfaa = [i[1:] for i in aafa.split('\n')[:-1][:-1:2]]
vfaa = aafa.split('\n')[:-1][1::2]
dfaa = dict(zip(kfaa, vfaa))


# In[98]:

gz = ','.join([ '>'+i+'_LG'+dg[i]+'\n'+dfg[i]+'\n'   for i in kg ]).replace('\n,','\n')
aaz = ','.join([ '>'+i+'_LG'+daa[i]+'\n'+dfaa[i]+'\n'   for i in kaa ]).replace('\n,','\n')


# In[99]:

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/Go_cross.fa', 'w')
z.write(gz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/AAo_cross.fa', 'w')
z.write(aaz)
z.close()


# In[ ]:



