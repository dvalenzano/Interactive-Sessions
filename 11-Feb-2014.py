# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
sys.path.append('/Users/DValenzano/Dropbox/programming/python/myscripts/')
import transp

Go_7 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_7.csv', 'rU').read()

# <codecell>

Go_7t = Go_7.split('\n')[:-1]
go_7 = Go_7t[:5]
for i in Go_7t[5:]:
    if int(i.split(',')[5]) >= 365:
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

# <codecell>

lw = []
for i in gosF[2:]:
    lw.append(i.split(',')[1])    

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
for i in gosF[2:]:
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
w = open('/Volumes/group_dv/personal/DValenzano/Feb2014/Go_fam7_Sqtl02.tsv', 'w')
#w = open('/Users/DValenzano/Dropbox/tmp/Go_fam7_Sqtl01.tsv', 'w')
w.write(lsZ)
w.close()

# <codecell>

Go_14 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_14.csv', 'rU').read()

Go_14t = Go_14.split('\n')[:-1]
go_14 = Go_14t[:5]
for i in Go_14t[5:]:
    if int(i.split(',')[5]) >= 365:
        go_14.append(i)

go_14T = zip(*[ i.split(',')  for i in go_14 ])
gO = ','.join([ ','.join(list(i))+'\n'  for i in go_14T]).replace('\n,','\n')
goS = gO.split('\n')
gos_N = [goS[1]]+[goS[5]]+goS[10:]
gos_nH = gos_N[0].split(',')[0]+',f1_gen,'+','.join(gos_N[0].split(',')[5:]) 
M = []
for i in gos_N[1:]: 
    M.append(i.split(',')[0]+','+','.join(i.split(',')[3:5]).replace(',','-')+','+','.join(i.split(',')[5:]))

gosF = [gos_nH]+M

import math
lS = ['Marker\tLRT\tLOD\tp_val\n']
for i in gosF[2:]:
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
        
lsZ = ','.join(lS).replace('\n,','\n')
w = open('/Volumes/group_dv/personal/DValenzano/Feb2014/Go_fam14_Sqtl02.tsv', 'w')
#w = open('/Users/DValenzano/Dropbox/tmp/Go_fam14_Sqtl01.tsv', 'w')
w.write(lsZ)
w.close()

# <codecell>

Go_8 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_8.csv', 'rU').read()

Go_8t = Go_8.split('\n')[:-1]
go_8 = Go_8t[:5]
for i in Go_8t[5:]:
    if int(i.split(',')[5]) >= 365:
        go_8.append(i)

go_8T = zip(*[ i.split(',')  for i in go_8 ])
gO = ','.join([ ','.join(list(i))+'\n'  for i in go_8T]).replace('\n,','\n')
goS = gO.split('\n')
gos_N = [goS[1]]+[goS[5]]+goS[10:]
gos_nH = gos_N[0].split(',')[0]+',f1_gen,'+','.join(gos_N[0].split(',')[5:]) 
M = []
for i in gos_N[1:]: 
    M.append(i.split(',')[0]+','+','.join(i.split(',')[3:5]).replace(',','-')+','+','.join(i.split(',')[5:]))

gosF = [gos_nH]+M

import math
lS = ['Marker\tLRT\tLOD\tp_val\n']
for i in gosF[2:]:
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
        
lsZ = ','.join(lS).replace('\n,','\n')
w = open('/Volumes/group_dv/personal/DValenzano/Feb2014/Go_fam8_Sqtl02.tsv', 'w')
#w = open('/Users/DValenzano/Dropbox/tmp/Go_fam8_Sqtl01.tsv', 'w')
w.write(lsZ)
w.close()

# <codecell>


