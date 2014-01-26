# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

surv = open('/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/grz2_survivial.csv', 'rU').read()

# <codecell>

ss = surv.split('\n')[:-1]

# <codecell>

ssn = [i.split(',') for i in ss]

# <codecell>

new = 'days,females,males,na,whole\n'

# <codecell>

ls = []
for i in ssn[1:]:
    if i[4] == '1':
       ls.append(i[3]+',1,,,\n')
    elif i[4] == '2':
        ls.append(i[3]+',,1,,\n')
    elif i[4] == '3':
        ls.append(i[3]+',,,1,\n')
    elif i[4] == '4':
        ls.append(i[3]+',,,,1\n')

# <codecell>

fin = ','.join([new]+ls).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/grz2_prism.csv', 'w')
z.write(fin)
z.close()

# <codecell>


