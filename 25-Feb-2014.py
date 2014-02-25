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

from sets import Set

set7 = set(sigma7)
ov7 = []
for i in sf7.split('new'):
    ls = []
    lz = []
    ln = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = set7 & set(lz)
        ln_in7 = len(both)
    ov7.append(ln_in7)

# <codecell>

#from sets import Set
#set7 = set(sigma7)
#ls = []
#lz = []
#ln = []
#for j in sf7.split('new')[0].split('\n')[1:]:
#    ls.append(float(j.split('\t')[2]))
#    ls2 = np.percentile(ls, 99)
#    if float(j.split('\t')[2]) >= ls2:
#        lz.append(j.split('\t')[0])
#    both = set7 & set(lz)
#    ln_in7 = len(both)    

# <codecell>

set14 = set(sigma14)
ov14 = []
for i in sf14.split('new'):
    ls = []
    lz = []
    ln = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = set14 & set(lz)
        ln_in14 = len(both)
    ov14.append(ln_in14)

# <codecell>

print (
       'hits per fam 7: %f +/- %f\n'
       'hits per fam 14: %f +/- %f\n'
       ) %(np.mean(ov7), np.std(ov7), np.mean(ov14), np.std(ov14)) 
       

# <markdowncell>

# len(sigma7) is 75 

# <markdowncell>

# len(sigma14) is 33

# <markdowncell>

# Now I will choose randomly 75 and 33 markers from the list of markers, and see what is the chance that these show up among the significant ones for both fam 7 and fam 14. 

# <codecell>

markers_7 = n7_2.split('new')[0].split('\n')[0].split(',')[10:]
markers_14 = n14_2.split('new')[0].split('\n')[0].split(',')[10:]

# <codecell>

random_7 = random.sample(markers_7, 75)
random_14 = random.sample(markers_14, 33)

# <codecell>

set_ran7 = set(random_7)
ov_ran7 = []
for i in sf7.split('new'):
    ls = []
    lz = []
    ln = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = set_ran7 & set(lz)
        ln_r7 = len(both)
    ov_ran7.append(ln_r7)

# <codecell>

set_ran14 = set(random_14)
ov_ran14 = []
for i in sf14.split('new'):
    ls = []
    lz = []
    ln = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = set_ran14 & set(lz)
        ln_r14 = len(both)
    ov_ran14.append(ln_r14)

# <codecell>

print (
       'hits per fam 7 in sample set: %f +/- %f\n'
       'hits per fam 14 in sample set: %f +/- %f\n'
       ) %(np.mean(ov_ran7), np.std(ov_ran7), np.mean(ov_ran14), np.std(ov_ran14)) 
       

# <markdowncell>

# Looks like 1 or perhaps two markers per fam are highly represented among the significant ones in all the matrices.  
# Now I need to get a plot of which ones are these markers.

# <codecell>

set7 = set(sigma7)
ov7_nail = []
for i in sf7.split('new'):
    ls = []
    lz = []
    ln = []
    vl = []
    lst7 = []
    d7 = {}
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = ','.join(list(set7 & set(lz)))
#        ln_in7 = len(both)
    ov7_nail.append(both)
    lst7 = ','.join(ov7_nail).split(',')
    d7 = dict(zip(list(set7), [ lst.count(i) for i in list(set7) ]))

# <codecell>

set14 = set(sigma14)
ov14_nail = []
for i in sf14.split('new'):
    ls = []
    lz = []
    ln = []
    vl = []
    lst14 = []
    d14 = {}
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = ','.join(list(set14 & set(lz)))
#        ln_in14 = len(both)
    ov14_nail.append(both)
    lst14 = ','.join(ov14_nail).split(',')
    d14 = dict(zip(list(set14), [ lst14.count(i) for i in list(set14) ]))

# <codecell>

d7 = d
lst7 = lst

# <codecell>

def myfun(s):
    return s[-1]
td7 = d7.items()
#x7 = list(set7)
x7 = [i[0] for i in sorted(td7, key=myfun, reverse=True)]

#y7 = [ d7[i] for i in list(set7)]
y7 = [ d7[i] for i in x7]

import matplotlib.pyplot as plt

pos = np.arange(len(x7))
width = .9     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(x7)

