
# coding: utf-8

# In[23]:

slGo = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read().replace('"','')
slAAo = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read().replace('"','')


# In[27]:

slGom = ','.join([ i.split(',')[0]  for i in slGo.split('\n')[1:-1] if i.split(',')[1]=='3' ])


# In[28]:

slAAom = ','.join([ i.split(',')[0]  for i in slAAo.split('\n')[1:-1] if i.split(',')[1]=='3'])


# In[33]:

faGo = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
faAAo = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()


# AAo cross first:

# In[36]:

import re
asp = slAAom.split(',')
asp2 = [ '>'+i+'\n'+'\w+'+'\n'  for i in asp]
ls = []
for i in asp2:
    ls.append(re.search(i, faAAo).group())
lsj = ','.join(ls).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/AAo_sl.fa', 'w')
z.write(lsj)
z.close()


# In[37]:

import re
asp = slGom.split(',')
asp2 = [ '>'+i+'\n'+'\w+'+'\n'  for i in asp]
ls = []
for i in asp2:
    ls.append(re.search(i, faGo).group())
lsj = ','.join(ls).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/Go_sl.fa', 'w')
z.write(lsj)
z.close()


# In[ ]:



