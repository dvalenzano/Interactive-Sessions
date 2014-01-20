# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

young = []
adult = []
old = []
resources = []

### script here ###

young.append(#output for len(young) at every time point)
aduld.append(#output for len(adult) at every time point)
old.append(#output for len(old) at every time point)
resources.append(#same thing as above)
 
# These are all lists, not strings, so they cannot be saved as a file. 

yst = ','.join(young)+'\n' #now you have a string
ast = ','.join(adult)+'\n'
ost = ','.join(old)+'\n'
res = ','.join(resources)+'\n'

tab = (yst+ast+ost+res).replace('\n,','\n')

tabt = zip(*[i.split(',') for i in tab.split('\n')]) #transpose tab so that y, a, o, r are columns, not rows - now you have an array, which is a list of lists, so we need to re-join everything in a big string

tabtj = ','.join([  ','.join(list(i))+'\n'  for i in tabt]).replace('\n,','\n')

z = open('/path-to-file-you-want-to-save', 'w')
z.write(tabtj)
z.close()

