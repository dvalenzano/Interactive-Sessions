# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# As always, all this scripts are saved in my [github](https://github.com/dvalenzano) personal page
# 
# Goal: to filter for mis-coded F1/F2 genotypes, derived from situations like the following:
# 
# P0: aaxbb
# F1: *bb*
# F2: *aa*
# 
# P0: aaxbb
# F1: *aa*
# F2: *bb*
# 
# Rationale: if there are 'bb' or 'aa' genotypes in the F1 from aabb P0 parents, then I do not expect to have 'aa' and 'bb' genotypes respectively in the F2 genotypes. So what do I do if I do have 'aa' in an F2 from a 'bbab' F1 genotype? Here's the thing: I can use likelyhood ratio test.   
# Example: P0= aabb; F1=abaa; and I do find one F2 with a 'bb' genotype, which is not expected given the parents' genotypes. Now it could be that either one of the F1 is mis-typed, or that the F2 is mistyped. How do I know what's wrong? Given abaa F1, I expect to have 3a:1b in the F2. If, in fact, the F2 have a 3a:1b ratio, than most likely the 'bb' F2 is just mis-typed and I will correct it to 'ab'. However, if the allele frequency in the F2 is 1a:1b, then most likely one F1 genotype is wrong, and rather than being aaab, or abaa, it's actually abab. 
# 
# Similar approach applies for the following genotypes:
# 
# P0: aaxab
# F1: aaxab
# F2: *bb*
# 
# P0: aaxab
# F1: *bb*
# F2: *aa* 
# 
# 
# So here are the steps and the pseudocode:
# 
# For each family  
# Find the mismatching F1-F2 genotypes  
# Save the IDs  
# measure the allele frequency for these markers 
# if the allele frequency is compatible with the F1 model (run likelihood ratio test), then modify the F2 genotype  
# elsif the allele frequency is incompatible with the F1 model (run likelihood ratio test), then re-type F1 alleles 

# <codecell>

import math

# <codecell>

go1 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inf_fam_Go/inf_fam_1.csv', 'rU').read()

# <codecell>

go1t = zip(*[ i.split(',')  for i in go1.split('\n')[:-1]])

# <codecell>

ID = []
p0 = []
f1 = []
f2 = []
p0f1 = []
f1f2 = []
keys = []
aL = []
for i in go1t[10:]:
    ID.append(i[0])
    p0.append(i[1]+i[2])
    f1.append(i[3]+i[4])
    p0f1.append(i[1]+i[2]+i[3]+i[4])
    f2.append(list(i[5:]))
    f1f2.append(list(i[3:]))
    keys.append(i[0]+','+i[1]+i[2]+','+i[3]+','+i[4])
    aL.append(list(i))

# <codecell>

d = dict(zip(keys, f2))
df2 = dict(zip(ID, f2))
df1f2 = dict(zip(ID, f1f2))
df1 = dict(zip(ID, f1))
daL = dict(zip(ID, aL))

# <codecell>

q = []
for i in ID:
    if df1[i] == 'abbb':
        q.append(i)
        
len(q) # this q is the list of F1 that have 'abbb' genotypes

# <codecell>

daL[q[0]]

# <codecell>

def count_allele(input): #the input here is an ID
    al = ['a','b']
    values = 2*df2[input].count('aa')+df2[input].count('ab'), 2*df2[input].count('bb')+df2[input].count('ab')
    return dict(zip(al, values))

# <codecell>

P0_aabb = []
for i in keys:
    if i.split(',')[1] == 'aabb':
        P0_aabb.append(i)

# <codecell>

#oddF1_aa = []
#oddF1_bb = []
#for i in P0_aabb:
#    if i.split(',')[2] == 'aa':
#        oddF1_aa.append(i)
#    elif i.split(',')[3] == 'aa':
#        oddF1_aa.append(i) 
#    elif i.split(',')[2] == 'bb':
#        oddF1_bb.append(i)
#    elif i.split(',')[3] == 'bb':
#        oddF1_bb.append(i)

# <codecell>

#odd_ID_aa = []
#for i in oddF1_aa:
#    if 'bb' in d[i]:
#        odd_ID_aa.append(i.split(',')[0])

# <codecell>

#odd_ID_bb = []
#for i in oddF1_bb:
#    if 'aa' in d[i]:
#        odd_ID_bb.append(i.split(',')[0])

# <markdowncell>

# <del> Now I need to find the markers where - in oddF1_bb - there are F2 with 'aa' genotypes, and in oddF1_aa, there are F2 with 'bb' genotypes </del>  
# I will only allow F1 from aabb P0 to be abab

# <markdowncell>

# <del>The above odd_ID_aa and odd_ID_bb are lists of markers where P0 are aabb and F1 present either aa or bb, while F2 present odd genotypes, which present a</del>

# <codecell>

P0_aabb_2 = []
for i in keys:
    if i.split(',')[1] == 'aabb':
        P0_aabb_2.append(i.split(',')[0])

