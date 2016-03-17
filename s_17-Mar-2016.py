import numpy as np
from scipy.stats.stats import pearsonr
from scipy import stats
from scipy import stats, integrate
import matplotlib.pyplot as plt
%matplotlib inline
#import seaborn as sns

rna = open('/beegfs/group_dv/home/DValenzano/uBiome/data/rnaseq_fpkm_genes_sorted.csv', 'rU').read()
otu = open('/beegfs/group_dv/home/DValenzano/uBiome/data/rnaseq_merged_otu_table_sorted.csv','rU').read()

rnal = [i.split(',') for i in rna.split('\n')] #that's a "l" as in "L"
otul = [i.split(',') for i in otu.split('\n')]

rnat = [ list(i) for i in zip(*rnal)]
otut = [list(i) for i in zip(*otul) ]

rnat_z = [ map(float, i[1:]) for i in rnat[1:] if i.count('0') < 8]
otut_z = [ map(float, i[1:]) for i in otut[1:] if i.count('0.0') < 8]

# rnat_z1 = [ map(float, i[1:]) for i in rnat[1:] if i.count('0') < 5]
# otut_z1 = [ map(float, i[1:]) for i in otut[1:] if i.count('0') < 5]

# rna_key1 = [i[0] for i in rnat[1:] if i.count('0') < 5]
# otu_key1 = [ i[0] for i in otut[1:] if i.count('0') < 5]

# rna_value1 = rnat_z1
# otu_value1 = otut_z1

# rna_d1 = dict(zip(rna_key1, rna_value1))
# otu_d1 = dict(zip(otu_key1, otu_value1))

rna_key = [i[0] for i in rnat[1:] if i.count('0') < 8]
otu_key = [ i[0] for i in otut[1:] if i.count('0.0') < 8]

rna_value = rnat_z
otu_value = otut_z

rna_d = dict(zip(rna_key, rna_value))
otu_d = dict(zip(otu_key, otu_value))

def loop_one(m1,otu): # this returns all the correlation coefficients between m1 and a given otu (otu)
    ls = []
    for i in m1:
        ls.append(stats.linregress(i, otu))    #this function returns slope, intercept, r_value, p_value, std_err
    return ','.join(map(str, ls))+'\n'

def loop_two(m1, m2):
    ls = []
    for j in m2:
        ls.append(loop_one(m1, j))
    return ','.join(ls).replace('\n,','\n')

fpkmvsotu = loop_two(rnat_z, otut_z)

z = open('/beegfs/group_dv/home/DValenzano/uBiome/data/regr.csv','w')
z.write(fpkmvsotu)
z.close()

#fpkmvsotu = open('/beegfs/group_dv/home/DValenzano/uBiome/data/regr.csv','rU').read()

class reg(object):
    
    """
    This class uses as input a linear regression file obtained by the loop_two function and returns 
    regression tables and plots, given specific parameteres, such as R-squared value, p-value, OTU or 
    transcript
    """
    
    version = 0.1
    
    def __init__(self, inp):
        self.inp = inp 
        self.inp2 = [ i.split('(') for i in self.inp.split('\n')[:-1]] 
    
        def loop1(inp, n):
            ls = []
            for i in inp[1:]:
                ls.append(i.split(',')[n])
            return ','.join(ls).replace(')', '')
        def loop2(inp, n):
            ls = []
            for i in inp:
                ls.append(loop1(i, n))
            return ls
       
        self.slope =  [map(float, i.split(',')) for i in loop2(self.inp2, 0)]
        self.intercept = [map(float, i.split(',')) for i in loop2(self.inp2, 1)]
        self.rvalue = [map(float, i.split(',')) for i in loop2(self.inp2, 2)]
        self.rsquare = [ map(lambda x: x**2, i) for i in self.rvalue]
        self.pvalue = [map(float, i.split(',')) for i in loop2(self.inp2, 3)]
        self.stderr = [map(float, i.split(',')) for i in loop2(self.inp2, 4)  ]     
        
        
def filt(inp, thr, sign): #filter p-values, r-values and so forth based on a chosen threshold
    ar = np.array(inp)
    ls = []
    if sign == '>':
        ls = zip(*np.where(ar > thr))
    elif sign == '<':
        ls = zip(*np.where(ar < thr))
    else: 
        print "Error: check your input file"
    return ls

rf = reg(fpkmvsotu)

Rpval = filt(rf.pvalue, 0.00001, '<')

P = [otu_key[i[0]]+','+rna_key[i[1]]  for i in Rpval ]
