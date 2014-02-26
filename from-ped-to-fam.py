# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

ped = open('/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_7/inf-fam_7.ped', 'rU').read()

# <codecell>

pedt = ','.join([','.join(i.split('\t')[:6])+'\n' for i in ped.split('\n')[:-1]]).replace('\n,','\n').replace(',','\t')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_7/inf-fam_7.fam', 'w')
z.write(pedt)
z.close()

