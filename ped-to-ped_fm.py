# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
inp = raw_input('What family would you like to analyze?\n')
inp2 = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/inf-fam_%s.ped' % (inp, inp)
inP = open(inp2, 'rU').read()

# <codecell>

m = []
f = []
for i in inP.split('\n')[4:-1]:
    if i.split('\t')[4]=='2':
        f.append(i+'\n')
    elif i.split('\t')[4]=='1':
        m.append(i+'\n')
        
f = ','.join([ i+'\n' for i in inP.split('\n')[:4]]).replace('\n,','\n').replace(',','\t') + ','.join(f).replace('\n,','\n').replace(',','\t')
m = ','.join([ i+'\n' for i in inP.split('\n')[:4]]).replace('\n,','\n').replace(',','\t') + ','.join(m).replace('\n,','\n').replace(',','\t')

# <codecell>

fsave = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fem/fam_%sf.ped'  % (inp, inp)
msave = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/mal/fam_%sm.ped'  % (inp, inp)
z = open(fsave, 'w') 
w = open(msave, 'w')
z.write(f)
w.write(m)
z.close()
w.close()

# <codecell>


