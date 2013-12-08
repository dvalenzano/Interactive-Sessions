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

Id = []
p0 = []
f1 = []
f2 = []
p0f1 = []
f1f2 = []
keys = []
for i in go1t[10:]:
    ID.append(i[0])
    p0.append(i[1]+i[2])
    f1.append(i[3]+i[4])
    p0f1.append(i[1]+i[2]+i[3]+i[4])
    f2.append(list(i[5:]))
    f1f2.append(list(i[3:]))
    keys.append(i[0]+','+i[1]+i[2]+','+i[3]+','+i[4])

# <codecell>

d = dict(zip(keys, f2))
df2 = dict(zip(ID, f2))
df1f2 = dict(zip(ID, f1f2))
df1 = dict(zip(ID, f1))

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

# <markdowncell>

# Now I need to consider the case where P0 are 'aaab' or 'abaa'

# <codecell>

P0_aaab = []
for i in keys:
    if i.split(',')[1] == 'aaab':
        P0_aaab.append(i)
        
P0_abaa = []
for i in keys:
    if i.split(',')[1] == 'abaa':
        P0_abaa.append(i)

# <markdowncell>

# Now I need to carefully take into account all the possible F1 scenarios

# <codecell>

p0aaab_f1aaaa = []
p0aaab_f1bbbb = []
p0aaab_f1aabb = []
p0aaab_f1bbaa = []
p0aaab_f1aaab = []
p0aaab_f1abaa = []
p0aaab_f1abab = []
p0aaab_f1abbb = []
p0aaab_f1bbab = []

for i in P0_aaab:
    if df1[i.split(',')[0]] == 'aaaa':
        p0aaab_f1aaaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbbb':
        p0aaab_f1bbbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aabb':
        p0aaab_f1aabb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbaa':
        p0aaab_f1bbaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aaab':
        p0aaab_f1aaab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abaa':
        p0aaab_f1abaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abab':
        p0aaab_f1abab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abbb':
        p0aaab_f1abbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbab':
        p0aaab_f1bbab.append(i.split(',')[0])
        
        
p0abaa_f1aaaa = []
p0abaa_f1bbbb = []
p0abaa_f1aabb = []
p0abaa_f1bbaa = []
p0abaa_f1aaab = []
p0abaa_f1abaa = []
p0abaa_f1abab = []
p0abaa_f1abbb = []
p0abaa_f1bbab = []

for i in P0_abaa:
    if df1[i.split(',')[0]] == 'aaaa':
        p0abaa_f1aaaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbbb':
        p0abaa_f1bbbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aabb':
        p0abaa_f1aabb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbaa':
        p0abaa_f1bbaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aaab':
        p0abaa_f1aaab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abaa':
        p0abaa_f1abaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abab':
        p0abaa_f1abab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abbb':
        p0abaa_f1abbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbab':
        p0abaa_f1bbab.append(i.split(',')[0])

# <codecell>

print (
 len(p0aaab_f1aaaa),
 len(p0aaab_f1bbbb),
 len(p0aaab_f1aabb),
 len(p0aaab_f1bbaa),
 len(p0aaab_f1aaab),
 len(p0aaab_f1abaa),
 len(p0aaab_f1abab),
 len(p0aaab_f1abbb),
 len(p0aaab_f1bbab),
 )

# <codecell>

print (
 len(p0abaa_f1aaaa),
 len(p0abaa_f1bbbb),
 len(p0abaa_f1aabb),
 len(p0abaa_f1bbaa),
 len(p0abaa_f1aaab),
 len(p0abaa_f1abaa),
 len(p0abaa_f1abab),
 len(p0abaa_f1abbb),
 len(p0abaa_f1bbab),
 )

# <codecell>


# <codecell>

odd_P0aaab = []
for i in P0_aaab:
    if 'bb' in df2[i]:
        odd_P0aaab.append(i)
        
odd_P0abaa = []
for i in P0_abaa:
    if 'bb' in df2[i]:
        odd_P0abaa.append(i)

# <codecell>

df1f2['25984']

# <codecell>

keys[:10]

# <codecell>


