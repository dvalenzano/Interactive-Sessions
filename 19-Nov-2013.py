# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# add phenotypes to genotype table 

# <codecell>

go = open('/Volumes/group_dv/personal/DValenzano/Nov2013/NfGo_allgeno-t.csv', 'rU').read()
aao = open('/Volumes/group_dv/personal/DValenzano/Nov2013/NfAAo_allgeno-t.csv', 'rU').read()
gn = open('/Users/DValenzano/cecco/Rad-Tag/Apr2013/Gn_final_LM_fam.csv', 'rU').read()
aan = open('/Volumes/group_dv/personal/DValenzano/Nov2013/NfAAn_allpg_transp_pheno2.csv', 'rU').read()

# <codecell>

gos = go.split('\n')[:-1]
aaos = aao.split('\n')[:-1]
gns = gn.split('\n')
aans = aan.split('\n')

# <headingcell level=4>

# First cross Go

# <codecell>

gols = []
for i in gos:
    gols.append([i.split(',')[0]]+['-', '-', '-', '-', '-', '-', '-', '-']+i.split(',')[1:])

# <codecell>

gols0 = ','.join(gns[0].split(',')[:8]+['melanoma']+gols[0][9:])+'\n'

# <codecell>

keys = []
values = []
for i in gns[3:]:
    keys.append(i.split(',')[0])
    values.append(','.join(i.split(',')[1:8]))
#keys = ','.join(keys)
#values = ','.join(values)
dgn = dict(zip(keys, values))

# <codecell>

ls = []
for i in gols[2:]:
    if i[0] in keys:
        ls.append([i[0]]+dgn[i[0]].split(',')+i[8:])
    else: 
        ls.append(i)   

# <codecell>

lsj = []
for i in ls:
    lsj.append(','.join(i)+'\n')

# <codecell>

lsj2 = ','.join(lsj).replace('\n,','\n')[:-1]

# <codecell>

goo2 = gols0+','.join(gols[1])+'\n'+lsj2

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/go_phen0.csv', 'w')
z.write(goo2)
z.close()

# <markdowncell>

# Now I need to fix the P0 genotypes - will do later - first I need to fix the

# <headingcell level=4>

# Second cross AAo

# <codecell>

aaols = []
for i in aaos:
    aaols.append([i.split(',')[0]]+['-', '-', '-', '-', '-', '-', '-', '-', '-']+i.split(',')[1:])

# <codecell>

aaols0 = ','.join(aans[0].split(',')[:10]+aaos[0].split(',')[1:])

# <codecell>

keys = []
values = []
for i in aans[2:]:
    keys.append(i.split(',')[0])
    values.append(','.join(i.split(',')[1:10]))
#keys = ','.join(keys)
#values = ','.join(values)
dgn = dict(zip(keys, values))

# <codecell>

ls = []
for i in aaols[2:]:
    if i[0] in keys:
        ls.append([i[0]]+dgn[i[0]].split(',')+i[10:])
    else: 
        ls.append(i)   

# <codecell>

lsj = []
for i in ls:
    lsj.append(','.join(i)+'\n')

# <codecell>

lsj2 = ','.join(lsj).replace('\n,','\n')[:-1]

# <codecell>

aao2 = aaols0+'\n'+','.join(aaols[1])+'\n'+lsj2

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aao_phen0.csv', 'w')
z.write(aao2)
z.close()

# <codecell>


