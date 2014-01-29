# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

tr = open('/Volumes/group_dv/group/data/sequences/transcriptome/Annotated_Reference_Nfurzeri_transcriptome_Liver_Testis_Brain.fa', 'rU').read()

# <codecell>

tr2 = tr.replace('>', '\m>')
tr2s = tr2.split('\m')
tr3 = set(tr2s)

# <codecell>

tr4 = ','.join(tr3).replace(',','')

# <codecell>

print (
len(tr), 
len(tr4),
len(tr)-len(tr4)
)

# <codecell>

#z = open('/Volumes/group_dv/group/data/sequences/transcriptome/Nfur_transcriptome_reduced.fa', 'w')
#z.write(tr4)
#z.close()

# <codecell>

keys = tr.split('\n')[:-1][::2]
values = tr.split('\n')[:-1][1::2]
d = dict(zip(keys, values))

# <codecell>

keyss = set(keys)

# <codecell>

len(keys)==len(keyss)

# <codecell>

ls = []
for i in keyss:
    ls.append(i+'\n'+d[i]+'\n')
lsj = ','.join(ls).replace('\n,','\n').replace(',','')

# <codecell>

z = open('/Volumes/group_dv/group/data/sequences/transcriptome/Nfur_transcriptome_reduced.fa', 'w')
z.write(lsj)
z.close()

