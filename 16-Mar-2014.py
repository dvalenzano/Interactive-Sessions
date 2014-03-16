# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Here I generate a script that saves a color ped file for family 7

# <codecell>

import sys
inp = raw_input('What family would you like to analyze?\n')
inp2 = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_%s.csv' % inp
fam = open(inp2, 'rU').read()
fams = fam.split('\n')[:-1]
fams2 = [','.join(i.split(',')[:5]) +','+ i.split(',')[6]+','+','.join(i.split(',')[10:]) for i in fams[1:]]

# <codecell>

def blast(input):
    ls = []
    for i in input.split(',')[6:]:
        if len(i)== 2:
            ls.append(i[0]+','+i[1])
        else:
            ls.append(i+','+i)
    return ','.join(ls)+'\n'

# <codecell>

#[i for i in  [ ','.join(i.split(',')[:6])+','+blast(i) for i in fams2 ] if i.split(',')[5]!='0']

# <codecell>

pedfam = ','.join([ ','.join(i.split(',')[:6])+','+blast(i) for i in fams2 ][:4]+[i for i in  [ ','.join(i.split(',')[:6])+','+blast(i) for i in fams2 ][4:] if i.split(',')[5]!='0']).replace('\n,','\n').replace(',','\t')
out0 = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/color/inf-fam_%s_c.ped' % (inp, inp)
z = open(out0,'w')
z.write(pedfam)
z.close()

# <markdowncell>

# Here follows a script that isolates overlapping survival QTL in association to sex in family 7 and 14 for cross Go

# <codecell>

from sets import Set
lin_7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/inf-fam_7as.assoc.linear', 'rU').read()
lin_14 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/inf-fam_14as.assoc.linear', 'rU').read()

# <codecell>

f7_01 = [lin_7.split('\n')[0]]+[i for i in [i.split() for i in lin_7.split('\n')[1:-1] if i.split()[-1] != 'NA' ] if float(i[-1]) < 0.01  ]
f14_01 = [lin_14.split('\n')[0]]+[ i for i in [i.split() for i in lin_14.split('\n')[1:-1] if i.split()[-1] != 'NA' ] if float(i[-1]) < 0.01 ]

f7_05 = [lin_7.split('\n')[0]]+[i for i in [i.split() for i in lin_7.split('\n')[1:-1] if i.split()[-1] != 'NA' ] if float(i[-1]) < 0.05  ]
f14_05 = [lin_14.split('\n')[0]]+[ i for i in [i.split() for i in lin_14.split('\n')[1:-1] if i.split()[-1] != 'NA' ] if float(i[-1]) < 0.05 ]

# <codecell>

#f7sig_01 = [i for i in f7[1:] if float(i[-1]) < 0.01]
#f14sig_01 = [i for i in f14[1:] if float(i[-1]) < 0.01]
f7s_01 = Set([i[1] for i in f7_01 ])
f14s_01 = Set([i[1] for i in f14_01 ])
p_01 = f7s_01 & f14s_01

#f7sig_05 = [i for i in f7[1:] if float(i[-1]) < 0.05]
#f14sig_05 = [i for i in f14[1:] if float(i[-1]) < 0.05]
f7s_05 = Set([i[1] for i in f7_05 ])
f14s_05 = Set([i[1] for i in f14_05 ])
p_05 = f7s_05 & f14s_05

# <codecell>

print "markers with p-val < 0.01 in family 7: " + str(len(f7_01)) + "\nmarkers with p-val < 0.01 in family 14: " + str(len(f14_01)) + "\noverlapping markers with p-val < 0.01 between family 7 and family 14: " + str(len(p_01)) + "\nmarkers with p-val < 0.05 in family 7: " + str(len(f7_05)) + "\nmarkers with p-val < 0.05 in family 14: " + str(len(f14_05)) + "\noverlapping markers with p-val < 0.05 between family 7 and family 14: " + str(len(p_05))

# <markdowncell>

# Now I need to test differences in survival between males and females for family 7 and 14

# <codecell>

f7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/inf-fam_7.ped', 'rU').read()
f7s = [i.split() for i in f7.split('\n')[:-1]]

f14 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/inf-fam_14.ped', 'rU').read()
f14s = [i.split() for i in f14.split('\n')[:-1]]

f1_1 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/inf-fam_1.1.ped', 'rU').read()
f1_1s = [i.split() for i in f1_1.split('\n')[:-1]]

f8 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/inf-fam_8.ped', 'rU').read()
f8s = [i.split() for i in f1_1.split('\n')[:-1]]

# <codecell>

f7f = [ float(i[5]) for i in f7s if i[4]=='2']  
f7m = [ float(i[5]) for i in f7s if i[4]=='1'] 

