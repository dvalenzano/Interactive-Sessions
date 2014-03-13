# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

f7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/inf-fam_7.assoc.linear', 'rU').read()
f14 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/inf-fam_14.assoc.linear', 'rU').read()
f8 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/inf-fam_8.assoc.linear', 'rU').read()
f1_1 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/inf-fam_1.1.assoc.linear', 'rU').read()

# <codecell>

f7s = [i.split() for i in f7.split('\n')[:-1]]
f14s = [i.split() for i in f14.split('\n')[:-1]]
f8s = [i.split() for i in f8.split('\n')[:-1]]
f1_1s = [i.split() for i in f1_1.split('\n')[:-1]]

# <codecell>

f7ss = [i[1]+','+i[8] for i in f7s ][2::3]
f14ss = [i[1]+','+i[8] for i in f14s ][2::3]
f1_1ss = [i[1]+','+i[8] for i in f1_1s ][2::3]
f8ss = [i[1]+','+i[8] for i in f8s ][2::3]

# <codecell>

k7 = [i.split(',')[0] for i in f7ss ]
v7 = [i.split(',')[1] for i in f7ss ]
d7 = dict(zip(k7, v7))

k14 = [i.split(',')[0] for i in f14ss ]
v14 = [i.split(',')[1] for i in f14ss ]
d14 = dict(zip(k14, v14))

k8 = [i.split(',')[0] for i in f8ss ]
v8 = [i.split(',')[1] for i in f8ss ]
d8 = dict(zip(k8, v8))

k1_1 = [i.split(',')[0] for i in f1_1ss ]
v1_1 = [i.split(',')[1] for i in f1_1ss ]
d1_1 = dict(zip(k1_1, v1_1))

# <codecell>

from sets import Set
ins7_14 = Set(k7).intersection(Set(k14))
ins7_8 = Set(k7).intersection(Set(k8))
ins7_1_1 = Set(k7).intersection(Set(k1_1))
ins14_8 = Set(k14).intersection(Set(k8))
ins14_1_1 = Set(k14).intersection(Set(k1_1))
ins8_1_1 = Set(k8).intersection(Set(k1_1))

# <codecell>

li = list(ins7_14)
lif = 'Marker,fam7,fam14\n'+','.join([ i+','+d7[i]+','+d14[i]+'\n' for i in li ]).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/f7_14.csv', 'w')
z.write(lif)
z.close()

# <codecell>


