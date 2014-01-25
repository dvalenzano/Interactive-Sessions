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
        
ls = list(set(rdss))

# <codecell>

lsim = []
for i in ls:
    lsim.append(i[19:].split('(')[0])

# <codecell>

keys = list(set([ i.split(':')[0] for i in lsim]))

# <codecell>

import re
str = ','.join(lsim)
lz = []
lz0 = []
for i in keys:
    match = re.findall(i+r':\d*-\d*', str)
    head = match[0].split(':')[0]
    tail = [j.split(':')[1] for j in match ]
    lz0.append(','.join([head]+tail))
    lz.append(','.join([head]+tail)+'\n')

# <codecell>

lzj = ','.join(lz).replace('\n,','\n')

# <markdowncell>

# The following line of code generates a dictionary, with scaffold as key, and interval of matching exons as values, just like you wanted

# <codecell>

values = [ i.split(',')[1:]  for i in lz0 ] 
d = dict(zip(keys, values))

# <codecell>

z = open('/Volumes/group_dv/group/data/WES/header_process0.csv', 'w')
z.write(lzj)
z.close()

# <codecell>


