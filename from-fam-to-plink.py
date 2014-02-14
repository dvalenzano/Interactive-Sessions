# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

f8 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_8.csv', 'rU').read()
f8s = f8.split('\n')[:-1]

# <markdowncell>

# First I need to generate a ped file

# <codecell>

f8s2 = [','.join(i.split(',')[:6]) +','+ ','.join(i.split(',')[10:]) for i in f8s[1:]]

# <codecell>

def blast(input):
    ls = []
    for i in input.split(',')[6:]:
        if len(i)== 2:
            ls.append(i[0]+','+i[1])
        else:
            ls.append(i+','+i)
    return ','.join(ls)+'\n'

# <codecell>

ped8 = ','.join([ ','.join(i.split(',')[:6])+','+blast(i) for i in f8s2 ]).replace('\n,','\n').replace(',','\t')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Feb2014/plink/inf-fam_8.ped','w')
z.write(ped8)
z.close()

# <markdowncell>

# Now we need a MAP file, where, by default, each line describes a single marker and must contain exactly 4 columns:  
#      chromosome (1-22, X, Y or 0 if unplaced)  
#      rs# or snp identifier  
#      Genetic distance (morgans)  
#      Base-pair position (bp units)  

# <codecell>

map_col2 = ','.join(f8s[0].split(',')[10:])+'\n'

# <codecell>

map_col1 = ('1,'*7694)[:-1]+'\n'

# <codecell>

len(map_col1.split(','))

# <codecell>

map_col3 = ('0,'*7694)[:-1]+'\n'
map_col4 = ('0,'*7694)[:-1]

# <codecell>

Map = map_col1+map_col2+map_col3+map_col4
mapt = zip(*[ i.split(',')    for i in Map.split('\n')])
maptf = ','.join([','.join(i)+'\n' for i in mapt  ]).replace('\n,','\n')[:-1].replace(',','\t')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Feb2014/plink/inf-fam_8.map', 'w')
z.write(maptf)
z.close()

