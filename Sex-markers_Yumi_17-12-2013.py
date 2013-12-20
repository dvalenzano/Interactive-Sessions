# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: to identify sex-biased markers in cross Go and cross AAo - these markers will be used to design primers that amplify sex-linked regions in N. furzeri

# <codecell>

bigmatrix = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_allfam_2.csv', 'rU').read() # open the file in python

# <codecell>

bms = bigmatrix.split('\n') # split the file by new line

# <codecell>

fem = [] # this loop will save a female-only matrix
for i in bms:
    if i.split(',')[1]=='2':
        fem.append(i+'\n')

# <codecell>

fin_fem = ','.join([bms[0]+'\n']+fem).replace('\n,','\n') #join the list into a string again. Python can only save files as string (to my knowledge).

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female.csv', 'w')
z.write(fin_fem)
z.close()

# <codecell>

ft = zip(*[  i.split(',') for i in fin_fem.split('\n')[:-1]]) #zip(* operates a matrix transposition

ft1 = []  
for i in ft:
    ft1.append(list(i)) #this converts the list of tuples in to list of lists, i.e. an array

# <codecell>

ft1f = [ft1[0]]+[ft1[1]]+ft1[7:]

# <codecell>

ft1f2 = []
for i in ft1f:
    ft1f2.append(','.join(i)+'\n')
ff = ','.join(ft1f2).replace('\n,','\n')

ffs = ff.split('\n')[2:-1] # only considers the genotypes, i.e. no phenotype or markers names now

# <codecell>

ffss = zip(*[ o.split(',') for o in ffs])

# <codecell>

ffss0 = ffss[1:]

lst = []
for i in ffss0:
    lst.append(','.join(list(i))+'\n')
    
lstj = ','.join(lst).replace('\n,','\n').replace('0', '-')

lstjs = lstj.split('\n')[:-1] # this will be used later as the data matrix to which we add header and marker names

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female1.csv','w')
z.write(ff)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_lst.csv','w')
z.write(lstj)
z.close()

# <codecell>

header01 = ft1f[:2] # this is the first two lines of the header, including IDs and the "melanoma" row with all the "1"
fcol = list(ffss[0]) # this is the list of markers 
lst2 = [','.join(fcol)] + lstjs  
lst3 = [  i.split(',')  for i in lst2]
lst3t = zip(*lst3)
lst4 = [ list(i)  for i in lst3t]
lst5 = header01 + lst4
lst5t =[  list(i) for i in zip(*lst5)]
Lst = []
for i in lst5t:
    Lst.append(','.join(list(i))+'\n')
    
Lstj = ','.join(Lst).replace('\n,','\n')  # this is the final file on which we run the likelihood ratio test

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_2.csv','w') 
z.write(Lstj)
z.close()

# lrt analyzes a data file that is the transposed version of Lstj, i.e. lst5, which needs to be joined as as string and saved as such

Lst5 = []
for i in lst5:
    Lst5.append(','.join(list(i))+'\n')
    
Lst5j = ','.join(Lst5).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_3.csv','w') 
z.write(Lst5j)
z.close()

add = []
for i in Lst5:
    if i.count('aa') == 0:
        if i.count('bb') == 0:
            add.append(i)



add = []
for i in Lst5:
    if i.count('a') + i.count('b') == 0:
        add.append(i)

# <markdowncell>

# As super user, I ran:  
# >>> a = open('Go_female_3.csv','rU').read()  
# >>> import lrt  
# >>> a_lrt = lrt.out(a)  
# >>> z = open('Go_femaleqtl0.csv', 'w')   #this file has all the LRT, LOD score and p-values for all the markers in association to sex#
# >>> z.write(a_lrt)  
# >>> z.close()  

# <markdowncell>

# Now we need to isolate the markers that have LOD score for sex higher than 5 - these will most likely be sex-linked

# <codecell>

fqtl0 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_femaleqtl0.csv', 'rU').read()

# <codecell>

fqs = fqtl0.split('\n')
fhLOD = [ i  for i in fqs[1:] if float(i.split('\t')[2])>20] #only picks markers that have LOD score higher than 20

# <codecell>

fqtlID = [ i.split('\t')[0][:-1] for i in fhLOD ]

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_qtl1.csv', 'w')
z.write(','.join(fqtlID))
z.close()

# <codecell>

','.join(fqtlID)[:100]

# <markdowncell>

# Now for males:

# <codecell>

mal = [] # this loop will save a male-only matrix
for i in bms:
    if i.split(',')[1]=='1':
        mal.append(i+'\n')
        
fin_mal = ','.join([bms[0]+'\n']+mal).replace('\n,','\n') #join the list into a string again. Python can only save files as string (to my knowledge).

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_male.csv', 'w')
z.write(fin_mal)
z.close()

