# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

mqtl = open('/Volumes/TAP/files_for_melanoma_qtl/melanoma_qtl.tsv', 'rU').read()
big = bigmatrix = open('/Volumes/TAP/files_for_melanoma_qtl/Go_allfam_2.csv', 'rU').read()

# <codecell>

mqtls = mqtl.split('\n')
sqtl = []
for i in mqtls[1:]:
    if float(i.split('\t')[2]) > 4:
        sqtl.append(i+'\n')

sqtlj = mqtls[0]+'\n'+','.join(sqtl).replace('\n,','\n')
z = open('/Volumes/TAP/files_for_melanoma_qtl/sqtl.tsv', 'w')
z.write(sqtlj)
z.close()

# <markdowncell>

# sqtl.tsv contains only the markers that have LOD score for melanoma that is higher than 4 

# <markdowncell>

# Next, we need to bootstrap 1000 (as a starter) samples from the original matrix, which contain 18 IDs chosen randomly

# <codecell>

bigs = big.split('\n')
bigt = zip(*[ i.split(',') for i in big.split('\n') ])

# <codecell>

ID = list(bigt[0])

# <codecell>

keys = []
values = []
d = {}
for i in bigs:
    keys.append(i.split(',')[0])
    values.append(i.split(',')[8:])
    d = dict(zip(keys, values)) 

# <codecell>

def bs(input, size, iter): #input is the input file, like a list of items we want to bootstrap; size is the size of each bootstrap; iter is the number of iterations we run
    ls = []
    for i in range(iter):
        ls.append(random.sample(input, size))
    return ls

# <codecell>

def bs2(input, size, iter): #input is the input file, like a list of items we want to bootstrap; size is the size of each bootstrap; iter is the number of iterations we run
    ls = []
    ls2 = []
    ls3 = []
    for i in range(iter):
        ls.append(random.sample(input, size))
    for i in ls:
        for j in i:
            ls2.appen(j+','+','.join(d[j])+'\n')
        
        
       
        ls3.append(bis[0]+'\n'+
        for j in i:
            ls2.append(bigs[0]+'\n'+j+','+','.join(d[j])+'\n')
    return ls2

# <codecell>

one = bs2(ID, 4, 20)

# <codecell>

one = bs(ID, 4, 20)

# <codecell>

bigs[0][:100]

# <codecell>

one[:5]

# <codecell>

len(one[0].split('\n'))

# <codecell>

one[0].split('\n')[-1][:40]

# <codecell>


################################## ################################## ################################## 
##################################           Dec-20-2013              ################################## 
################################## ################################## ##################################  

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

mqtl = open('/Volumes/TAP/files_for_melanoma_qtl/melanoma_qtl.tsv', 'rU').read()
big = bigmatrix = open('/Volumes/TAP/files_for_melanoma_qtl/Go_allfam_2.csv', 'rU').read()

# <codecell>

mqtls = mqtl.split('\n')   #here we are saving the markers that have a lod score higher than 4 in a new file named sqtl
sqtl = []
for i in mqtls[1:]:
    if float(i.split('\t')[2]) > 4:
        sqtl.append(i+'\n')

sqtlj = mqtls[0]+'\n'+','.join(sqtl).replace('\n,','\n')
z = open('/Volumes/TAP/files_for_melanoma_qtl/sqtl.tsv', 'w')
z.write(sqtlj)
z.close()

# <markdowncell>

# sqtl.tsv contains only the markers that have LOD score for melanoma that is higher than 4 

# <markdowncell>

# Next, we need to bootstrap 1000 (as a starter) samples from the original matrix, which contain 18 IDs chosen randomly

# <codecell>

bigs = big.split('\n')
bigt = zip(*[ i.split(',') for i in big.split('\n') ])

# <codecell>

ID = list(bigt[0])

# <codecell>

keys = []
values = []
d = {}
for i in bigs:
    keys.append(i.split(',')[0])
    values.append(i.split(',')[8:])
    d = dict(zip(keys, values)) 

# <codecell>

def bs(input, size, iter): #input is the input file, like a list of items we want to bootstrap; size is the size of each bootstrap; iter is the number of iterations we run
    ls = []
    for i in range(iter):
        ls.append(random.sample(input, size))
    return ls

# <codecell>

def bs2(input, size, iter): #input is the input file, like a list of items we want to bootstrap; size is the size of each bootstrap; iter is the number of iterations we run
    ls = []
    ls2 = []
    ls3 = []
    ls4 = []
    for i in range(iter):
        ls.append(random.sample(input, size))
    for n in ls:
        for j in n:
            ls2.append(j+','+','.join(d[j])+'\n')
        ls3.append(bigs[0]+'\n'+','.join(ls2).replace('\n,','\n'))
#    return ls3
    for p in ls3[:-1]:
        ls4.append(p+'\p')
    return ','.join(ls4).replace('\p,','\p')

# <codecell>

one = bs2(ID, 4, 20)

# <markdowncell>

# Todo: generate a matrix with only markers that are significantly associated to melanoma in the first analysis

# <codecell>

sID = open('/Volumes/group_dv/group/files_for_melanoma_qtl/lod4_marker_only.csv', 'rU').read()

# <codecell>

sID = sID.replace(':','')

# <codecell>

sIDl = sID.split(',')

# <codecell>

big_IDs = list(bigt[0]+['\n'])

# <codecell>

r_big = [','.join(big_IDs)]
for i in bigt[7:]:
    if i[0] in sIDl:
        r_big.append(','.join(list(i)+['\n']).replace(',\n','\n'))

# <codecell>

r_bigj = ','.join(r_big).replace('\n,','\n')[:-1] #this is the matrix with only the significant markers - needs to be transposed

r_bt = zip(*[ i.split(',')  for i in r_bigj.split('\n')])

# <codecell>

r_btj = ','.join([  (','.join(list(i))+'\n').replace(',\n','\n') for i in r_bt]).replace('\n,','\n')[:-1]

# <codecell>

z = open('/Volumes/group_dv/group/files_for_melanoma_qtl/red-big.csv', 'w')
z.write(r_btj)
z.close()

# <markdowncell>

# Now we want to create a new set of matrices generated by sampling randomly 18 individuals from the r_btj matrix - this will allow us to calculate  
# LRT for each of these and have eventually a LRT statistics distribution for each marker. If a marker is likely to have high LOD scores on the  
# different random matrices, then it's less likely to be significantly associated to melanoma

# <codecell>

r_btjs = r_btj.split('\n')
r_btjt = zip(*[ i.split(',') for i in r_btj.split('\n') ])

# <codecell>

r_t = r_btjt
ID = list(r_t[0])
keys = []
values = []
d = {}
for i in r_btjs:
    keys.append(i.split(',')[0])
    values.append(i.split(',')[1:])
    d = dict(zip(keys, values)) 

# <codecell>

boot_m = bs2(ID, 18, 50)

# <codecell>

boot_m.count('\\p')

# <codecell>

boot_m[-956060:-955860]

# <codecell>