f14f = [ float(i[5]) for i in f14s if i[4]=='2']  
f14m = [ float(i[5]) for i in f14s if i[4]=='1'] 

f1_1f = [ float(i[5]) for i in f1_1s if i[4]=='2']  
f1_1m = [ float(i[5]) for i in f1_1s if i[4]=='1'] 

f8f = [ float(i[5]) for i in f8s if i[4]=='2']  
f8m = [ float(i[5]) for i in f8s if i[4]=='1'] 

# <codecell>

from scipy import stats
tt = stats.ttest_1samp(f7f, f7m)

# <codecell>

f7_2 = 'sex,age\n'+','.join([ ','.join(i.split()[4:6])+'\n' for i in f7.split('\n')[4:-1]]).replace('\n,','\n')

f14_2 = 'sex,age\n'+','.join([ ','.join(i.split()[4:6])+'\n' for i in f14.split('\n')[4:-1]]).replace('\n,','\n')

f1_1_2 = 'sex,age\n'+','.join([ ','.join(i.split()[4:6])+'\n' for i in f1_1.split('\n')[4:-1]]).replace('\n,','\n')

f8_2 = 'sex,age\n'+','.join([ ','.join(i.split()[4:6])+'\n' for i in f8.split('\n')[4:-1]]).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/subdir/sex_7.csv', 'w')
z.write(f7_2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/subdir/sex_14.csv', 'w')
z.write(f14_2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/subdir/sex_1_1.csv', 'w')
z.write(f1_1_2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/subdir/sex_8.csv', 'w')
z.write(f8_2)
z.close()

# <markdowncell>

# Next goal: test overlap of sex-specific surv-QTL in 4 families

# <codecell>

ff7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/fem/fam_7f_sqtl.assoc.linear', 'rU').read()
fm7 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_7/mal/fam_7m_sqtl.assoc.linear', 'rU').read()

ff14 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/fem/fam_14f_sqtl.assoc.linear', 'rU').read()
fm14 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_14/mal/fam_14m_sqtl.assoc.linear', 'rU').read()

ff8 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/fem/fam_8f_sqtl.assoc.linear', 'rU').read()
fm8 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_8/mal/fam_8m_sqtl.assoc.linear', 'rU').read()

ff1_1 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/fem/fam_1.1f_sqtl.assoc.linear', 'rU').read()
fm1_1 = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_1.1/mal/fam_1.1m_sqtl.assoc.linear', 'rU').read()

# <codecell>

ff7s = [ i[-1] for i in [i.split() for i in ff7.split('\n')[:-1]][1:] if i[-1] != 'NA' ]
fm7s = [ i[-1] for i in [i.split() for i in fm7.split('\n')[:-1]][1:] if i[-1] != 'NA' ]
ff14s = [ i[-1] for i in [i.split() for i in ff14.split('\n')[:-1]][1:] if i[-1] != 'NA' ]
fm14s = [ i[-1] for i in [i.split() for i in fm14.split('\n')[:-1]][1:] if i[-1] != 'NA' ]
ff8s = [ i[-1] for i in [i.split() for i in ff8.split('\n')[:-1]][1:] if i[-1] != 'NA' ]
fm8s = [ i[-1] for i in [i.split() for i in fm8.split('\n')[:-1]][1:] if i[-1] != 'NA' ]
ff1_1s = [ i[-1] for i in [i.split() for i in ff1_1.split('\n')[:-1]][1:] if i[-1] != 'NA' ]
fm1_1s = [ i[-1] for i in [i.split() for i in fm1_1.split('\n')[:-1]][1:] if i[-1] != 'NA' ]

# <codecell>

p_val= 'p-val,'+','.join(ff7s) + ','+','.join(fm7s) + ','+ ','.join(ff14s) +','+ ','.join(fm14s)+ ','+','.join(ff8s) + ','+ ','.join(fm8s) +','+ ','.join(ff1_1s)+','+ ','.join(fm1_1s)

# <codecell>

group = 'group,'+(len(ff7s)*'f7,')[:-1] + ','+(len(fm7s)*'m7,')[:-1]+','+(len(ff14s)*'f14,')[:-1] + ','+(len(fm14s)*'m14,')[:-1]+','+(len(ff8s)*'f8,')[:-1] + ','+(len(fm8s)*'m8,')[:-1]+','+(len(ff1_1s)*'f1.1,')[:-1] + ','+(len(fm1_1s)*'m1.1,')[:-1]

# <codecell>

fams = p_val+'\n'+group

# <codecell>

famst = ','.join([ ','.join(list(i)+['\n']).replace(',\n','\n') for i in zip(*[i.split(',') for i in fams.split('\n')])]).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fams-sqtl.csv', 'w')
z.write(famst)
z.close()

# <codecell>


