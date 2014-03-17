# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from sets import Set

ff7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/fem/fam_7f_sqtl.assoc.linear', 'rU').read()
fm7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/mal/fam_7m_sqtl.assoc.linear', 'rU').read()

ff14 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/fem/fam_14f_sqtl.assoc.linear', 'rU').read()
fm14 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/mal/fam_14m_sqtl.assoc.linear', 'rU').read()

ff8 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/fem/fam_8f_sqtl.assoc.linear', 'rU').read()
fm8 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/mal/fam_8m_sqtl.assoc.linear', 'rU').read()

ff1_1 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/fem/fam_1.1f_sqtl.assoc.linear', 'rU').read()
fm1_1 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/mal/fam_1.1m_sqtl.assoc.linear', 'rU').read()

# <codecell>

fams = [7, 14, 8, 1.1]

# <codecell>

def mp(input):
    ls = []
    for i in input.split('\n')[:-1]:
        ls.append(i.split()[1]+','+i.split()[-1]+'\n')
    return ','.join(ls).replace('\n,','\n')

# <codecell>

def td(input):
    keys = []
    values = []
    for i in input.split('\n')[1:-1]: #this removes 'P' and ' '
        keys.append(i.split()[1])
        values.append(i.split()[-1])
    return dict(zip(keys, values))

# <codecell>

pf7 = td(ff7)
pf8 = td(ff8)
pf14 = td(ff14)
pf1_1 = td(ff1_1)

pm7 = td(fm7)
pm8 = td(fm8)
pm14 = td(fm14)
pm1_1 = td(fm1_1)

# <codecell>

sig7f = [i for i in pf7.keys() if pf7[i] != 'NA' and float(pf7[i]) <0.05]
sig8f = [i for i in pf8.keys() if pf8[i] != 'NA' and float(pf8[i]) <0.05]
sig14f = [i for i in pf14.keys() if pf14[i] != 'NA' and float(pf14[i]) <0.05]
sig1_1f = [i for i in pf1_1.keys() if pf1_1[i] != 'NA' and float(pf1_1[i]) <0.05]

# <codecell>

sig7m = [i for i in pm7.keys() if pm7[i] != 'NA' and float(pm7[i]) <0.05]
sig8m = [i for i in pm8.keys() if pm8[i] != 'NA' and float(pm8[i]) <0.05]
sig14m = [i for i in pm14.keys() if pm14[i] != 'NA' and float(pm14[i]) <0.05]
sig1_1m = [i for i in pm1_1.keys() if pm1_1[i] != 'NA' and float(pm1_1[i]) <0.05]

# <markdowncell>

# How many significant markers are shared among all the families?

# <codecell>

intf = Set(sig7f) & Set(sig14f) & Set(sig1_1f) & Set(sig8f)

# <markdowncell>

# Significant and overlapping markers between fam7 and 14 among females:

# <codecell>

print (
"significant markers in fam 7 females: " +  str(len(Set(sig7f))) + "\nsignificant markers in fam 14 females: "+  str(len(Set(sig14f)))
)

# <codecell>

len(Set(sig14f)) #markers significant in fam 14

# <codecell>

len(Set(sig7f) & Set(sig14f))

# <markdowncell>

# Significant overlapping markers between family 7 and 14 among males:

# <codecell>

len(Set(sig7m) & Set(sig14m))

# <codecell>

len(Set(sig7m)) #markers significant in fam 7

# <codecell>

len(Set(sig14m)) #markers significant in fam 14

# <markdowncell>

# Is this significant? First, what is the number of overlapping markers between these two families?

# <codecell>

len(Set(pf7.keys())&Set(pf14.keys()))

# <markdowncell>

# How many significant markers are shared among all the families in males?

# <codecell>

len(Set(sig7m) & Set(sig14m)&Set(sig8m)&Set(sig1_1m))

# <codecell>

len(Set(sig14m) &Set(sig8m))

# <codecell>

','.join(list(Set(sig7m) & Set(sig14m))) #here follow the significant marker with a p-val < 0.05

# <codecell>

sig7m2 = [i for i in pm7.keys() if pm7[i] != 'NA' and float(pm7[i]) <0.01]
sig8m2 = [i for i in pm8.keys() if pm8[i] != 'NA' and float(pm8[i]) <0.01]
sig14m2 = [i for i in pm14.keys() if pm14[i] != 'NA' and float(pm14[i]) <0.01]
sig1_1m2 = [i for i in pm1_1.keys() if pm1_1[i] != 'NA' and float(pm1_1[i]) <0.01]

# <codecell>

len(Set(sig7m2) & Set(sig14m2))

# <markdowncell>

# Now let's try to build a class that does all the work

# <codecell>

#class Handle:
    
#    def __init__(self, fam, sex):
#        self.fam = fam
#        self.sex = sex 
#        self.txt = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fem/fam_%sf_sqtl.assoc.linear' %(self.fam, self.fam)
#        print 'We are analyzing family {}.'.format(self.fam)
    
#    def __str__(self):
#        return 'family {} is now analyzed.'.format(self.fam)
    
#    def mp(self):
#        self.fam = fam
#        self.inp = open(self.txt, 'rU').read()
#        ls = []
#        for i in self.inp.split('\n')[:-1]:
#            ls.append(i.split()[1]+','+i.split()[-1]+'\n')
#        return ','.join(ls).replace('\n,','\n')
    
#    def td(self):
#        keys = []
#        values = []
#        for i in self.inp.split('\n')[:-1]:
#            keys.append(i.split()[1])
#            values.append(i.split()[-1])
#        return dict(zip(keys, values))

# <codecell>


