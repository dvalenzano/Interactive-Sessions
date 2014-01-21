# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# I need a file that lists all the possible F1 genotypes available in a ped file like '/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/Go_inf-fam/inf_fam_7.csv' 

# <codecell>

import sys
sys.path.append('/Users/DValenzano/Dropbox/programming/python/myscripts/')
import transp

Go_7 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/Go_inf-fam/inf_fam_7.csv', 'rU').read()

# <codecell>

Go_7t = Go_7.split('\n')[:-1]
go_7 = Go_7t[:5]
for i in Go_7t[5:]:
    if int(i.split(',')[5]) >= 266:
        go_7.append(i)

go_7T = zip(*[ i.split(',')  for i in go_7 ])
gO = ','.join([ ','.join(list(i))+'\n'  for i in go_7T]).replace('\n,','\n')
goS = gO.split('\n')
gos_N = [goS[1]]+[goS[5]]+goS[10:]
gos_nH = gos_N[0].split(',')[0]+',f1_gen,'+','.join(gos_N[0].split(',')[5:]) 
M = []
for i in gos_N[1:]: 
    M.append(i.split(',')[0]+','+','.join(i.split(',')[3:5]).replace(',','-')+','+','.join(i.split(',')[5:]))

gosF = [gos_nH]+M

# <markdowncell>

# Now I need to list the F1 types

# <codecell>

lw = []
for i in gosf[2:]:
    lw.append(i.split(',')[1])    

# <markdowncell>

# Here how to output the types of F1 genotypes:

# <codecell>

lx = []
for i in lw:
    if i in lx:
        pass
    else:
        lx.append(i)

# <codecell>

lx

# <codecell>

import math
lS = ['Marker\tLRT\tLOD\tp_val\n']
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
            out = i.split(',')[0]+ '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            lS.append(out)
        elif i.split(',')[1] == 'ab-aa':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_075 = (.75**a)*(.25**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_075))
            LOD = math.log10(MLE_ab/MLE_075)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0] + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            lS.append(out)
        elif i.split(',')[1] == 'aa-ab':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_075 = (.75**a)*(.25**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_075))
            LOD = math.log10(MLE_ab/MLE_075)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0]+ '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            lS.append(out)
        elif i.split(',')[1] == 'bb-ab':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_025 = (.25**a)*(.75**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_025))
            LOD = math.log10(MLE_ab/MLE_025)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0]+ '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            lS.append(out)
        elif i.split(',')[1] == 'ab-bb':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_025 = (.25**a)*(.75**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_025))
            LOD = math.log10(MLE_ab/MLE_025)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0] + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            lS.append(out)
        elif i.split(',')[1] == 'aa-bb':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_05 = (.5**a)*(.5**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_05))
            LOD = math.log10(MLE_ab/MLE_05)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0]+ '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            lS.append(out)
        elif i.split(',')[1] == 'bb-aa':
            MLE_ab = (freq_a**a)*(freq_b**b)
            MLE_05 = (.5**a)*(.5**b) 
            LRT = 2*(math.log(MLE_ab)-math.log(MLE_05))
            LOD = math.log10(MLE_ab/MLE_05)
            p_val = 1.0/(10**(LOD))
            out = i.split(',')[0]+ '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
            lS.append(out)
        else:
            pass

# <codecell>

lS[:10]

# <codecell>

lsZ = ','.join(lS).replace('\n,','\n')
w = open('/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/Go_fam7_Sqtl01.tsv', 'w')
#w = open('/Users/DValenzano/Dropbox/tmp/Go_fam7_Sqtl01.tsv', 'w')
w.write(lsZ)
w.close()

# <codecell>


