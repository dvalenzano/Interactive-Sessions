# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

Go_fam16_in = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inf_fam_Go/inf_fam_16.csv', 'rU').read()
Go_fam16_out = '/Volumes/group_dv/personal/DValenzano/Jan2014/out_reduced.csv'
z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/new-out_reduced.csv', 'w')

# <markdowncell>

# First, generate a hashtable with marker names and f1 genotypes

# <codecell>

Go_fam16_int = zip(*[ i.split(',') for i in Go_fam16_in.split('\n')[:-1]])

# <codecell>

keys = []
values = []
d = {}
for i in Go_fam16_int[10:]:
    keys.append(i[0])
    values.append(','.join(i[3:5]).replace(',',''))
    
d = dict(zip(keys, values))

# <codecell>

#lz = []
for i in open(Go_fam16_out):
    if i[0] == 'm':
        pass
    else:
        #lz.append([i.split(',')[0]]+[d[i.split(',')[0].split('-')[0]]+'_'+d[i.split(',')[0].split('-')[1]]]+i.split(',')[1:])
        z.write(','.join([i.split(',')[0]]+[d[i.split(',')[0].split('-')[0]]+'_'+d[i.split(',')[0].split('-')[1]]]+i.split(',')[1:]))
   

# <codecell>

z.close()

# <markdowncell>

# Now I'll try with the whole big table

################################################################################################################
##########################################  RUN ON THE LARGE FILE  #############################################
################################################################################################################

# <codecell>

Go_fam16_in = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inf_fam_Go/inf_fam_16.csv', 'rU').read()
Go_fam16_Out = '/Volumes/group_dv/personal/DValenzano/Jan2014/inf_fam_16_output.csv'
w = open('/Volumes/group_dv/personal/DValenzano/Jan2014/new-out_inf_fam_16.csv', 'w')

Go_fam16_int = zip(*[ i.split(',') for i in Go_fam16_in.split('\n')[:-1]])

keys = []
values = []
d = {}
for i in Go_fam16_int[10:]:
    keys.append(i[0])
    values.append(','.join(i[3:5]).replace(',',''))
    
D = dict(zip(keys, values))

for i in open(Go_fam16_Out):
    if i[0] == 'm':
        pass
    else:
        w.write(','.join([i.split(',')[0]]+[D[i.split(',')[0].split('-')[0]]+'_'+D[i.split(',')[0].split('-')[1]]]+i.split(',')[1:]))
   

# <codecell>


