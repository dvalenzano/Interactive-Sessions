# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Goal: To build a genotype/phenotipe matrix with complete phenotypes for QTL analysis

# <codecell>

inf1a = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_1.csv', 'rU').read()
inf1b = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inf_fam_Go/inf_fam_1.csv', 'rU').read()

# <markdowncell>

# Now I need to transpose both matrices 

# <codecell>

headgo = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped7.csv', 'rU').read()
headaao = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped7.csv', 'rU').read()

# <codecell>

headgo0 = headgo.split('\n')[0].split(',')[10:]
headaao0 = headaao.split('\n')[0].split(',')[10:]

# <codecell>

ls_inf1a = []
[ ls_inf1a.append(i.split(','))    for i in inf1a.split('\n')[:-2]]
inf1at = zip(*ls_inf1a)

ls_inf1b = []
[ ls_inf1b.append(i.split(','))    for i in inf1b.split('\n')[:-1]]
inf1bt = zip(*ls_inf1b)

keys_1a = []
values_1a = []

keys_1b = []
values_1b = []

whatevs1a = [ keys_1a.append(i[0]) for i in inf1at[10:]]
whatevs1a = [ values_1a.append(','.join(i[1:]))  for i in inf1at[10:]]

whatevs1b = [ keys_1b.append(i[0]) for i in inf1bt[10:]]
whatevs1b = [ values_1b.append(','.join(i[1:]))  for i in inf1bt[10:]]


dict_1a = dict(zip(keys_1a, values_1a))
dict_1b = dict(zip(keys_1b, values_1b))

# <codecell>

fullgo = []
whatevesfgo = [ fullgo.append([i]+dict_1b[i].split(',')) if i in dict_1b.keys() else fullgo.append([i]+dict_1a[i].split(',')) for i in headgo0]

# <codecell>

fullgof = inf1at[:10]+fullgo
fullgot = zip(*fullgof)

fullgo2 = []
[ fullgo2.append(','.join(list(i))+'\n') for i in fullgot]
fullgo3 = ','.join(fullgo2).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/provaGofam1.csv', 'w')
z.write(fullgo3)
z.close()

# <markdowncell>

# Now will follow the same as above for all the families

# <codecell>

headgo = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped7.csv', 'rU').read()
headaao = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped7.csv', 'rU').read()

headgo0 = headgo.split('\n')[0].split(',')[10:]
headaao0 = headaao.split('\n')[0].split(',')[10:]

# <codecell>

for f in open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/family-list.txt','rU').read().split('\n')[:-1]:  
    source_a = '/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_%s' %f
    source_b = '/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inf_fam_Go/inf_%s' %f

    ina = open(source_a, 'rU').read()
    inb = open(source_b, 'rU').read()

    ls_ina = []
    [ ls_ina.append(i.split(','))    for i in ina.split('\n')[:-2]]
    inat = zip(*ls_ina)
    
    ls_inb = []
    [ ls_inb.append(i.split(','))    for i in inb.split('\n')[:-1]]
    inbt = zip(*ls_inb)
    
    keys_a = []
    values_a = []
    
    keys_b = []
    values_b = []
    
    whatevsa = [ keys_a.append(i[0]) for i in inat[10:]]
    whatevsa = [ values_a.append(','.join(i[1:]))  for i in inat[10:]]
    
    whatevsb = [ keys_b.append(i[0]) for i in inbt[10:]]
    whatevsb = [ values_b.append(','.join(i[1:]))  for i in inbt[10:]]
    
    dict_a = dict(zip(keys_a, values_a))
    dict_b = dict(zip(keys_b, values_b))
    
    fullgo = []
    whatevesfgo = [ fullgo.append([i]+dict_b[i].split(',')) if i in dict_b.keys() else fullgo.append([i]+dict_a[i].split(',')) for i in headgo0]
    
    fullgo = inat[:10]+fullgo
    fullgot = zip(*fullgo)
    
    fullgo2 = []
    [ fullgo2.append(','.join(list(i))+'\n') for i in fullgot]
    fullgo3 = ','.join(fullgo2).replace('\n,','\n')
    
    des = '/Volumes/group_dv/personal/DValenzano/Dec2013/Go_%s' %f
    
    z = open(des, 'w')
    z.write(fullgo3)
    z.close()

