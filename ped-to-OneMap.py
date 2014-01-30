# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

f7 = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_7.csv', 'rU').read()

# <codecell>

f7s = zip(*[ i.split(',') for i in f7.split('\n')[:-2]])

# <markdowncell>

# What I want is marker ID, F1 genotypes, F2 genotypes

# <codecell>

ls = []
for i in f7s[10:]:
    ls.append([i[0]]+[i[3]+'-'+i[4]]+list(i[5:]))

# <codecell>

lz = []
for i in ls:
    lz.append(','.join(i)+'\n')

# <codecell>

lz2 = ','.join(lz).replace('\n,','\n')

# <codecell>

#d = {}
#d['ab-ab'] = 'B2.6'
#d['aa-ab'] = 'D2.15'
#d['ab-aa'] = 'D1.10'

# <codecell>

#lz3 = [ i.split(',')[0]+','+d[i.split(',')[1]]+','+','.join(i.split(',')[2:]) +'\n' for i in lz2.split('\n')[:-1]]

# <codecell>

lw = [i.split(',')[1] for i in lz2.split('\n')[:-1]]

# <codecell>

# first I'll check the F1 genotypes
lx = []
for i in lw:
    if i not in lx:
        lx.append(i)

# <codecell>

lx

# <codecell>

# Genotype table:
d = {}
d['ab-ab'] = 'B3.7'
d['aa-ab'] = 'D2.15'
d['ab-aa'] = 'D1.10'

# <codecell>

d.items()

# <codecell>

lz3 = []
for i in lz2.split('\n')[:-1]:
    lz3.append(i.split(','))

# <codecell>

lz4 = []
for i in lz3:
    lz4.append('*'+i[0]+'\t'+d[i[1]]+'\t'+','.join(i[2:]).replace('0','-')+'\n')
    

# <codecell>

lz5 = ','.join(lz4).replace('\n,','\n').replace('aa','a').replace('bb','b')

# <codecell>

len(lz5.split('\n')[0].split(','))

# <codecell>

fin = str(len(lz5.split('\n')[0].split(',')))+' '+str(len(lz5.split('\n')[:-1]))+'\n'+lz5

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/fam_7.Onemap.txt', 'w')
z.write(fin)
z.close()


#######################################################################################################
#######################                       ITERATIVELY                       #######################
#######################################################################################################


input = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-list.txt', 'rU').read() #inferred-list.txt is a file that contains all the paths to the inferred files:
files = input.split('\n')[:-1]
for f in files:
    fam = open(f, 'rU').read()
    fams = zip(*[ i.split(',') for i in fam.split('\n')[:-2]])
    # What I want is marker ID, F1 genotypes, F2 genotypes
    ls = []
    for i in fams[10:]:
        ls.append([i[0]]+[i[3]+'-'+i[4]]+list(i[5:]))
    lz = []
    for i in ls:
        lz.append(','.join(i)+'\n')
    lz2 = ','.join(lz).replace('\n,','\n')
    #d = {}
    #d['ab-ab'] = 'B2.6'
    #d['aa-ab'] = 'D2.15'
    #d['ab-aa'] = 'D1.10'
    #lz3 = [ i.split(',')[0]+','+d[i.split(',')[1]]+','+','.join(i.split(',')[2:]) +'\n' for i in lz2.split('\n')[:-1]]
    #lw = [i.split(',')[1] for i in lz2.split('\n')[:-1]]
    lx = []
    for i in lw:
        if i not in lx:
            lx.append(i)
    #lx
    d = {}
    d['ab-ab'] = 'B3.7'
    d['aa-ab'] = 'D2.15'
    d['ab-aa'] = 'D1.10'
    d.items()
    lz3 = []
    for i in lz2.split('\n')[:-1]:
        lz3.append(i.split(','))
    lz4 = []
    for i in lz3:
        lz4.append('*'+i[0]+'\t'+d[i[1]]+'\t'+','.join(i[2:]).replace('0','-')+'\n')
    lz5 = ','.join(lz4).replace('\n,','\n').replace('aa','a').replace('bb','b')
    len(lz5.split('\n')[0].split(','))
    fin = str(len(lz5.split('\n')[0].split(',')))+' '+str(len(lz5.split('\n')[:-1]))+'\n'+lz5
    o = '/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/OneMap/'+ ','.join(f.split('-')[1].split('.')[:-1]).replace(',','.')+ '_OneMap.txt'
    z = open(o, 'w')
    z.write(fin)
    z.close()


# <codecell>

f = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_7.1.csv'
'/Volumes/group_dv/personal/DValenzano/Jan2014/Stanford_paper/OneMap/'+ ','.join(f.split('-')[1].split('.')[:-1]).replace(',','.')+ '_OneMap.txt'

# <codecell>


