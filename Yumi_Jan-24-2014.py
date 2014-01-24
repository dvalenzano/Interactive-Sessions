# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

rd = open('/Volumes/group_dv/group/data/WES/Nfur_exon_Yumi_short.fa', 'rU').read()
 
# <codecell>
 
rds = rd.split('\n')[:-1]

# <codecell>

rdss = []
for i in rds:
#    if i[0] == '>':
#        rdss[-1:]
    if '>' in i:
        rdss.append(i)         #take only scaffold number and exon region info.  

# <codecell>

rdss[:2]

# <codecell>

ls = list(set(rdss))

# <codecell>

print(len(ls), len(rdss)) #remove 100% duplicates in the list. This reduces from 439630 to 412908.

# <codecell>

# lss = ls.sort() 
lsim = []
for i in ls:
    lsim.append(i[19:].split('(')[0])

# <codecell>

keys = list(set([ i.split(':')[0] for i in lsim]))
values = [str('a')]*len(keys)

# <codecell>

d = []
for i in range(len(keys)):
    d.append(keys[i]+',')
#d = dict(zip(keys, values))

# <codecell>

d2 = []
for i in d:
    d2.append(i.split(','))
d2

# <codecell>

#lt = []
#for i in lsim:
#    if i.split(':')[0] in keys:
#        lt.append(i.split(':')[0]

from collections import defaultdict
e = defaultdict(d2)

for i in lsim:
    if i.split(':')[0] in keys:
        e[i.split(':')[0]].append(i.split(':')[1])
        

# <codecell>


# <codecell>

lt = []
for i in keys:
    if i in lsim:
        lt.append(i+lsim.split(':')[1]+'\n')#split(':')[1])#d[i.split(':')[0]].append(i.split(':')[1])

# <codecell>

lt

# <codecell>

lsim[:10]

# <codecell>


