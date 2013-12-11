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

lstjs = lstj.split('\n')[:-1] # this will be used later as the data matrix to which we add header and marker names

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_melanoma1.csv','w')
z.write(ff)
z.close()

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_melanoma_lst.csv','w')
z.write(lstj)
z.close()

# <markdowncell>

# put back the columns and rows that are missing 

# <codecell>

header01 = fslf[:2] # this is the first two lines of the header, including IDs and the "melanoma" row with all the "1"

# <codecell>

fcol = list(ffss[0]) # this is the list of markers 

# <codecell>

lst2 = [','.join(fcol)] + lstjs  

# <codecell>

lst3 = [  i.split(',')  for i in lst2]

# <codecell>

lst3t = zip(*lst3)

# <codecell>

lst4 = [ list(i)  for i in lst3t]

# <codecell>

lst5 = header01 + lst4

# <codecell>

lst5t =[  list(i) for i in zip(*lst5)]

# <codecell>

Lst = []
for i in lst5t:
    Lst.append(','.join(list(i))+'\n')
    
Lstj = ','.join(Lst).replace('\n,','\n')  # this is the final file on which we run the likelihood ratio test

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_melanoma_2.csv','w') 
z.write(Lstj)
z.close()

# <markdowncell>

# lrt analyzes a data file that is the transposed version of Lstj, i.e. lst5, which needs to be joined as as string and saved as such

# <codecell>

Lst5 = []
for i in lst5:
    Lst5.append(','.join(list(i))+'\n')
    
Lst5j = ','.join(Lst5).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_melanoma_3.csv','w') 
z.write(Lst5j)
z.close()

# <codecell>

add = []
for i in Lst5:
    if i.count('aa') == 0:
        if i.count('bb') == 0:
            add.append(i)

# <codecell>

add = []
for i in Lst5:
    if i.count('a') + i.count('b') == 0:
        add.append(i)

# <markdowncell>

# From here on I moved to terminal and ran python from there - see following lines (which raises the point: how do I import python modules in ipython notebook???)

# <markdowncell>

# >>> a = open('/Volumes/group_dv/personal/DValenzano/Dec2013/Go_melanoma_3.csv','rU').read()  
# >>> import lrt  
# >>> a_lrt = lrt.out(a)  
# >>> z = open('Melanoma_QTL.csv', 'w')  
# >>> z.write(a_lrt)  
# >>> z.close()  
# 
# I did modify lrt.py to exclude the markers that have 0 'a' and 0 'b'  

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

