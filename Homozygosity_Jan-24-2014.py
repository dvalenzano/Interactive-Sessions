# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

tab = open('/Volumes/group_dv/personal/DValenzano/stacks/pop-stacks/pop-stacks_2/pop01_export_hp.tsv', 'rU').read()

# <codecell>

tabs = [ i.split('\t') for i in tab.split('\n')[:-1]]

# <codecell>

tabss = [i[12:] for i in tabs  if len(i) > 10]

# <codecell>

tabt =  [list(i) for i in zip(*(tabss))]

# <codecell>

import math
keys = [i[0]  for i in tabt ]

values = []
nonnull = []
for i in range(len(tabt)):
    null = float(tabt[i].count(''))
    het = float(','.join(tabt[i]).count('/'))
    values.append(1-(het/(len(tabt[0])-null-1)))
    nonnull.append(1-(null/float(len(tabt[0])-1))) #this last line indicates the fraction of genotyped markers

d = dict(zip(keys, values))

# <codecell>

lz = []
for i in keys:
    lz.append(i+','+str(d[i])+'\n')

# <codecell>

lz = ','.join(lz).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/Homozygosity.csv', 'w')
z.write(lz)
z.close()

# <markdowncell>

# Now I want to plot homozygosity as a function of assigned genotypes

# <codecell>

d2 = dict(zip(keys, nonnull))

# <codecell>

lz2 = ['ID,homozygosity,coverage\n']
for i in keys:
    lz2.append(i+','+str(d[i])+','+str(d2[i])+'\n')

# <codecell>

lz2 = ','.join(lz2).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/Homozygosity_2.csv', 'w')
z.write(lz2)
z.close()

# <codecell>