# <codecell>

import math  
def out(input):  
  ls = []  
  for i in input.split('\n')[2:]:  
    a = i.count('a')  
    b = i.count('b')  
    if a+b == 0:  
      next  
    else:  
      freq_a = float(a)/(a+b)  
      freq_b = 1-freq_a  
      MLE_ab = (freq_a**a)*(freq_b**b)  
      MLE_05 = (.5**a)*(.5**b)   
      LRT = 2*(math.log(MLE_ab)-math.log(MLE_05))  
      LOD = math.log10(MLE_ab/MLE_05)  
      p_val = 1.0/(10**(LOD))  
      out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'  
      ls.append(out)  
  return 'Marker'+'\tLRT\tLOD\tp_val\n'+','.join(ls)[:-1].replace('\n,','\n')
  
  
  
#################################### #################################### ####################################
####################################         20-Dec-2013 session          ####################################
#################################### #################################### ####################################

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: to identify sex-biased markers in cross Go and cross AAo - these markers will be used to design primers that amplify sex-linked regions in N. furzeri

# <codecell>

from sets import Set

# <codecell>

bigmatrix = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_allfam_2.csv', 'rU').read() # open the file in python

# <codecell>

bms = bigmatrix.split('\n') # split the file by new line

# <codecell>

fem = [] # this loop will save a female-only matrix
for i in bms:
    if i.split(',')[1]=='2':
        fem.append(i+'\n')

# <codecell>

fin_fem = ','.join([bms[0]+'\n']+fem).replace('\n,','\n') #join the list into a string again. Python can only save files as string (to my knowledge).

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female.csv', 'w')
z.write(fin_fem)
z.close()

# <codecell>

ft = zip(*[  i.split(',') for i in fin_fem.split('\n')[:-1]]) #zip(* operates a matrix transposition

ft1 = []  
for i in ft:
    ft1.append(list(i)) #this converts the list of tuples in to list of lists, i.e. an array

# <codecell>

ft1f = [ft1[0]]+[ft1[1]]+ft1[7:]

# <codecell>

ft1f2 = []
for i in ft1f:
    ft1f2.append(','.join(i)+'\n')
ff = ','.join(ft1f2).replace('\n,','\n')

ffs = ff.split('\n')[2:-1] # only considers the genotypes, i.e. no phenotype or markers names now

# <codecell>

ffss = zip(*[ o.split(',') for o in ffs])

# <codecell>

ffss0 = ffss[1:]

lst = []
for i in ffss0:
    lst.append(','.join(list(i))+'\n')
    
lstj = ','.join(lst).replace('\n,','\n').replace('0', '-')

lstjs = lstj.split('\n')[:-1] # this will be used later as the data matrix to which we add header and marker names

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female1.csv','w')
z.write(ff)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_lst.csv','w')
z.write(lstj)
z.close()

# <codecell>

header01 = ft1f[:2] # this is the first two lines of the header, including IDs and the "melanoma" row with all the "1"
fcol = list(ffss[0]) # this is the list of markers 
lst2 = [','.join(fcol)] + lstjs  
lst3 = [  i.split(',')  for i in lst2]
lst3t = zip(*lst3)
lst4 = [ list(i)  for i in lst3t]
lst5 = header01 + lst4
lst5t =[  list(i) for i in zip(*lst5)]
Lst = []
for i in lst5t:
    Lst.append(','.join(list(i))+'\n')
    
Lstj = ','.join(Lst).replace('\n,','\n')  # this is the final file on which we run the likelihood ratio test

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_2.csv','w') 
z.write(Lstj)
z.close()

# lrt analyzes a data file that is the transposed version of Lstj, i.e. lst5, which needs to be joined as as string and saved as such

Lst5 = []
for i in lst5:
    Lst5.append(','.join(list(i))+'\n')
    
Lst5j = ','.join(Lst5).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_3.csv','w') 
z.write(Lst5j)
z.close()

add = []
for i in Lst5:
    if i.count('aa') == 0:
        if i.count('bb') == 0:
            add.append(i)



add = []
for i in Lst5:
    if i.count('a') + i.count('b') == 0:
        add.append(i)

# <markdowncell>

# As super user, I ran:  
# >>> a = open('Go_female_3.csv','rU').read()  
# >>> import lrt  
# >>> a_lrt = lrt.out(a)  
# >>> z = open('Go_femaleqtl0.csv', 'w')   #this file has all the LRT, LOD score and p-values for all the markers in association to sex#  
# >>> z.write(a_lrt)  
# >>> z.close()  

# <markdowncell>

# Now we need to isolate the markers that have LOD score for sex higher than 5 - these will most likely be sex-linked

# <codecell>

fqtl0 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_femaleqtl0.csv', 'rU').read()

# <codecell>