# <markdowncell>

# Now I need to put all the families together in one big file

# <codecell>

lst = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go-list.txt', 'rU').read()
lists = lst.split('\n')[:-1]
ls = []
num = range(len(lists))

# <codecell>

for i in lists:
    fam = open(i, 'rU').read()
    ls.append(fam)
    
ls = ','.join(ls).replace('\n,','\n')
lss = ls.split('\n')
l3s = []
for i in lss:
    if i.split(',')[0] == '':
        next
    else:
        l3s.append(i+'\n')

lf = lss[0]+'\n'+','.join(l3s).replace('\n,','\n')
       
z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_allfam.csv', 'w')
z.write(lf)
z.close()

# <headingcell level=2>

# It works! Now I need to do the same thing for cross AA

# <codecell>

headaao = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped7.csv', 'rU').read()
headaao0 = headaao.split('\n')[0].split(',')[10:]

for f in open('/Volumes/group_dv/personal/DValenzano/Nov2013/AAo_families/family-list.txt','rU').read().split('\n')[:-1]:  
    source_a = '/Volumes/group_dv/personal/DValenzano/Nov2013/AAo_families/inferrednew_%s' %f
    source_b = '/Volumes/group_dv/personal/DValenzano/Nov2013/AAo_families/inf_fam_AAo/inf_%s' %f

    ina = open(source_a, 'rU').read()
    inb = open(source_b, 'rU').read()

    ls_ina = []
    [ ls_ina.append(i.split(','))    for i in ina.split('\n')[:-2]]
    inat = zip(*ls_ina)
    
    ls_inb = []
    [ ls_inb.append(i.split(','))    for i in inb.split('\n')[:-1]]
    inbt = zip(*ls_inb)
    
    keys_a = []
    values_a = []
    
    keys_b = []
    values_b = []
    
    whatevsa = [ keys_a.append(i[0]) for i in inat[10:]]
    whatevsa = [ values_a.append(','.join(i[1:]))  for i in inat[10:]]
    
    whatevsb = [ keys_b.append(i[0]) for i in inbt[10:]]
    whatevsb = [ values_b.append(','.join(i[1:]))  for i in inbt[10:]]
    
    dict_a = dict(zip(keys_a, values_a))
    dict_b = dict(zip(keys_b, values_b))
    
    fullaao = []
    whatevesfaao = [ fullaao.append([i]+dict_b[i].split(',')) if i in dict_b.keys() else fullaao.append([i]+dict_a[i].split(',')) for i in headaao0]
    
    fullaao = inat[:10]+fullaao
    fullaaot = zip(*fullaao)
    
    fullaao2 = []
    [ fullaao2.append(','.join(list(i))+'\n') for i in fullaaot]
    fullaao3 = ','.join(fullaao2).replace('\n,','\n')
    
    des = '/Volumes/group_dv/personal/DValenzano/Dec2013/AAo_%s' %f
    
    z = open(des, 'w')
    z.write(fullaao3)
    z.close()

# <codecell>

lst = open('/Volumes/group_dv/personal/DValenzano/Dec2013/AAo-list.txt', 'rU').read()
lists = lst.split('\n')[:-1]
ls = []
num = range(len(lists))

for i in lists:
    fam = open(i, 'rU').read()
    ls.append(fam)
    
ls = ','.join(ls).replace('\n,','\n')
lss = ls.split('\n')
l3s = []
for i in lss:
    if i.split(',')[0] == '':
        next
    else:
        l3s.append(i+'\n')

lf = lss[0]+'\n'+','.join(l3s).replace('\n,','\n')
       
z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/AAo_allfam.csv', 'w')
z.write(lf)
z.close()

# <codecell>


