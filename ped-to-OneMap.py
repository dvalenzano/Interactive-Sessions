# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

f7 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/inferrednew_fam_7.csv', 'rU').read()

# <codecell>

f7s = zip(*[ i.split(',') for i in f7.split('\n')[:-1]])

# <markdowncell>

# What I want is marker ID, F1 genotypes, F2 genotypes

# <codecell>

#ls = []
#for i in f7t[10:]:
#    ls.append([i[0]]+[i[3]+'-'+i[4]]+list(i[5:]))

# <codecell>

#lz = []
#for i in ls:
#    lz.append(','.join(i)+'\n')

# <codecell>

#lz2 = ','.join(lz).replace('\n,','\n')

# <codecell>

#d = {}
#d['ab-ab'] = 'B2.6'
#d['aa-ab'] = 'D2.15'
#d['ab-aa'] = 'D1.10'

# <codecell>

#lz3 = [ i.split(',')[0]+','+d[i.split(',')[1]]+','+','.join(i.split(',')[2:]) +'\n' for i in lz2.split('\n')[:-1]]

# <codecell>

lw = [i.split(',')[1] for i in lz2.split('\n')[:-1]]

# <codecell>

# I need to correct 
# 'aa-bb'
# 'bb-aa'
# 'ab-bb'

lx = []
for i in lw:
    if i not in lx:
        lx.append(i)

# <codecell>

lx

# <codecell>

bbabf1 = []
for i in lz2.split('\n')[:-1]:
    if i.split(',')[1]== 'bb-ab':
        bbabf1.append(i)
bbabf1 = [i.split(',')[0] for i in bbabf1 ]

bbaaf1 = []
for i in lz2.split('\n')[:-1]:
    if i.split(',')[1]== 'bb-aa':
        bbaaf1.append(i)
bbaaf1 = [i.split(',')[0] for i in bbaaf1 ]

abbbf1 = []
for i in lz2.split('\n')[:-1]:
    if i.split(',')[1]== 'ab-bb':
        abbbf1.append(i)
abbbf1 = [i.split(',')[0] for i in abbbf1 ]

aabbf1 = []
for i in lz2.split('\n')[:-1]:
    if i.split(',')[1]== 'aa-bb':
        aabbf1.append(i)
aabbf1 = [i.split(',')[0] for i in aabbf1 ]

weird = aabbf1+abbbf1+bbaaf1+bbabf1

# <codecell>

import random

good = [i.split(',')[0] for i in lz if i.split(',')[0] not in weird]

# <codecell>

final = weird + random.sample(good, 86)

# <codecell>

len(final)

# <codecell>

small = [','.join(i)+'\n' for i in f7s[10:] if list(i)[0] in final]

# <codecell>

Small =   ','.join([','.join(list(i))+'\n' for i in f7s[:11]]+small).replace('\n,','\n')
Smallt = zip(*[i.split(',') for i in Small.split('\n')[:-1]])
Smallt2 = ','.join([ ','.join(list(i))+'\n' for i in Smallt]).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/small_fam7.csv', 'w')
z.write(Smallt2)
z.close()

# <codecell>


