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
keys = []
for i in go1t[10:]:
    ID.append(i[0])
    p0.append(i[1]+i[2])
    f1.append(i[3]+i[4])
    p0f1.append(i[1]+i[2]+i[3]+i[4])
    f2.append(list(i[5:]))
    keys.append(i[0]+','+i[1]+i[2]+','+i[3]+','+i[4])

# <codecell>

d = dict(zip(keys, f2))

# <codecell>

P0_aabb = []
for i in keys:
    if i.split(',')[1] == 'aabb':
        P0_aabb.append(i)

# <codecell>

oddF1_aa = []
oddF1_bb = []
for i in P0_aabb:
    if i.split(',')[2] == 'aa':
        oddF1_aa.append(i)
    elif i.split(',')[3] == 'aa':
        oddF1_aa.append(i)
    elif i.split(',')[2] == 'bb':
        oddF1_bb.append(i)
    elif i.split(',')[3] == 'bb':
        oddF1_bb.append(i)

# <markdowncell>

# Now I need to find the markers where - in oddF1_bb - there are F2 with 'aa' genotypes, and in oddF1_aa, there are F2 with 'bb' genotypes. 

# <codecell>

odd_ID_aa = []
for i in oddF1_aa:
    if 'bb' in d[i]:
        odd_ID_aa.append(i.split(',')[0])

# <codecell>

odd_ID_bb = []
for i in oddF1_bb:
    if 'aa' in d[i]:
        odd_ID_bb.append(i.split(',')[0])

# <codecell>


