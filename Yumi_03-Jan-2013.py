# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: we want to extract from a fasta file all the sequences that correspond to a list of fasta headers in a smaller fasta file

# <codecell>

import re
fasta0 = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
markers = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/Go_female_qtl1.csv', 'rU').read()

# <codecell>

asp = markers.split(',')
asp2 = [ '>'+i+'\n'+'\w+'+'\n'  for i in asp]
ls = []
for i in asp2:
    ls.append(re.search(i, fasta0).group())
lsj = ','.join(ls).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_fem.fa', 'w')
z.write(lsj)
z.close()

# <codecell>


 
