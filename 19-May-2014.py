qtl0_pop = open('/Volumes/group_dv/group/data/sex_determination/sex-linked_rad-tags/rn,X1002J1xJ2,ADBELL,ck1005R_lrt.csv', 'rU').read()


# In[22]:

qspop = qtl0_pop.split('\n')
hLODpop = [ i  for i in qspop[1:] if float(i.split('\t')[2])>4] #only picks markers that have LOD score higher than 15

# hLODpop2 = [  i  for i in hLODpop if i.split('\t')[2] != '40']



# In[19]:

qtlIDpop = [ i.split('\t')[0][:-1].replace(' ','') for i in hLODpop ]


# <codecell>

z = open('/Volumes/group_dv/group/data/sex_determination/sex-linked_rad-tags/pop_slrt.csv', 'w')
z.write(','.join(qtlIDpop))
z.close()

