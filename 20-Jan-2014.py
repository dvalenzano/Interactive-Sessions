# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: to calculate Survival QTL in cross AAo and Go, using LRT method as I wrote it. This has to include both homozygous and heterozygous markers  
# For survival, I got to decide how to proceed, because it's not a binary trait, then I either treat it as such, or try to find a way to compute LRT with a continuous variable.  
# Since we're using different families, this has to be done family by family. 

# <markdowncell>

# To use lrt.py I need to arrange the data in a file like the following:  
# Clt1log.ID, ID1, ID2, ID3, ..., IDN\nphen, phen1, phen2, phen3, ..., phenn\nMark1, gen1, gen2, gen3, ..., genn\nMark2, gen1, gen2, gen3, ..., genn\n...

# <codecell>

import sys
sys.path.append('/Users/DValenzano/Dropbox/programming/python/myscripts/')
import transp

Go_7 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/Go_inf-fam/inf_fam_7.csv', 'rU').read()

# <codecell>

import math
import numpy

# <codecell>


# <codecell>

Go_7t = Go_7.split('\n')
go_7 = Go_7t[:5]
for i in Go_7t[5:]:
    if int(i.split(',')[5]) >= '266':
        go_7.append(i)

# <codecell>

go_7t = zip(*[ i.split(',')  for i in Go_7.split('\n')[:-1] ])

# <codecell>

go = ','.join([ ','.join(list(i))+'\n'  for i in go_7t]).replace('\n,','\n')

# <codecell>

gos = go.split('\n')

# <codecell>

age = map(int, gos[5].split(',')[5:])

# <codecell>

numpy.mean(age)

# <codecell>

gos_n = [gos[1]]+[gos[5]]+gos[10:]

# <codecell>

gos_n[0][:20]

# <codecell>

gos_nh = gos_n[0].split(',')[0]+',f1_gen,'+','.join(gos_n[0].split(',')[5:]) #header of the new file

# <codecell>

m = []
for i in gos_n[1:]: 
    m.append(i.split(',')[0]+','+','.join(i.split(',')[3:5]).replace(',','-')+','+','.join(i.split(',')[5:]))

# <codecell>

gosf = [gos_nh]+m

# <codecell>

ls = ['Marker:\tLRT\tLOD\tp_val\n']
for i in gosf[2:]:
    a = ','.join(i.split(',')[2:]).count('a')
    b = ','.join(i.split(',')[2:]).count('b')
    if a and b > 0:
        freq_a = float(a)/(a+b)
        freq_b = 1-freq_a
        if i.split(',')[1] == 'ab-ab':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_05 = (.5**a)*(.5**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_05))
            LOD = math.log10(MLE_ab/MLE_05)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            ls.append(out)
        elif i.split(',')[1] == 'ab-aa':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_075 = (.75**a)*(.25**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_075))
            LOD = math.log10(MLE_ab/MLE_075)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            ls.append(out)
        elif i.split(',')[1] == 'aa-ab':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_075 = (.75**a)*(.25**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_075))
            LOD = math.log10(MLE_ab/MLE_075)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            ls.append(out)
        else:
            pass

# <codecell>


# <codecell>