plt.bar(pos, y7, width, color='r')
xlabel('markers significant in fam 7 for max lifespan')
ylabel(' frequency ')
plt.show()

# <codecell>

def myfun(s):
    return s[-1]
td14 = d14.items()
#x7 = list(set14)
x14 = [i[0] for i in sorted(td14, key=myfun, reverse=True)]

#y14 = [ d14[i] for i in list(set14)]
y14 = [ d14[i] for i in x14]

import matplotlib.pyplot as plt

pos = np.arange(len(x14))
width = .9     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(x14)

plt.bar(pos, y14, width, color='r')
xlabel('markers significant in fam 14 for max lifespan')
ylabel(' frequency ')
plt.show()

# <markdowncell>

# Now I need to perform the same analysis with the random set of markers from fam 7 and 14

# <codecell>

set_ran7_2 = set(random_7)
ov7_nail_2 = []
for i in sf7.split('new'):
    ls = []
    lst_7_2 = []
    d7_2 = {}
    lz = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = ','.join(list(set_ran7_2 & set(lz)))
    #        ln_in7 = len(both)
    ov7_nail_2.append(both)
    lst_7_2 = ','.join(ov7_nail_2).split(',')
    d7_2 = dict(zip(list(set_ran7_2), [ lst_7_2.count(i) for i in list(set_ran7_2) ]))

# <codecell>

def myfun(s):
    return s[-1]
td7_2 = d7_2.items()
#x7_2 = list(set14)
x7_2 = [i[0] for i in sorted(td7_2, key=myfun, reverse=True)]

#y7_2 = [ d14[i] for i in list(set14)]
y7_2 = [ d7_2[i] for i in x7_2]

import matplotlib.pyplot as plt

pos = np.arange(len(x7_2))
width = .9     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(x7_2)

plt.bar(pos, y7_2, width, color='r')
xlabel('markers significant in fam 7 for max lifespan')
ylabel(' frequency ')
title('frequency distribution of random hits in random matrices (fam7)')
plt.show()

# <codecell>

set_ran14_2 = set(random_14)
ov14_nail_2 = []
for i in sf14.split('new'):
    ls = []
    lst_14_2 = []
    d14_2 = {}
    lz = []
    for j in i.split('\n')[1:]:
        ls.append(float(j.split('\t')[2]))
        ls2 = np.percentile(ls, 99)
        if float(j.split('\t')[2]) >= ls2:
            lz.append(j.split('\t')[0])
        both = ','.join(list(set_ran14_2 & set(lz)))
    #        ln_in14 = len(both)
    ov14_nail_2.append(both)
    lst_14_2 = ','.join(ov14_nail_2).split(',')
    d14_2 = dict(zip(list(set_ran14_2), [ lst_14_2.count(i) for i in list(set_ran14_2) ]))

# <codecell>

def myfun(s):
    return s[-1]
td14_2 = d14_2.items()
#x14_2 = list(set14)
x14_2 = [i[0] for i in sorted(td14_2, key=myfun, reverse=True)]

#y7_2 = [ d14[i] for i in list(set14)]
y14_2 = [ d14_2[i] for i in x14_2]

import matplotlib.pyplot as plt

pos = np.arange(len(x14_2))
width = .9     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(x14_2)

plt.bar(pos, y14_2, width, color='r')
xlabel('markers significant in fam 14 for max lifespan')
ylabel(' frequency ')
title('frequency distribution of random hits in random matrices (fam14)')
plt.show()

# <codecell>

lst7j = open('/Volumes/group_dv/personal/DValenzano/Feb2014/list7.csv', 'w')
lst14j = open('/Volumes/group_dv/personal/DValenzano/Feb2014/list14.csv', 'w')
lst7_2j = open('/Volumes/group_dv/personal/DValenzano/Feb2014/list7_2.csv', 'w')
lst14_2j = open('/Volumes/group_dv/personal/DValenzano/Feb2014/list14_2.csv', 'w')
lst7j.write(','.join(lst7))
lst14j.write(','.join(lst14))
lst7_2j.write(','.join(lst_7_2))
lst14_2j.write(','.join(lst_14_2))
lst7j.close()
lst14j.close()
lst7_2j.close()
lst14_2j.close()

# <codecell>


