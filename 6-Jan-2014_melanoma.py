import random
import sys
sys.path.append('/Users/dvalenzano/Dropbox/tmp/lrt_melanoma.py')

r_btj = open('/Users/dvalenzano/Dropbox/tmp/red-big.csv', 'rU').read()
big = bigmatrix = open('/Users/dvalenzano/Dropbox/tmp/Go_allfam_2.csv', 'rU').read()
bigs = big.split('\n')

r_btjs = r_btj.split('\n')
r_btjt = zip(*[ i.split(',') for i in r_btj.split('\n') ])

r_t = r_btjt
ID = list(r_t[0])[1:]
keys = []
values = []
d = {}
for i in r_btjs:
    keys.append(i.split(',')[0])
    values.append(i.split(',')[1:])
    d = dict(zip(keys, values)) 
    
def bs_0(input, size, iter): #input is the input file, like a list of items we want to bootstrap; size is the size of each bootstrap; iter is the number of iterations we run

    ls = []
    for i in range(iter):
        ls.append(random.sample(input, size))
    return ls
    
boot_0 = bs_0(ID, 18, 50) 

def bs_1(inp, matrix):
    ls = []
    for i in inp:
        ls.append(i+','+','.join(d[i])+'\n')
    return matrix[0] +'\n'+ ','.join(ls).replace('\n,','\n')[:-1]+'\p'

ls = []
for i in boot_0:
    ls.append(bs_1(i, r_btjs)) # I am calling the second function in this simple loop.

ls2 = ','.join(ls).replace('\p,','\p')[:-1] # I am joining all together in a big string that can be broken down at '\p'

z = open('/Users/dvalenzano/Desktop/prova.csv', 'w')
z.write(ls2)
z.close()

attempt = lrt.out(boot_m.split('\p')[0])