fqs = fqtl0.split('\n')
fhLOD = [ i  for i in fqs[1:] if float(i.split('\t')[2])>20] #only picks markers that have LOD score higher than 20

# <codecell>

fqtlID = [ i.split('\t')[0][:-1] for i in fhLOD ]

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_female_qtl1.csv', 'w')
z.write(','.join(fqtlID))
z.close()

# <codecell>

','.join(fqtlID)[:100]

# <markdowncell>

# Now for males:

# <codecell>

mal = [] # this loop will save a male-only matrix
for i in bms:
    if i.split(',')[1]=='1':
        mal.append(i+'\n')
        
fin_mal = ','.join([bms[0]+'\n']+mal).replace('\n,','\n') #join the list into a string again. Python can only save files as string (to my knowledge).

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_male.csv', 'w')
z.write(fin_mal)
z.close()

mt = zip(*[  i.split(',') for i in fin_mal.split('\n')[:-1]]) #zip(* operates a matrix transposition

mt1 = []  
for i in mt:
    mt1.append(list(i)) #this converts the list of tuples in to list of lists, i.e. an array

mt1f = [mt1[0]]+[mt1[1]]+mt1[7:]
    
mt1f2 = []
for i in mt1f:
    mt1f2.append(','.join(i)+'\n')
mm = ','.join(mt1f2).replace('\n,','\n')

mms = mm.split('\n')[2:-1] # only considers the genotypes, i.e. no phenotype or markers names now

mmss = zip(*[ o.split(',') for o in mms])

mmss0 = mmss[1:]

lst = []
for i in mmss0:
    lst.append(','.join(list(i))+'\n')
    
lstj = ','.join(lst).replace('\n,','\n').replace('0', '-')

lstjs = lstj.split('\n')[:-1] # this will be used later as the data matrix to which we add header and marker names

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_male1.csv','w')
z.write(mm)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_male_lst.csv','w')
z.write(lstj)
z.close()

header01 = mt1f[:2] # this is the first two lines of the header, including IDs and the "melanoma" row with all the "1"
mcol = list(mmss[0]) # this is the list of markers 
lst2 = [','.join(mcol)] + lstjs  
lst3 = [  i.split(',')  for i in lst2]
lst3t = zip(*lst3)
lst4 = [ list(i)  for i in lst3t]
lst5 = header01 + lst4
lst5t =[  list(i) for i in zip(*lst5)]
Lst = []
for i in lst5t:
    Lst.append(','.join(list(i))+'\n')
    
Lstj = ','.join(Lst).replace('\n,','\n')  # this is the final file on which we run the likelihood ratio test

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_male_2.csv','w') 
z.write(Lstj)
z.close()

# lrt analyzes a data file that is the transposed version of Lstj, i.e. lst5, which needs to be joined as as string and saved as such

Lst5 = []
for i in lst5:
    Lst5.append(','.join(list(i))+'\n')
    
Lst5j = ','.join(Lst5).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_male_3.csv','w') 
z.write(Lst5j)
z.close()

add = []
for i in Lst5:
    if i.count('aa') == 0:
        if i.count('bb') == 0:
            add.append(i)



add = []
for i in Lst5:
    if i.count('a') + i.count('b') == 0:
        add.append(i)

# <codecell>

mqtl0 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_maleqtl0.csv', 'rU').read()

# <codecell>

mqs = mqtl0.split('\n')
mhLOD = [ i  for i in mqs[1:] if float(i.split('\t')[2])>20] #only picks markers that have LOD score higher than 20

# <codecell>

mqtlID = [ i.split('\t')[0][:-1] for i in mhLOD ]

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_male_qtl1.csv', 'w')
z.write(','.join(mqtlID))
z.close()

# <codecell>

sm = Set(mqtlID)
sf = Set(fqtlID)

# <codecell>

print(
      'the male set length is: '+  str(len(sm)),
      'the female set length is: ' + str(len(sf))
      )

# <codecell>

sf -= sm

# <codecell>

len(sf)

# <codecell>

list(sf)

# <codecell>

import math  
def out(input):  
  ls = []  
  for i in input.split('\n')[2:]:  
    a = i.count('a')  
    b = i.count('b')  
    if a+b == 0:  
      next  
    else:  
      freq_a = float(a)/(a+b)  
      freq_b = 1-freq_a  
      MLE_ab = (freq_a**a)*(freq_b**b)  
      MLE_05 = (.5**a)*(.5**b)   
      LRT = 2*(math.log(MLE_ab)-math.log(MLE_05))  
      LOD = math.log10(MLE_ab/MLE_05)  
      p_val = 1.0/(10**(LOD))  
      out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'  
      ls.append(out)  
  return 'Marker'+'\tLRT\tLOD\tp_val\n'+','.join(ls)[:-1].replace('\n,','\n')



