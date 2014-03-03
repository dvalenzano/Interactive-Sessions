# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

survbysex_fam7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/inf-fam_7.assoc.linear.csv', 'rU').read()

# <codecell>

sbss = []
for i in survbysex_fam7.split('\n')[1:-2]:
    if i.split(',')[8] != 'NA':
        if float(i.split(',')[8]) < 0.01:
            sbss.append(i)

# <codecell>

sbs_7 = 'Marker,TEST,p-val\n'+','.join([ i.split(',')[1]+','+i.split(',')[4]+','+i.split(',')[8]+'\n' for i in sbss   ]).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/fam_7_survbysex.csv', 'w')
z.write(sbs_7)
z.close()

# <codecell>

Below I do the same for family 8:

# <codecell>

assoc = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/inf-fam_8.assoc.linear', 'rU').read()
import re
assocs = ','.join([ ','.join(i.split())+'\n' for i in assoc.split('\n')]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/inf-fam_8.assoc.linear.csv', 'w')
z.write(assocs)
z.close()

# <codecell>

assocs = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/inf-fam_8.assoc.linear.csv', 'rU').read()
sbss_8 = []
for i in assocs.split('\n')[1:-2]:
    if i.split(',')[8] != 'NA':
        if float(i.split(',')[8]) < 0.01:
            sbss_8.append(i)
sbs_8 = 'Marker,TEST,p-val\n'+','.join([ i.split(',')[1]+','+i.split(',')[4]+','+i.split(',')[8]+'\n' for i in sbss_8   ]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/fam_8_survbysex.csv', 'w')
z.write(sbs_8)
z.close()

# <codecell>

assoc = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/inf-fam_14.assoc.linear', 'rU').read()
import re
assocs = ','.join([ ','.join(i.split())+'\n' for i in assoc.split('\n')]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/inf-fam_14.assoc.linear.csv', 'w')
z.write(assocs)
z.close()
#assocs = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/inf-fam_14.assoc.linear.csv', 'rU').read()
sbss_14 = []
for i in assocs.split('\n')[1:-2]:
    if i.split(',')[8] != 'NA':
        if float(i.split(',')[8]) < 0.01:
            sbss_14.append(i)
sbs_14 = 'Marker,TEST,p-val\n'+','.join([ i.split(',')[1]+','+i.split(',')[4]+','+i.split(',')[8]+'\n' for i in sbss_14   ]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/fam_14_survbysex.csv', 'w')
z.write(sbs_14)
z.close()

# <codecell>

assoc = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/inf-fam_1.1.assoc.linear', 'rU').read()
import re
assocs = ','.join([ ','.join(i.split())+'\n' for i in assoc.split('\n')]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/inf-fam_1.1.assoc.linear.csv', 'w')
z.write(assocs)
z.close()
#assocs = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/inf-fam_1.1.assoc.linear.csv', 'rU').read()
sbss_1_1 = []
for i in assocs.split('\n')[1:-2]:
    if i.split(',')[8] != 'NA':
        if float(i.split(',')[8]) < 0.01:
            sbss_1_1.append(i)
sbs_1_1 = 'Marker,TEST,p-val\n'+','.join([ i.split(',')[1]+','+i.split(',')[4]+','+i.split(',')[8]+'\n' for i in sbss_1_1   ]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/fam_1.1_survbysex.csv', 'w')
z.write(sbs_1_1)
z.close()

# <codecell>


