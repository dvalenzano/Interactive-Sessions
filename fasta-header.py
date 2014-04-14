# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

kita = open('/Volumes/group_dv/group/tmp/kita_jena.fa', 'rU').read()
newkita = kita.split('\n')[0].replace(' ', '_')+'\n'+','.join([  i+'\n' for i in kita.split('\n')[1:-1]]).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/group/tmp/kita_j2.fa', 'w')
z.write(newkita)
z.close()

# <codecell>

z = open('/Volumes/group_dv/group/tmp/kita_j2.fa', 'w')
z.write(newkita)
z.close()

# <codecell>


