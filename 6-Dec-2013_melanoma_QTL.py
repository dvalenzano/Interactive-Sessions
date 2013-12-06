# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Goal: To map melanoma in cross G and cross AA ... to be continued with Pat

# <markdowncell>

# First, from the matrix that contains all the genotypeXphenotypes, I need to select a submatrix that contains only individuals with melanoma

# <codecell>

bigmatrix = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_allfam_2.csv', 'rU').read()

# <codecell>

bms = bigmatrix.split('\n')

# <codecell>

ls = []
for i in bms:
    if i.split(',')[6]=='1':
        ls.append(i+'\n')

# <codecell>

final = ','.join([bms[0]+'\n']+ls).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_melanoma0.csv', 'w')
z.write(final)
z.close()

# <markdowncell>

# The file Go_melanoma0.csv is indeed the matrix that contains only F2 males with melanoma

# <markdowncell>

# Second, we transpose the matrix that we just generated, and remove all the phenotypes that we do not need, leaving only "melanoma"

# <codecell>

fs = zip(*[  i.split(',') for i in final.split('\n')[:-1]]) #zip(* operates a matrix transposition

# <codecell>

fsl = []
for i in fs:
    fsl.append(list(i))

# <codecell>

fslf = [fsl[0]]+fsl[6:]

# <codecell>

fslf2 = []
for i in fslf:
    fslf2.append(','.join(i)+'\n')
ff = ','.join(fslf2).replace('\n,','\n')

ffs = ff.split('\n')[2:-1]

# <codecell>

ffss = zip(*[ o.split(',') for o in ffs])

# <codecell>

ffss0 = ffss[1:]

# <codecell>

lst = []
for i in ffss0:
    lst.append(','.join(list(i))+'\n')

# <codecell>

#lst = [','.join(list(i))+'\n' for i in ffss0]

# <codecell>

lstj = ','.join(lst).replace('\n,','\n').replace('0', '-')

# <markdowncell>

# put back the columns and rows that are missing 

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_melanoma1.csv','w')
z.write(ff)
z.close()

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


