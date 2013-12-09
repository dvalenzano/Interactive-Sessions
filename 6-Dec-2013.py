## As always, all this scripts are saved in my [github](https://github.com/dvalenzano) personal page

## Goal: to filter for mis-coded F1/F2 genotypes, derived from situations like the following:

## P0: aaxbb
## F1: *bb*
## F2: *aa*

## P0: aaxbb
## F1: *aa*
## F2: *bb*

## Rationale: if there are 'bb' or 'aa' genotypes in the F1 from aabb P0 parents, then I do not expect to have 'aa' and 'bb' genotypes respectively in the F2 genotypes. So what do I do if I do have 'aa' in an F2 from a 'bbab' F1 genotype? Here's the thing: I can use likelyhood ratio test.   
## Example: P0= aabb; F1=abaa; and I do find one F2 with a 'bb' genotype, which is not expected given the parents' genotypes. Now it could be that either one of the F1 is mis-typed, or that the F2 is mistyped. How do I know what's wrong? Given abaa F1, I expect to have 3a:1b in the F2. If, in fact, the F2 have a 3a:1b ratio, than most likely the 'bb' F2 is just mis-typed and I will correct it to 'ab'. However, if the allele frequency in the F2 is 1a:1b, then most likely one F1 genotype is wrong, and rather than being aaab, or abaa, it's actually abab. 

## Similar approach applies for the following genotypes:

## P0: aaxab
## F1: aaxab
## F2: *bb*

## P0: aaxab
## F1: *bb*
## F2: *aa* 


## So here are the steps and the pseudocode:

## For each family
## Find the mismatching F1-F2 genotypes  
## Save the IDs  
## measure the allele frequency for these markers 
## if the allele frequency is compatible with the F1 model (run likelihood ratio test), then modify the F2 genotype  
## elsif the allele frequency is incompatible with the F1 model (run likelihood ratio test), then re-type F1 alleles 
# <codecell>

go1 = open('/Users/dvalenzano/Downloads/inf_famGo/inf_fam_1.csv', 'rU').read()

go1t = zip(*[ i.split(',')  for i in go1.split('\n')[:-1]])

ID = []
p0 = []
f1 = []
f2 = []
p0f1 = []
f1f2 = []
keys = []
for i in go1t[10:]:
    ID.append(i[0])
    p0.append(i[1]+i[2])
    f1.append(i[3]+i[4])
    p0f1.append(i[1]+i[2]+i[3]+i[4])
    f2.append(list(i[5:]))
    f1f2.append(list(i[3:]))
    keys.append(i[0]+','+i[1]+i[2]+','+i[3]+','+i[4])

# <codecell>

d = dict(zip(keys, f2))
df2 = dict(zip(ID, f2))
df1f2 = dict(zip(ID, f1f2))
df1 = dict(zip(ID, f1))

# <codecell>

P0_aabb = []
for i in keys:
    if i.split(',')[1] == 'aabb':
        P0_aabb.append(i)

# <codecell>

oddF1_aa = []
oddF1_bb = []
for i in P0_aabb:
    if i.split(',')[2] == 'aa':
        oddF1_aa.append(i)
    elif i.split(',')[3] == 'aa':
        oddF1_aa.append(i)
    elif i.split(',')[2] == 'bb':
        oddF1_bb.append(i)
    elif i.split(',')[3] == 'bb':
        oddF1_bb.append(i)

# <codecell>

# Now I need to find the markers where - in oddF1_bb - there are F2 with 'aa' genotypes, and in oddF1_aa, there are F2 with 'bb' genotypes. 

odd_ID_aa = []
for i in oddF1_aa:
    if 'bb' in d[i]:
        odd_ID_aa.append(i.split(',')[0])

# <codecell>

# Now I need to consider the case where P0 are 'aaab' or 'abaa'

P0_aaab = []
for i in keys:
    if i.split(',')[1] == 'aaab':
        P0_aaab.append(i)
        
P0_abaa = []
for i in keys:
    if i.split(',')[1] == 'abaa':
        P0_abaa.append(i)

# <codecell>

p0aaab_f1aaaa = []
p0aaab_f1bbbb = []
p0aaab_f1aabb = []
p0aaab_f1bbaa = []
p0aaab_f1aaab = []
p0aaab_f1abaa = []
p0aaab_f1abab = []
p0aaab_f1abbb = []
p0aaab_f1bbab = []

for i in P0_aaab:
    if df1[i.split(',')[0]] == 'aaaa':
        p0aaab_f1aaaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbbb':
        p0aaab_f1bbbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aabb':
        p0aaab_f1aabb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbaa':
        p0aaab_f1bbaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aaab':
        p0aaab_f1aaab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abaa':
        p0aaab_f1abaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abab':
        p0aaab_f1abab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abbb':
        p0aaab_f1abbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbab':
        p0aaab_f1bbab.append(i.split(',')[0])
        
        
