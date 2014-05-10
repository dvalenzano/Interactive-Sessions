
# coding: utf-8

# In[7]:

qtl0_Go = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/Go_lrt.csv', 'rU').read()
qtl0_AAo = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/AAo_lrt.csv', 'rU').read()

# <codecell>

qsGo = qtl0_Go.split('\n')
hLODGo = [ i  for i in qsGo[1:] if float(i.split('\t')[2])>15] #only picks markers that have LOD score higher than 20

qsAAo = qtl0_AAo.split('\n')
hLODAAo = [ i  for i in qsAAo[1:] if float(i.split('\t')[2])>15]

# <codecell>

qtlIDGo = [ i.split('\t')[0][:-1] for i in hLODGo ]
qtlIDAAo = [ i.split('\t')[0][:-1] for i in hLODAAo ]

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/Go_qtl1.csv', 'w')
z.write(','.join(qtlIDGo))
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/AAo_qtl1.csv', 'w')
z.write(','.join(qtlIDAAo))
z.close()


# Now follows the script to build the fasta files associated to these markers

# In[9]:

import re
fasta0 = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
markers = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/Go_qtl1.csv', 'rU').read()

# <codecell>

asp = markers.split(',')
asp2 = [ '>'+i+'\n'+'\w+'+'\n'  for i in asp]
ls = []
for i in asp2:
    ls.append(re.search(i, fasta0).group())
lsj = ','.join(ls).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/NfGo_sl.fa', 'w')
z.write(lsj)
z.close()


# In[11]:

fasta0 = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()
markers = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/AAo_qtl1.csv', 'rU').read()

# <codecell>

asp = markers.split(',')
asp2 = [ '>'+i+'\n'+'\w+'+'\n'  for i in asp]
ls = []
for i in asp2:
    ls.append(re.search(i, fasta0).group())
lsj = ','.join(ls).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/NfAAo_sl.fa', 'w')
z.write(lsj)
z.close()


# Now I need to check if these markers are in the sex-linked LGs

# In[44]:

slGo = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read().replace('"','')
slAAo = open('/Volumes/group_dv/personal/DValenzano/May2014/aao32014_swi_pos.csv', 'rU').read().replace('"','')

# In[27]:

slGom = ','.join([ i.split(',')[0]  for i in slGo.split('\n')[1:-1] if i.split(',')[1]=='3' ])
allGo = ','.join([ i.split(',')[0]  for i in slGo.split('\n')[1:-1]])

# In[28]:

slAAom = ','.join([ i.split(',')[0]  for i in slAAo.split('\n')[1:-1] if i.split(',')[1]=='3'])
allAAo = ','.join([ i.split(',')[0]  for i in slAAo.split('\n')[1:-1]])


# In[47]:

from sets import Set

allGo_s = Set(allGo.split(','))
allAAo_s = Set(allAAo.split(','))

slGom_s = Set(slGom.split(','))
slAAom_s = Set(slAAom.split(','))

qtlIDGo_s = Set(qtlIDGo)
qtlIDAAo_s = Set(qtlIDAAo)

print(
'Go lrt-sex markers also present in LG 3 are: ' + str(len(qtlIDGo_s & slGom_s)) +
'\nAAo lrt-sex markers also present in LG 3 are: ' + str(len(qtlIDAAo_s & slAAom_s)) +
'\nGo lrt-sex markers also present in LM are: ' + str(len(qtlIDGo_s & allGo_s)) +
'\nAAo lrt-sex markers also present in LM are: ' + str(len(qtlIDAAo_s & allAAo_s))
)


# BINGO!!!

# In[ ]:



