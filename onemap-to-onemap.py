# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

ominp = open('/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/fam_7_OneMap.txt', 'rU').read()
qtlinp = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/fam_7_survbysex.csv', 'rU').read()

# <markdowncell>

# Now I transpose both matrices

# <codecell>

qtl = [ list(i) for i in zip(*[ i.split(',')  for i in qtlinp.split('\n')[:-1]])][0][1:]

# <codecell>

new_ominp = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(qtl))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in qtl]).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/f7_om_survbysex.txt', 'w')
z.write(new_ominp)
z.close()

# <codecell>

import sys

inp = raw_input('What family would you like to analyze?\n')
omfam = '/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/fam_%s_OneMap.txt' % inp
ominp = open(omfam, 'rU').read()
qtl = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fam_%s_survbysex.csv' % (inp, inp)
qtlinp = open(qtl, 'rU').read()
qtl = [ list(i) for i in zip(*[ i.split(',')  for i in qtlinp.split('\n')[:-1]])][0][1:]
new_ominp = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(qtl))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in qtl]).replace('\n,','\n')
out = '/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/f%s_om_survbysex.txt' % inp
z = open(out, 'w')
z.write(new_ominp)
z.close()