p0abaa_f1aaaa = []
p0abaa_f1bbbb = []
p0abaa_f1aabb = []
p0abaa_f1bbaa = []
p0abaa_f1aaab = []
p0abaa_f1abaa = []
p0abaa_f1abab = []
p0abaa_f1abbb = []
p0abaa_f1bbab = []

for i in P0_abaa:
    if df1[i.split(',')[0]] == 'aaaa':
        p0abaa_f1aaaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbbb':
        p0abaa_f1bbbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aabb':
        p0abaa_f1aabb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbaa':
        p0abaa_f1bbaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'aaab':
        p0abaa_f1aaab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abaa':
        p0abaa_f1abaa.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abab':
        p0abaa_f1abab.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'abbb':
        p0abaa_f1abbb.append(i.split(',')[0])
    elif df1[i.split(',')[0]] == 'bbab':
        p0abaa_f1bbab.append(i.split(',')[0])

# <codecell>

print (
 len(p0aaab_f1aaaa),
 len(p0aaab_f1bbbb),
 len(p0aaab_f1aabb),
 len(p0aaab_f1bbaa),
 len(p0aaab_f1aaab),
 len(p0aaab_f1abaa),
 len(p0aaab_f1abab),
 len(p0aaab_f1abbb),
 len(p0aaab_f1bbab),
 )

print (
 len(p0abaa_f1aaaa),
 len(p0abaa_f1bbbb),
 len(p0abaa_f1aabb),
 len(p0abaa_f1bbaa),
 len(p0abaa_f1aaab),
 len(p0abaa_f1abaa),
 len(p0abaa_f1abab),
 len(p0abaa_f1abbb),
 len(p0abaa_f1bbab),
 )

# <codecell>

odd_ID_p0aaab_f1aaaa = []
odd_ID_p0aaab_f1bbbb = []
odd_ID_p0aaab_f1aabb = []
odd_ID_p0aaab_f1bbaa = []
odd_ID_p0aaab_f1aaab = []
odd_ID_p0aaab_f1abaa = []
odd_ID_p0aaab_f1abab = []
odd_ID_p0aaab_f1abbb = []
odd_ID_p0aaab_f1bbab = []

for i in p0aaab_f1aaaa:
    if 'bb' in df2[i]:
        odd_ID_p0aaab_f1aaaa.append(i.split(',')[0])
    elif 'ab' in df2[i]:
        odd_ID_p0aaab_f1aaaa.append(i.split(',')[0])    #These F1 genotypes now need to be changed
        
for i in p0aaab_f1bbbb:
    if 'aa' in df2[i]:
        odd_ID_p0aaab_f1bbbb.append(i.split(',')[0])
    elif 'ab' in df2[i]:
        odd_ID_p0aaab_f1bbbb.append(i.split(',')[0])       
        
for i in p0aaab_f1aaab:
    if 'bb' in df2[i]:
        odd_ID_p0aaab_f1aaab.append(i.split(',')[0])
        
for i in p0aaab_f1abaa:
    if 'bb' in df2[i]:
        odd_ID_p0aaab_f1abaa.append(i.split(',')[0])        

for i in p0aaab_f1bbab:
    if 'aa' in df2[i]:
        odd_ID_p0aaab_f1bbab.append(i.split(',')[0])        
        
odd_ID_p0abaa_f1aaaa = []
odd_ID_p0abaa_f1bbbb = []
odd_ID_p0abaa_f1aabb = []
odd_ID_p0abaa_f1bbaa = []
odd_ID_p0abaa_f1aaab = []
odd_ID_p0abaa_f1abaa = []
odd_ID_p0abaa_f1abab = []
odd_ID_p0abaa_f1abbb = []
odd_ID_p0abaa_f1bbab = []

for i in p0abaa_f1aaaa:
    if 'bb' in df2[i]:
        odd_ID_p0abaa_f1aaaa.append(i.split(',')[0]) #These F1 genotypes now need to be changed
    elif 'ab' in df2[i]:
        odd_ID_p0abaa_f1aaaa.append(i.split(',')[0])  
        
for i in p0abaa_f1bbbb:
    if 'aa' in df2[i]:
        odd_ID_p0abaa_f1bbbb.append(i.split(',')[0])
    elif 'ab' in df2[i]:
        odd_ID_p0abaa_f1bbbb.append(i.split(',')[0])         
        
for i in p0abaa_f1aaab:
    if 'bb' in df2[i]:
        odd_ID_p0abaa_f1aaab.append(i.split(',')[0])

# <codecell>

odd_ID_p0abaa_f1bbbb

# <codecell>

odd_ID_p0abaa_f1bbab

odd_P0aaab = []
for i in P0_aaab:
    if 'bb' in df2[i]:
        odd_P0aaab.append(i)
        
odd_P0abaa = []
for i in P0_abaa:
    if 'bb' in df2[i]:
        odd_P0abaa.append(i)

df1f2['25984']

keys[:10]


