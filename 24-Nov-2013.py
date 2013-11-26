# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Goal: cleaning up the ped files

# <codecell>

aao = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped2.csv', 'rU').read()
go = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped2.csv', 'rU').read()

# <markdowncell>

# The following converts to "0" the single and double dashes

# <codecell>

aao = aao.replace(" ", "0").replace("--", "0").replace("-", "0").replace("Catalog0", "Catalog-").replace(',,',',0,').replace(',0,,',',0,0,')
go = go.replace(" ", "0").replace("--", "0").replace("-", "0").replace("Catalog0", "Catalog-")

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped3.csv', 'w')
z.write(aao)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped3.csv', 'w')
z.write(go)
z.close()

# <codecell>

lsaa = []
lsg = []
aaoar = zip(*[ i.split(',')  for i in aao.split('\n')[:-1]])
goar = zip(*[   i.split(',')  for i in go.split('\n')[:-1]] )

# <headingcell level=2>

# First I work with AA

# <codecell>

len(aaoar[2]) - (list(aaoar[2])[1:].count('F1')+ list(aaoar[2])[1:].count('P0')+2)

# <markdowncell>

# This above is the number of F2 individuals in this cross

# <codecell>

#i = 0 
#a = 0
#b = len(list(aaoar[10]))
#while i < b:
#    if aaoar[2][i] == 'F2' and aaoar[10][i] == '0':
#        a+=1
#    i+=1
#print a

# <codecell>

#ls = []
#ls2 = []
#for i in range(10, len(aaoar)):
#    for j in range(0, (len(aaoar[10])-1)):
#                if aaoar[2][j] == 'F2' and aaoar[i][j] == '0':
#                    ls.append('1')
#                if len(ls) < 60:
#                    ls2.append(list(aaoar[i]))

# <markdowncell>

# Below a method to select the markers with less than 75% blanck genotypes among the F2 subjects

# <codecell>

F2 = [] 
for j in (range(0, (len(aaoar[0])-1))):
    if aaoar[2][j] == 'F2':
        F2.append(j) #F2 contains the index numbers corresponding to F2 genotypes

# <codecell>

def count0(input):
    a = []
    for i in F2:
        a.append(input[i])
    return [input[0]] + [a.count('0')] #this function returns a list with the marker name and the number of '0' for the F2 subject

# <codecell>

ls = []
for i in range(10, len(aaoar)):
    ls.append(count0(aaoar[i]))  #here I am calling the function for each marker in the array

namesin = []
for i in ls:
    if i[1] <61:
        namesin.append(i[0]) #here I am keeping only the names of the markers with less than 61 '0', which corresponds to 75% of blanck genotypes

# <codecell>

print len(ls) - len(namesin)

# <markdowncell>

# 905 markers are excluded from the analysis because they have genotyping depth that is lower than 25% 

# <codecell>

included = []
for i in aaoar:
    if i[0] in namesin:
        included.append(list(i)) #here I am saving the markers with the right names

# <codecell>

filtered = aaoar[:10]+included #here I am reconstructing the whole array, including the phenotypes and family names

# <codecell>

filteredt = zip(*filtered)

# <codecell>

aaof = []
for i in filteredt:
    aaof.append(','.join(list(i))+'\n')

# <codecell>

aaofj = ','.join(aaof).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped4.csv', 'w')
z.write(aaofj)
z.close()

# <headingcell level=2>

# Now I need to do the same with G

# <codecell>

len(goar[2]) - (list(goar[2])[1:].count('F1')+ list(goar[2])[1:].count('P0')+2)

# <codecell>

F2g = [] 
for j in (range(0, (len(goar[0])-1))):
    if goar[2][j] == 'F2':
        F2g.append(j) #F2 contains the index numbers corresponding to F2 genotypes

# <codecell>

def count0(input):
    a = []
    for i in F2g:
        a.append(input[i])
    return [input[0]] + [a.count('0')] #this function returns a list with the marker name and the number of '0' for the F2 subject

# <codecell>

206*.75

# <codecell>

ls = []
for i in range(10, len(goar)):
    ls.append(count0(goar[i]))  #here I am calling the function for each marker in the array

namesin = []
for i in ls:
    if i[1] <155:
        namesin.append(i[0]) #here I am keeping only the names of the markers with less than 61 '0', which corresponds to 75% of blanck genotypes

# <codecell>

print len(ls) - len(namesin)

# <markdowncell>

# 905 markers are excluded from the analysis because they have genotyping depth that is lower than 25%

# <codecell>

included = []
for i in goar:
    if i[0] in namesin:
        included.append(list(i)) #here I am saving the markers with the right names

# <codecell>

filtered = goar[:10]+included #here I am reconstructing the whole array, including the phenotypes and family names

# <codecell>

filteredt = zip(*filtered)

# <codecell>

gof = []
for i in filteredt:
    gof.append(','.join(list(i))+'\n')

# <codecell>

gofj = ','.join(gof).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped4.csv', 'w')
z.write(gofj)
z.close()

# <codecell>


