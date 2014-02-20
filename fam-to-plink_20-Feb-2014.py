# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
inp = raw_input('What family would you like to analyze?\n')
inp2 = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_%s.csv' % inp

fam = open(inp2, 'rU').read()
fams = fam.split('\n')[:-1]

# <markdowncell>

# First I need to generate a ped file

# <codecell>

fams2 = [','.join(i.split(',')[:6]) +','+ ','.join(i.split(',')[10:]) for i in fams[1:]]

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

pedfam = ','.join([ ','.join(i.split(',')[:6])+','+blast(i) for i in fams2 ]).replace('\n,','\n').replace(',','\t')

# <codecell>

out0 = '/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_%s/inf-fam_%s.ped' % (inp, inp)
z = open(out0,'w')
z.write(pedfam)
z.close()

# <markdowncell>

# Now we need a MAP file, where, by default, each line describes a single marker and must contain exactly 4 columns:  
#      chromosome (1-22, X, Y or 0 if unplaced)  
#      rs# or snp identifier  
#      Genetic distance (morgans)  
#      Base-pair position (bp units)  

# <codecell>

map_col2 = ','.join(fams[0].split(',')[10:])+'\n'

# <codecell>

snpn = len(fams[0].split(',')[10:]) #this line gives me the number of microsatellites

# <codecell>

map_col1 = ('1,'*snpn)[:-1]+'\n'

# <codecell>

map_col3 = ('0,'*snpn)[:-1]+'\n'
map_col4 = ('0,'*snpn)[:-1]

# <codecell>

Map = map_col1+map_col2+map_col3+map_col4
mapt = zip(*[ i.split(',')    for i in Map.split('\n')])
maptf = ','.join([','.join(i)+'\n' for i in mapt  ]).replace('\n,','\n')[:-1].replace(',','\t')

# <codecell>

out1 = '/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_%s/inf-fam_%s.map' % (inp, inp)
z = open(out1, 'w')
z.write(maptf)
z.close()

# <codecell>

famt = zip(*[i.split(',') for i in fam.split('\n')[:-1]])
famt2 = famt[:2]+famt[4:]
head = ','.join([','.join(list(j)+['\n'])  for j in zip(*[list(i) for i in famt2[:8]])[1:]]).replace(',\n','\n').replace('\n,','\n').replace(',','\t')
z0 = '/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_%s/fam_%scov.txt' % (inp, inp)
z = open(z0, 'w')
z.write(head)
z.close()

