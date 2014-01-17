# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

bm = open('/Volumes/group_dv/group/files_for_melanoma_qtl/lrt_m_out.csv', 'rU').read()

# <codecell>

bms = bm.split('\D')[:-2]

# <markdowncell>

# There are 367 markers per matrix

# <codecell>

markers = []
for i in bms[0].split('\n'):
    markers.append(i.split('\t')[0])

# <codecell>

ls = []
ls2 = []
for i in bms:
    ls.append(i.split('\n')[2].split('\t')[2])
ls2 = markers[2]+','+','.join(ls)

# <codecell>

def loop1(markers, j):
    ls = []
    for i in bms:
        ls.append(i.split('\n')[j].split('\t')[2])
    return markers[j]+','+','.join(ls)

# <codecell>

marlod = []
for n in range(1, len(bms[0].split('\n'))):
               marlod.append(loop1(markers, n)+'\n')

# <codecell>

d = {}
lods = [ map(float, i.split(',')[1:]) for i in marlod] #check out the map() function in this line, converts a list of strings into a list of floats

# <codecell>

d = dict(zip(markers, lods))

# <codecell>

len(d['7854'])

# <codecell>

d['7854'] #this is how you call the values of a given key in a dictionary (or hashtable, same thing)

# <codecell>

sum(d['7854'])/50 #average LOD score for marker 7854

# <codecell>

# for standard deviation either you calculate it yourself, or you simply call the function SD, which I am sure you can import form numpy or scipy

# <codecell>

from numpy import * # check how to go from here

# <codecell>

np.std(d['7854'])

# <codecell>


