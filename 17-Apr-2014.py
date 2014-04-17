# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

allm = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/mal/fam_14m_sqtl.assoc.linear', 'rU').read()
LGs = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/f14m_LGs.dat', 'rU').read()

# <codecell>

LGss = [ i for i in LGs.split('\n\n')]

mcm = [ [ i.split()[1:3] for i in LGss[j].split('\n') ] for j in range(len(LGss))]

keys = [ i.split()[1] for i in allm.split('\n')[1:-1]]
values = [ i.split()[-1] for i in allm.split('\n')[1:-1]]
d = dict(zip(keys, values))

# <codecell>

range(len(mcm))

# <codecell>

#allLGs = [','.join([','.join(mcm[j][i]+[d[mcm[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm[j])) ])[:-1].replace('\n,','\n') for j in range(len(mcm))]
allLGs = [','.join([','.join(mcm[j][i]+[d[mcm[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm[j])) ]).replace('\n,','\n') for j in range(len(mcm))]

# In[77]:

LG1 = allLGs[0]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG1', 'w')
z.write(LG1)

LG2 = allLGs[1]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG2', 'w')
z.write(LG2)

LG3 = allLGs[2]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG3', 'w')
z.write(LG3)

LG4 = allLGs[3]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG4', 'w')
z.write(LG4)

LG5 = allLGs[4]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG5', 'w')
z.write(LG5)

LG6 = allLGs[5]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG6', 'w')
z.write(LG6)

LG7 = allLGs[6]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG7', 'w')
z.write(LG7)

LG8 = allLGs[7]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG8', 'w')
z.write(LG8)

LG9 = allLGs[8]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG9', 'w')
z.write(LG9)

LG10 = allLGs[9]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG10', 'w')
z.write(LG10)

LG11 = allLGs[10]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG11', 'w')
z.write(LG11)

LG12 = allLGs[11]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG12', 'w')
z.write(LG12)

LG13 = allLGs[12]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG13', 'w')
z.write(LG13)

LG14 = allLGs[13]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG14', 'w')
z.write(LG14)

LG15 = allLGs[14]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG15', 'w')
z.write(LG15)

LG16 = allLGs[15]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG16', 'w')
z.write(LG16)

LG17 = allLGs[16]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG17', 'w')
z.write(LG17)

LG18 = allLGs[17]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG18', 'w')
z.write(LG18)

LG19 = allLGs[18]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG19', 'w')
z.write(LG19)

LG20 = allLGs[19]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG20', 'w')
z.write(LG20)

LG21 = allLGs[20]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG21', 'w')
z.write(LG21)

LG22 = allLGs[21]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG22', 'w')
z.write(LG22)

LG22 = allLGs[21]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG22', 'w')
z.write(LG22)

# <codecell>


