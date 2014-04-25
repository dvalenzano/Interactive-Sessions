# This script takes a list of linkage groups, then takes the survival QTL analyzed with plink and combines them in a new file
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

allm = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/mal/fam_8m_sqtl.assoc.linear', 'rU').read()
LGs = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/f8m_LGs.txt', 'rU').read()

# <codecell>

LGss = [ i for i in LGs.split('\n\n')]

mcm = [ [ i.split()[1:3] for i in LGss[j].split('\n') ] for j in range(len(LGss))]

keys = [ i.split()[1] for i in allm.split('\n')[1:-1]]
values = [ i.split()[-1] for i in allm.split('\n')[1:-1]]
d = dict(zip(keys, values))

# <codecell>

allLGs = [','.join([','.join(mcm[j][i]+[d[mcm[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm[j])) ]).replace('\n,','\n') for j in range(len(mcm)-1)]

# <codecell>


LG1 = allLGs[0]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG1', 'w')
z.write(LG1)

LG2 = allLGs[1]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG2', 'w')
z.write(LG2)

LG3 = allLGs[2]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG3', 'w')
z.write(LG3)

LG4 = allLGs[3]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG4', 'w')
z.write(LG4)

LG5 = allLGs[4]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG5', 'w')
z.write(LG5)

LG6 = allLGs[5]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG6', 'w')
z.write(LG6)

LG7 = allLGs[6]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG7', 'w')
z.write(LG7)

LG8 = allLGs[7]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG8', 'w')
z.write(LG8)

LG9 = allLGs[8]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG9', 'w')
z.write(LG9)

LG10 = allLGs[9]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG10', 'w')
z.write(LG10)

LG11 = allLGs[10]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG11', 'w')
z.write(LG11)

LG12 = allLGs[11]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG12', 'w')
z.write(LG12)

LG13 = allLGs[12]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG13', 'w')
z.write(LG13)

LG14 = allLGs[13]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG14', 'w')
z.write(LG14)

LG15 = allLGs[14]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG15', 'w')
z.write(LG15)

LG16 = allLGs[15]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG16', 'w')
z.write(LG16)

LG17 = allLGs[16]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG17', 'w')
z.write(LG17)

LG18 = allLGs[17]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG18', 'w')
z.write(LG18)

LG19 = allLGs[18]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG19', 'w')
z.write(LG19)

LG20 = allLGs[19]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG20', 'w')
z.write(LG20)

LG21 = allLGs[20]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG21', 'w')
z.write(LG21)

LG22 = allLGs[21]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG22', 'w')
z.write(LG22)

LG23 = allLGs[22]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG23', 'w')
z.write(LG23)

LG24 = allLGs[23]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG24', 'w')
z.write(LG24)

LG25 = allLGs[24]
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f8m/LG25', 'w')
z.write(LG25)

# <codecell>


