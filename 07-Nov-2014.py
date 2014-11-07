# Goal: to save the peak files for AA cross in a fasta file in LG3

aafa = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()
peak_lg3 = ['33911', '8423', '19589', '39073', '25587', '44971', '8178', '4179', 
         '32767', '26568', '26780', '2663', '36581', '12275', '34490', '39114', 
         '10884', '2093', '6074', '18588', '32724', '32599']


# In[3]:

kfaa = [i[1:] for i in aafa.split('\n')[:-1][:-1:2]]
vfaa = aafa.split('\n')[:-1][1::2]
dfaa = dict(zip(kfaa, vfaa))


# In[8]:

aalm = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read()
aalm = aalm.replace('"','')


# In[13]:

kaa = [i.split(',')[0] for i in aalm.split('\n')[1:-1]]
vaa = [','.join(i.split(',')[1:]) for i in aalm.split('\n')[1:-1]]
daa = dict(zip(kaa,vaa))


# In[15]:

aaz = ','.join([ '>'+i+'_LG'+daa[i]+'\n'+dfaa[i]+'\n'   for i in peak_lg3 ]).replace('\n,','\n')


# In[18]:

z = open('/Volumes/group_dv/personal/DValenzano/Nov2014/AA-cross/peak_lg3.fa', 'w')
z.write(aaz)
z.close()


# In[ ]:



