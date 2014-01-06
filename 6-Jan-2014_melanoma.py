import random
import sys
sys.path.append('/Volumes/group_dv/group/files_for_melanoma_qtl/lrt_melanoma.py')

# <codecell>

r_btj = open('/Volumes/group_dv/group/files_for_melanoma_qtl/red-big.csv', 'rU').read()
big = bigmatrix = open('/Volumes/group_dv/group/tmp/Go_allfam_2.csv', 'rU').read()
bigs = big.split('\n')

# <codecell>

r_btjs = r_btj.split('\n')
r_btjt = zip(*[ i.split(',') for i in r_btj.split('\n') ])

# <codecell>

r_t = r_btjt
ID = list(r_t[0])[1:]
keys = []
values = []
d = {}
for i in r_btjs:
    keys.append(i.split(',')[0])
    values.append(i.split(',')[1:])
    d = dict(zip(keys, values)) 

# <codecell>

def bs2(input, size, iter, matrix): #input is the input file, like a list of items we want to bootstrap; size is the size of each bootstrap; iter is the number of iterations we run
# We added "matrix" in the parameters of bs2 function. This allows us to select which matrix we want to use. 
    ls = []
    ls2 = []
    ls3 = []
    ls4 = []
    for i in range(iter):
        ls.append(random.sample(input, size))
    for n in ls:
        for j in n:
            ls2.append(j+','+','.join(d[j])+'\n')
        ls3.append(matrix[0]+'\n'+','.join(ls2).replace('\n,','\n'))
#    return ls3
    for p in ls3[:-1]:
        ls4.append(p+'\p')
    return ','.join(ls4).replace('\p,','\p')

# <codecell>

def bs_0(input, size, iter): #, iter, matrix): #input is the input file, like a list of items we want to bootstrap; size is the size of each bootstrap; iter is the number of iterations we run
# We added "matrix" in the parameters of bs2 function. This allows us to select which matrix we want to use. 
    ls = []
    ls2 = []
    ls3 = []
    ls4 = []
    for i in range(iter):
        ls.append(random.sample(input, size))
    return ls

# <codecell>

boot_0 = bs_0(ID, 18, 50) 

# <codecell>

def bs_1(input, matrix):
    ls = []
    ls2 = []
    for i in input:
        for j in i:
            ls.append(j+','+','.join(d[j])+'\n')
        ls2.append(','.join(ls))
    return ','.join(ls2)        
            
#    return matrix[0]+'\n'+','.join(ls).replace('\n,','\n')

# <codecell>

boot_1 = bs_1(boot_0, r_btjs)

# <codecell>

z= open('/Users/DValenzano/Desktop/prova.csv', 'w')
z.write(boot_1)
z.close()

# <codecell>

boot_m = bs2(ID, 18, 50, r_btjs)

# <codecell>

boot_m.split('\p')[0][:100]

# <codecell>

attempt = lrt.out(boot_m.split('\p')[0])

