# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

fa = open('/Volumes/group_dv/personal/DValenzano/Shuhei/vasa_transcript_Jena.fa', 'rU').read()
fan = ','.join(fa.split('\n')[0]).replace(',','') + '\n'+','.join([ i.upper() for i in fa.split('\n')[1]]).replace(',','')

# <codecell>

fan

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Shuhei/vasa_transcript_Jena_2.fa','w')
z.write(fan)
z.close()

# <codecell>


