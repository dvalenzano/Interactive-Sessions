# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
sys.path.append('/Users/DValenzano/Dropbox/programming/python/myscripts/')
import transp

Go_7 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_7.csv', 'rU').read()

Go_7s = Go_7.split('\n')[:-1]
go_7 = Go_7s[:5]
for i in Go_7s[5:]:
    if int(i.split(',')[5]) >= 365:
        go_7.append(i)
        
len7 = len(go_7) - 5

# <codecell>

Go_14 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_14.csv', 'rU').read()

Go_14s = Go_14.split('\n')[:-1]
go_14 = Go_14s[:5]
for i in Go_14s[5:]:
    if int(i.split(',')[5]) >= 365:
        go_14.append(i)
        
len14 = len(go_14) - 5

# <codecell>

Go_8 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_8.csv', 'rU').read()

Go_8s = Go_8.split('\n')[:-1]
go_8 = Go_8s[:5]
for i in Go_8s[5:]:
    if int(i.split(',')[5]) >= 365:
        go_8.append(i)
        
len8 = len(go_8) - 5

# <codecell>

print (
'fam 7 longest lived IDs: %s\n' 
'fam 14 longest lived IDs: %s\n'
'fam 8 longest lived IDs: %s\n'
) % (len7, len14, len8)

# <codecell>

Go_7t =[ list(j) for j in zip(*[ i.split(',') for i in Go_7.split('\n')[:-1]])]

# <codecell>

Go_14t =[ list(j) for j in zip(*[ i.split(',') for i in Go_14.split('\n')[:-1]])]

# <codecell>

sigma = open('/Volumes/group_dv/personal/DValenzano/Feb2014/max-surv_sm.csv', 'rU').read().replace('"','')

# <codecell>

sigma7 = [ i.split(',')[1] for i in sigma.split('\n')[:-1] if i.split(',')[2]=='fam7']
sigma14 = [ i.split(',')[1] for i in sigma.split('\n')[:-1] if i.split(',')[2]=='fam14']

# <codecell>

sigmr7 = [','.join(i) for i in Go_7t[:10] ]+[','.join(i)  for i in Go_7t[10:] if i[0] in sigma7]
sigmr14 = [','.join(i) for i in Go_14t[:10] ]+[','.join(i)  for i in Go_14t[10:] if i[0] in sigma14]

# <markdowncell>

# Now I need to transpose back to the initial arrangement of phenotypes and markers in columns, and markers in rows

# <codecell>

compr7 = ','.join([  ','.join(list(j))+'\n' for j in zip(*[ i.split(',') for i in sigmr7])]).replace(',\n','\n').replace('\n,','\n')
compr14 = ','.join([  ','.join(list(j))+'\n' for j in zip(*[ i.split(',') for i in sigmr14])]).replace(',\n','\n').replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Feb2014/reduced_7.csv', 'w')
z.write(compr7)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Feb2014/reduced_14.csv', 'w')
z.write(compr14)
z.close()

# <markdowncell>

# Now I need to select random sets of IDs from all the IDs for each family  
# In particular, I need 1000 sets of 8 IDs from fam 7, 1000 sets of 6 IDs from fam 14  

# <codecell>

import random
ids7 = []
for i in range(1000):
    ids7.append(','.join(random.sample(Go_7t[1][5:], 8)))
    

ids14 = []
for i in range(1000):
    ids14.append(','.join(random.sample(Go_14t[1][5:], 6)))

# <markdowncell>

# Now I need to build and concatenate 1000 matrices for fam 7 and 14

# <codecell>

head7 = ','.join([ i+'\n' for i in Go_7s[:5]]).replace('\n,','\n')
head14 = ','.join([ i+'\n' for i in Go_14s[:5]]).replace('\n,','\n')

# <codecell>

keys_7 = []
keys_14 = []
values_7 = []
values_14 = []

for i in Go_7s:
    keys_7.append(i.split(',')[1])
    values_7.append(i)

for i in Go_14s:
    keys_14.append(i.split(',')[1])
    values_14.append(i)
    
d7 = dict(zip(keys_7, values_7))
d14 = dict(zip(keys_14, values_14))

# <codecell>

n7 = []
for i in ids7:
    m7 = []
    for j in i.split(','):
        if j in keys_7:
            m7.append(d7[j]+'\n')
    n7.append(head7+','.join(m7)+'new')
n7_2 = ','.join(n7).replace('\n,','\n').replace('new,','new').replace('\nnew', 'new')

# <codecell>

n14 = []
for i in ids14:
    m14 = []
    for j in i.split(','):
        if j in keys_14:
            m14.append(d14[j]+'\n')
    n14.append(head14+','.join(m14)[:-1]+'new')
n14_2 = ','.join(n14).replace('\n,','\n').replace('new,','new').replace('\nnew', 'new')

# <markdowncell>

# n7_2 and n14_2 are now the two lists of matrices with random 8 and 6 individuals from family 7 and 14. I can now run lrt on each of them. 

# <codecell>

#z = open('/Users/DValenzano/Desktop/prova.csv', 'w')
#z.write(pr)
#z.close()

# <codecell>

score_fam7 = []
for m in n7_2.split('new')[:-1]:
    go_famT = zip(*[ i.split(',')  for i in m.split('\n')])
    gO = ','.join([ ','.join(list(i))+'\n'  for i in go_famT]).replace('\n,','\n')
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
       
    #lsZ = ','.join(lS).replace('\n,','\n')
    score_fam7.append(','.join(lS).replace('\n,','\n')+'new')

# <codecell>

sf7 = ','.join(score_fam7).replace('new,','new').replace('\nnew','new')[:-1]
#len(sf7.split('new'))

# <markdowncell>

# Same as above, for fam 14

# <codecell>

score_fam14 = []
for m in n14_2.split('new')[:-1]:
    go_famT = zip(*[ i.split(',')  for i in m.split('\n')])
    gO = ','.join([ ','.join(list(i))+'\n'  for i in go_famT]).replace('\n,','\n')
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
       
    #lsZ = ','.join(lS).replace('\n,','\n')
    score_fam14.append(','.join(lS).replace('\n,','\n')+'new')

# <codecell>

sf14 = ','.join(score_fam14).replace('new,','new').replace('\nnew','new')[:-1]
#len(sf14.split('new'))

# <codecell>

import numpy as np
sf7l = []
for i in sf7.split('new'):
    ls = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
    sf7l.append(np.percentile(ls, 95))
    a_95_7 = np.mean(sf7l)

# <codecell>

import numpy as np
sf14l = []
for i in sf14.split('new'):
    ls = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
    sf14l.append(np.percentile(ls, 95))
    a_95_14 = np.mean(sf14l)

# <codecell>

print (
       '95 percentile threshold for fam 7: %f\n'
       '95 percentile threshold for fam 14: %f\n'
       ) %(a_95_7, a_95_14)

# <markdowncell>

# Here follows the calculation for the 99 percentile

# <codecell>

import numpy as np
sf7l = []
for i in sf7.split('new'):
    ls = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
    sf7l.append(np.percentile(ls, 99))
    a_99_7 = np.mean(sf7l)
    
import numpy as np
sf14l = []
for i in sf14.split('new'):
    ls = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
    sf14l.append(np.percentile(ls, 99))
    a_99_14 = np.mean(sf14l)
    
print (
       '99 percentile threshold for fam 7: %f\n'
       '99 percentile threshold for fam 14: %f\n'
       ) %(a_99_7, a_99_14)

# <codecell>