new_P0_aabb_2 = []
for i in P0_aabb_2:
    new_P0_aabb_2.append([i]+['aa', 'bb', 'ab','ab']+df2[i])
        
# new_P0_aabb = []
# for i in P0_aabb:
#     new_P0_aabb.append([i.split(',')[0]]+['aa', 'bb', 'ab','ab']+df2[i.split(',')[0]])

# <markdowncell>

# new_P0_aabb_2 is what we need to retype all the mis-typed markers with aabb P0 genotype

# <codecell>

# print (
# len(new_P0_aabb),
# len(P0_aabb)
# )

print (
len(new_P0_aabb_2),
len(P0_aabb_2)
)

# <headingcell level=3>

# Now I need to consider the case where P0 are 'aaab' or 'abaa'

# <markdowncell>

# I need to first identify the markers where ther are F2s with 'bb', then I need to run a LRT to check if we can exclude that the actual allele frequency is 50% a and 50% b

# <codecell>

#P0_aaab = []
#for i in keys:
#    if i.split(',')[1] == 'aaab':
#        P0_aaab.append(i)
        
#P0_abaa = []
#for i in keys:
#    if i.split(',')[1] == 'abaa':
#        P0_abaa.append(i)

P0_3a1b = []
for i in keys:
    if i.split(',')[1] == 'abaa': # P0 is 'abaa'
        if (i.split(',')[2]+i.split(',')[3]) != 'abab': #F1 is not 'abab'
            if 'bb' in df2[i.split(',')[0]]:
                P0_3a1b.append(i)
    elif i.split(',')[1] == 'aaab':
        if (i.split(',')[2]+i.split(',')[3]) != 'abab': # P0 is 'abaa'
            if 'bb' in df2[i.split(',')[0]]: # F1 is not 'abab'
                P0_3a1b.append(i)

# <codecell>

#P0_1a3b = []
#for i in keys:
#    if i.split(',')[1] == 'abbb': # P0 is 'abaa'
#        if (i.split(',')[2]+i.split(',')[3]) != 'abab': #F1 is not 'abab'
#            if 'bb' in df2[i.split(',')[0]]:
#                P0_3a1b.append(i)
#    elif i.split(',')[1] == 'aaab':
#        if (i.split(',')[2]+i.split(',')[3]) != 'abab': # P0 is 'abaa'
#            if 'bb' in df2[i.split(',')[0]]: # F1 is not 'abab'
#                P0_3a1b.append(i)

# <codecell>

def lrt(input):
    d = count_allele(input)
    a = d['a']
    b = d['b']
    freq_a = float(a)/(a+b)
    freq_b = 1-freq_a
    MLE_ab = (freq_a**a)*(freq_b**b)
    MLE_075 = (.75**a)*(.25**b) 
    LRT = 2*(math.log(MLE_ab)-math.log(MLE_075))
    LOD = math.log10(MLE_ab/MLE_075)
    p_val = 1.0/(10**(LOD))
#    out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
#    ls.append(out)
#  return 'Marker'+'\tLRT\tLOD\tp_val\n'+','.join(ls)[:-1].replace('\n,','\n') 
    return p_val

ls_ac = []
ls_nac = []

for i in P0_3a1b:
    if lrt(i.split(',')[0]) > 0.05:    
        ls_ac.append(i.split(',')[0])  #ls_ac are the ones that have been accurately typed as 'abaa' or 'aaab' as F1
    else:
        ls_nac.append(i.split(',')[0]) #ls_nac are the ones that have not been accurately typed as 'abaa' or 'aaab' as F1

# <headingcell level=3>

# Then the final edit to retype all the F1s

# <codecell>

#final = []
#for i in ID:
#    if i in new_P0_aabb_2:
#        final.append([i]+['aa', 'bb', 'ab','ab']+df2[i])
#    elif i in ls_nac:
#        final.append(daL[i][:3]+['ab','ab']+df2[i])
#    else:
#        final.append(daL[i])

final = []
for i in ID:
    if i in P0_aabb_2: #this lines fixes a bug, above a had 'if i in new_P0_aabb_2:'
        final.append([i]+['aa', 'bb', 'ab','ab']+df2[i])
    elif i in ls_nac:
        final.append(daL[i][:3]+['ab','ab']+df2[i])
    else:
        final.append(daL[i])

# <codecell>

lgot = []
for i in go1t[:10]:
    lgot.append(list(i))

# <codecell>

final2 = lgot + final

# <codecell>

finalt = zip(*final2)
fin = [ ','.join(list(i)+['\n']) for i in finalt ]
finj = ','.join(fin).replace(',\n','\n').replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/n-inf_fam_1.csv', 'w')
z.write(finj)
z.close()

# <markdowncell>

# <del>Now I need to carefully take into account all the possible F1 scenarios</del>

# <codecell>

#p0aaab_f1aaaa = []
#p0aaab_f1bbbb = []
#p0aaab_f1aabb = []
#p0aaab_f1bbaa = []
#p0aaab_f1aaab = []
#p0aaab_f1abaa = []
#p0aaab_f1abab = []
#p0aaab_f1abbb = []
#p0aaab_f1bbab = []

