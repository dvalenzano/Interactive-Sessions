# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Goal: To translate genotypes and phenotypes in numeric values

# <headingcell level=2>

# File type: ped file

# <codecell>

go = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped1.csv', 'rU').read() 
aao = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped1.csv', 'rU').read()  

# <markdowncell>

# Need to translate these files into arrays

# <codecell>

goar = [ i.split(',') for i in go.split('\n')]
aaoar = [ i.split(',') for i in aao.split('\n')]

# <codecell>

goart = zip(*goar)
aaoart = zip(*aaoar)

# <codecell>

goartsex = ','.join(goart[5]).replace('m', '1').replace('f', '2').replace('12', 'mf')
goartcol = ','.join(goart[8]).replace('y', '1').replace('r', '2').replace('col12', 'col')
goartb = ','.join(goart[9]).replace('nb', '2').replace('b', '1').replace('col_1.2', 'bl')
gof = goart[:5]+[tuple(goartsex.split(','))]+[tuple(goartcol.split(','))]+[tuple(goartb.split(','))]+goart[10:]

# <codecell>

gofnl = []
for i in gof:
    gofnl.append(list(i))

# <codecell>

gofnltt = zip(*gofnl)
gol = []
for i in gofnltt:
    gol.append(','.join(i)+'\n')
golj = ','.join(gol).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped2.csv', 'w')
z.write(golj)
z.close()

# <codecell>

aaoartsex = ','.join(aaoart[5]).replace('m', '1').replace('f', '2').replace('12', 'mf')
aaoartcol = ','.join(aaoart[8]).replace('y', '1').replace('r', '2').replace('col212', 'col')
aaoartb = ','.join(aaoart[9]).replace('nb', '2').replace('b', '1').replace('col_1.2', 'bl')
aaof = aaoart[:5]+[tuple(aaoartsex.split(','))]+[tuple(aaoartcol.split(','))]+[tuple(aaoartb.split(','))]+aaoart[10:]

# <codecell>

aaofnl = []
for i in aaof:
    aaofnl.append(list(i))

# <codecell>

aaofnltt = zip(*aaofnl)
aaol = []
for i in aaofnltt:
    aaol.append(','.join(i)+'\n')
aaolj = ','.join(aaol).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped2.csv', 'w')
z.write(aaolj)
z.close()

