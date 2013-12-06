# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: to filter for mis-coded F1/F2 genotypes, derived from situations like the following:
# 
# P0: aaxbb
# F1: *bb*
# F2: *aa*
# 
# P0: aaxbb
# F1: *aa*
# F2: *bb*
# 
# P0: aaxab
# F1: aaxab
# F2: *bb*
# 
# P0: aaxab
# F1: *bb*
# F2: *aa* 

# <codecell>

go1 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inf_fam_Go/inf_fam_1.csv', 'rU').read()

# <codecell>

go1t = zip(*[ i.split(',')  for i in go1.split('\n')[:-1]])

# <codecell>

ID = []
p0 = []
f1 = []
f2 = []
p0f1 = []
for i in go1t[10:]:
    ID.append(i[0])
    p0.append(i[1]+i[2])
    f1.append(i[3]+i[4])
    p0f1.append(i[1]+i[2]+i[3]+i[4])
    f2.append(list(i[5:]))

# <codecell>

p0f1[:10]

# <codecell>