#for i in P0_aaab:
#    if df1[i.split(',')[0]] == 'aaaa':
#        p0aaab_f1aaaa.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'bbbb':
#        p0aaab_f1bbbb.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'aabb':
#        p0aaab_f1aabb.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'bbaa':
#        p0aaab_f1bbaa.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'aaab':
#        p0aaab_f1aaab.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'abaa':
#        p0aaab_f1abaa.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'abab':
#        p0aaab_f1abab.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'abbb':
#        p0aaab_f1abbb.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'bbab':
#        p0aaab_f1bbab.append(i.split(',')[0])
        
        
#p0abaa_f1aaaa = []
#p0abaa_f1bbbb = []
#p0abaa_f1aabb = []
#p0abaa_f1bbaa = []
#p0abaa_f1aaab = []
#p0abaa_f1abaa = []
#p0abaa_f1abab = []
#p0abaa_f1abbb = []
#p0abaa_f1bbab = []

#for i in P0_abaa:
#    if df1[i.split(',')[0]] == 'aaaa':
#        p0abaa_f1aaaa.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'bbbb':
#        p0abaa_f1bbbb.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'aabb':
#        p0abaa_f1aabb.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'bbaa':
#        p0abaa_f1bbaa.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'aaab':
#        p0abaa_f1aaab.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'abaa':
#        p0abaa_f1abaa.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'abab':
#        p0abaa_f1abab.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'abbb':
#        p0abaa_f1abbb.append(i.split(',')[0])
#    elif df1[i.split(',')[0]] == 'bbab':
#        p0abaa_f1bbab.append(i.split(',')[0])

# <codecell>

#print (
# len(p0aaab_f1aaaa),
# len(p0aaab_f1bbbb),
# len(p0aaab_f1aabb),
# len(p0aaab_f1bbaa),
# len(p0aaab_f1aaab),
# len(p0aaab_f1abaa),
# len(p0aaab_f1abab),
# len(p0aaab_f1abbb),
# len(p0aaab_f1bbab),
# )

# <codecell>

#print (
# len(p0abaa_f1aaaa),
# len(p0abaa_f1bbbb),
# len(p0abaa_f1aabb),
# len(p0abaa_f1bbaa),
# len(p0abaa_f1aaab),
# len(p0abaa_f1abaa),
# len(p0abaa_f1abab),
# len(p0abaa_f1abbb),
# len(p0abaa_f1bbab),
# )

# <codecell>

# odd_ID_p0aaab_f1aaaa = []
# odd_ID_p0aaab_f1bbbb = []
# odd_ID_p0aaab_f1aabb = []
# odd_ID_p0aaab_f1bbaa = []
# odd_ID_p0aaab_f1aaab = []
# odd_ID_p0aaab_f1abaa = []
# odd_ID_p0aaab_f1abab = []
# odd_ID_p0aaab_f1abbb = []
# odd_ID_p0aaab_f1bbab = []

# for i in p0aaab_f1aaaa:
#     if 'bb' in df2[i]:
#         odd_ID_p0aaab_f1aaaa.append(i.split(',')[0])
#     elif 'ab' in df2[i]:
#         odd_ID_p0aaab_f1aaaa.append(i.split(',')[0])    #These F1 genotypes now need to be changed
        
# for i in p0aaab_f1aaab:
#     if 'bb' in df2[i]:
#         odd_ID_p0aaab_f1aaab.append(i.split(',')[0])
        
# for i in p0aaab_f1abaa:
#     if 'bb' in df2[i]:
#         odd_ID_p0aaab_f1abaa.append(i.split(',')[0])        

# for i in p0aaab_f1bbab:
#     if 'aa' in df2[i]:
#         odd_ID_p0aaab_f1bbab.append(i.split(',')[0])        
        
# odd_ID_p0abaa_f1aaaa = []
# odd_ID_p0abaa_f1bbbb = []
# odd_ID_p0abaa_f1aabb = []
# odd_ID_p0abaa_f1bbaa = []
# odd_ID_p0abaa_f1aaab = []
# odd_ID_p0abaa_f1abaa = []
# odd_ID_p0abaa_f1abab = []
# odd_ID_p0abaa_f1abbb = []
# odd_ID_p0abaa_f1bbab = []

# for i in p0abaa_f1aaaa:
#     if 'bb' in df2[i]:
#         odd_ID_p0abaa_f1aaaa.append(i.split(',')[0])
#     elif 'ab' in df2[i]:
#         odd_ID_p0abaa_f1aaaa.append(i.split(',')[0])    

# <codecell>

# odd_ID_p0abaa_f1bbab

# <codecell>

# odd_P0aaab = []
# for i in P0_aaab:
#    if 'bb' in df2[i]:
#         odd_P0aaab.append(i)
        
# odd_P0abaa = []
# for i in P0_abaa:
#     if 'bb' in df2[i]:
#         odd_P0abaa.append(i)

# <codecell>

# df1f2['25984']

# <codecell>

# keys[:10]

# <codecell>


