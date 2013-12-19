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


