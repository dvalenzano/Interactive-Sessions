# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# This script will performe a complete genotype inference for the F1 missing and mis-typed genotypes

# <markdowncell>

# First, break down the big genotyping matrix into sub-matrices

# <codecell>

go = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/goped6.csv', 'rU').read()
go = go.replace('A', 'a').replace('B', 'b')


gos1t = zip(*[ i.split(',')   for i in go.split('\n')])

# Here I am removing the markers where either of the grandparents have a missing genotype

gos2t = []
for i in gos1t[10:]:
    if '0' not in i[1] + i[2]:
        gos2t.append(list(i))

gos2t = gos1t[:10]+gos2t
gos2tt = zip(*gos2t)

gon = []
gonn=[]

for i in gos2tt:
   gon.append(','.join(list(i))+'\n') 

gonj = ','.join(gon).replace('\n,','\n')
gonj[-100:]
z = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/goped7.csv', 'w')
z.write(gonj)
z.close()

gonj = gonj.replace('Ffam', 'F_f').replace('Mfam', 'M_f') #I needed to add this line because splitting by "fam" was not giving the expected result - check out the F1 Catalog-IDs for this matrix and you'll understand the problem
gos = gonj.split('fam')
keys = gos[0].split(',')[10:]
keys= keys[:-1]+[keys[-1][:-1]] #the last element had a \n attached to it!!

values = []

for i in range(10, len(gos[0].split(','))):
               values.append(gos[1].split('\n')[0].split(',')[i]+gos[1].split('\n')[1].split(',')[i])
d = dict(zip(keys, values)) # A dictionary that goes like this: { '8563': 'aabb', '63406': 'aabb', ...}

# Now starts the family specific loop:
for f in range(1, len(gos)):
  valuesf1f = []
  valuesf1m = []

  for i in range(10, len(gos[0].split(','))):
    valuesf1f.append(gos[f].split('\n')[2].split(',')[i])

  for i in range(10, len(gos[0].split(','))):
    valuesf1m.append(gos[f].split('\n')[3].split(',')[i])       

  df1f = dict(zip(keys, valuesf1f)) #dictionaries are not sorted, so can't be sliced 
  df1m = dict(zip(keys, valuesf1m))

  f1f = [] #this returns the F1 female values
  for i in keys:
    if df1f[i] == '0':
      if d[i] == 'aabb': 
        f1f.append('ab')
      else:
        f1f.append(df1f[i])
    else:
      f1f.append(df1f[i])
        
  f1m = [] #this returns the F1 male values
  for i in keys:
    if df1m[i] == '0':
      if d[i] == 'aabb': 
        f1m.append('ab')
      else:
        f1m.append(df1m[i])
    else:
      f1m.append(df1m[i])
        
  ls = []
  for i in range(len(gos[f].split('\n'))):
    if i in [0,1]+range(4, len(gos[f].split('\n'))):
      ls.append(gos[f].split('\n')[i]+'\n')
    elif i == 2:
      ls.append(','.join(gos[f].split('\n')[i].split(',')[:10]+f1f)+'\n')
    elif i == 3:
      ls.append(','.join(gos[f].split('\n')[i].split(',')[:10]+f1m)+'\n')
        
        #  lsj = ','.join(ls).replace('\n,','\n')
  lsj = gos[0]+','.join(ls).replace('\n,','\n')

  currentfamily = '/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/inferrednew_fam_%s.csv' % gos[f].split('\n')[0].split(',')[0]
  z = open(currentfamily, 'w') 
  z.write(lsj)
  z.close()

# <codecell>


# <codecell>

import math
import numpy
import scipy

input = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/inferred-list.txt', 'rU').read() #inferred-list.txt is a file that contains all the paths to the inferred files:
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_1.1.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_1.2.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_1.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_10.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_13.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_14.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_16.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_2.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_4.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_5.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_7.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_7.1.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_8.csv
#/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_9.csv

files = input.split('\n')[:-1]

for fl in files:
    fam_1dot1 = open(fl, 'rU').read()
    
    ls = []
    for i in fam_1dot1.split('\n'):
        ls.append(i.split(','))
    
    ls = ls[:-2]
    
    lst = zip(*ls) #transpose the matrix and creates a list of tuples
    
    lst2 = []
    for i in lst:
        if i[0] != '3641': #this marker had 'c' alleles and was messing up with the analysis. I just removed it.
            lst2.append(','.join(i))
        
#    lst3 = []
#    for i in lst2: #originally it was 'for i in lst:'
#        lst3.append(','.join(i)+'\n')
        
#    lst4 = ','.join(lst3).replace('\n,', '\n')
    
    missingbf1s = []
    missing1f1s = []
    missing2f1s = []
    notmissingf1s = []
    
    for i in lst[10:]:
      if i[3] == '0' and i[4] == '0':  #i.e. both F1 are missing
            missingbf1s.append(i[0])
      elif i[3] == '0' and i[4] != '0': #i.e. the first F1 is missing
            missing1f1s.append(i[0])
      elif i[3] != '0' and i[4] == '0': #i.e. the second F1 is missing
            missing2f1s.append(i[0])
      else:
            notmissingf1s.append(i[0])
          
    missingbf1st = ','.join(missingbf1s)
    missing1f1st = ','.join(missing1f1s)
    missing2f1st = ','.join(missing2f1s)
    notmissingf1st = ','.join(notmissingf1s)

    lz = lst2[:10]
    
    ID = []
    p0 = []
    f1 = []
    f2 = []
    p0f1 = []
    f1f2 = []
    keys = []
    aL = []
   
    for i in lst2[10:]: #only import the array starting from the genotype rows
    
        if i.split(',')[0] in notmissingf1s:  #now we need to check that there are no mis-typed F1s
            
            ID.append(i.split(',')[0])
            p0.append(i.split(',')[1]+i.split(',')[2])
            f1.append(i.split(',')[3]+i.split(',')[4])
            p0f1.append(i.split(',')[1]+i.split(',')[2]+i.split(',')[3]+i.split(',')[4])
            f2.append(','.join(i.split(',')[5:]))
            f1f2.append(','.join(i.split(',')[3:]))
            keys.append(i.split(',')[0]+','+i.split(',')[1]+i.split(',')[2]+','+i.split(',')[3]+','+i.split(',')[4])
            aL.append(','.join(i.split(',')).split(','))
                
            d = dict(zip(keys, f2))
            df2 = dict(zip(ID, f2))
            df1f2 = dict(zip(ID, f1f2))
            df1 = dict(zip(ID, f1))
            daL = dict(zip(ID, aL))
            
            f1aaaa = [ i for i in ID if df1[i] == 'aaaa']
            f1aaab = [ i for i in ID if df1[i] == 'aaab']
            f1abaa = [ i for i in ID if df1[i] == 'abaa']
            f1abbb = [ i for i in ID if df1[i] == 'abbb']
            f1bbbb = [ i for i in ID if df1[i] == 'bbbb']
            
            nac_aaaa = [i for i in f1aaaa if 'ab' in df2[i]]
            nac_aaab = [i for i in f1aaab if 'bb' in df2[i]]
            nac_abaa = [i for i in f1abaa if 'bb' in df2[i]]
            nac_abbb = [i for i in f1abbb if 'aa' in df2[i]]
            nac_bbbb = [i for i in f1aaaa if 'ab' in df2[i]]            
            
            if i in nac_aaaa:
                a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
                b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
                if a+b == 0:
                    pass
                else:
                    freq_a = float(a)/(a+b)
                    freq_b = 1-freq_a
                
                    ############ LRT ##############
                        
                    MLE_ab = (freq_a**a)*(freq_b**b)
                    MLE_05 = (.5**a)*(.5**b) 
                    MLE_075 = (.75**a)*(.25**b)
                    MLE_025 = (.25**a)*(.75**b)
                        
                    LRT_05 = 2*(math.log(MLE_ab)-math.log(MLE_05))
                    LRT_075 = 2*(math.log(MLE_ab)-math.log(MLE_075))
                    LRT_025 = 2*(math.log(MLE_ab)-math.log(MLE_025))
            
                    ############ Poisson ##############
                        
                    lambda_05 = float(0.5*(a+b)) #lambda is the expected number of "a" give each test frequency for a (i.e. 0.5, 0.75, 0.25)
                    lambda_075 = float(.75*(a+b))
                    lambda_025 = float(.25*(a+b))
                        
                    Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
                    Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
                    Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
                    
                    ############## if i in nac_aaaa ############
                    if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                    elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                        pass  
            
            elif i in nac_aaab:
                a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
                b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
                if a+b == 0:
                    pass
                else:
                    freq_a = float(a)/(a+b)
                    freq_b = 1-freq_a
                    ############ LRT ##############
                        
                    MLE_ab = (freq_a**a)*(freq_b**b)
                    MLE_05 = (.5**a)*(.5**b) 
                    MLE_075 = (.75**a)*(.25**b)
                    MLE_025 = (.25**a)*(.75**b)
                        
                    LRT_05 = 2*(math.log(MLE_ab)-math.log(MLE_05))
                    LRT_075 = 2*(math.log(MLE_ab)-math.log(MLE_075))
                    LRT_025 = 2*(math.log(MLE_ab)-math.log(MLE_025))
            
                    ############ Poisson ##############
                        
                    lambda_05 = float(0.5*(a+b)) #lambda is the expected number of "a" give each test frequency for a (i.e. 0.5, 0.75, 0.25)
                    lambda_075 = float(.75*(a+b))
                    lambda_025 = float(.25*(a+b))
                        
                    Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
                    Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
                    Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
                    
                    ############## if i in nac_aaab ############
                    if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                    elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                        pass  
    
            elif i in nac_abaa:
                a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
                b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
                if a+b == 0:
                    pass
                else:
                    freq_a = float(a)/(a+b)
                    freq_b = 1-freq_a
                    ############ LRT ##############
                        
                    MLE_ab = (freq_a**a)*(freq_b**b)
                    MLE_05 = (.5**a)*(.5**b) 
                    MLE_075 = (.75**a)*(.25**b)
                    MLE_025 = (.25**a)*(.75**b)
                        
                    LRT_05 = 2*(math.log(MLE_ab)-math.log(MLE_05))
                    LRT_075 = 2*(math.log(MLE_ab)-math.log(MLE_075))
                    LRT_025 = 2*(math.log(MLE_ab)-math.log(MLE_025))
            
                    ############ Poisson ##############
                        
                    lambda_05 = float(0.5*(a+b)) #lambda is the expected number of "a" give each test frequency for a (i.e. 0.5, 0.75, 0.25)
                    lambda_075 = float(.75*(a+b))
                    lambda_025 = float(.25*(a+b))
                        
                    Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
                    Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
                    Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
                    
                    ############## if i in nac_abaa ############
                    if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                    elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                        pass  

            elif i in nac_abbb:
                a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
                b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
                if a+b == 0:
                    pass
                else:
                    freq_a = float(a)/(a+b)
                    freq_b = 1-freq_a
                    ############ LRT ##############
                        
                    MLE_ab = (freq_a**a)*(freq_b**b)
                    MLE_05 = (.5**a)*(.5**b) 
                    MLE_075 = (.75**a)*(.25**b)
                    MLE_025 = (.25**a)*(.75**b)
                        
                    LRT_05 = 2*(math.log(MLE_ab)-math.log(MLE_05))
                    LRT_075 = 2*(math.log(MLE_ab)-math.log(MLE_075))
                    LRT_025 = 2*(math.log(MLE_ab)-math.log(MLE_025))
            
                    ############ Poisson ##############
                        
                    lambda_05 = float(0.5*(a+b)) #lambda is the expected number of "a" give each test frequency for a (i.e. 0.5, 0.75, 0.25)
                    lambda_075 = float(.75*(a+b))
                    lambda_025 = float(.25*(a+b))
                        
                    Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
                    Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
                    Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
                    
                    ############## if i in nac_abbb ############
                    if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                    elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                        pass
            
            elif i in nac_bbbb:
                a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
                b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
                if a+b == 0:
                    pass
                else:
                    freq_a = float(a)/(a+b)
                    freq_b = 1-freq_a
                    ############ LRT ##############
                        
                    MLE_ab = (freq_a**a)*(freq_b**b)
                    MLE_05 = (.5**a)*(.5**b) 
                    MLE_075 = (.75**a)*(.25**b)
                    MLE_025 = (.25**a)*(.75**b)
                        
                    LRT_05 = 2*(math.log(MLE_ab)-math.log(MLE_05))
                    LRT_075 = 2*(math.log(MLE_ab)-math.log(MLE_075))
                    LRT_025 = 2*(math.log(MLE_ab)-math.log(MLE_025))
            
                    ############ Poisson ##############
                        
                    lambda_05 = float(0.5*(a+b)) #lambda is the expected number of "a" give each test frequency for a (i.e. 0.5, 0.75, 0.25)
                    lambda_075 = float(.75*(a+b))
                    lambda_025 = float(.25*(a+b))
                        
                    Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
                    Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
                    Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
                    
                    ############## if i in nac_bbbb ############
                    if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                    elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                        pass
            
            else:
                lz.append(i)
        
        else:
            a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
            b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
            if a+b == 0:
                pass
            else:
                freq_a = float(a)/(a+b)
                freq_b = 1-freq_a
                    
                ############ LRT ##############
                    
                MLE_ab = (freq_a**a)*(freq_b**b)
                MLE_05 = (.5**a)*(.5**b) 
                MLE_075 = (.75**a)*(.25**b)
                MLE_025 = (.25**a)*(.75**b)
                    
                LRT_05 = 2*(math.log(MLE_ab)-math.log(MLE_05))
                LRT_075 = 2*(math.log(MLE_ab)-math.log(MLE_075))
                LRT_025 = 2*(math.log(MLE_ab)-math.log(MLE_025))
        
                ############ Poisson ##############
                    
                lambda_05 = float(0.5*(a+b)) #lambda is the expected number of "a" give each test frequency for a (i.e. 0.5, 0.75, 0.25)
                lambda_075 = float(.75*(a+b))
                lambda_025 = float(.25*(a+b))
                    
                Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
                Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
                Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
                    
                ############## F1 inference #################
                    
                if a+b >15: #i.e. if there are enough genotypes to run the analysis - this line of code drops a lot of markers 
        
                    ############## below the case with both F1 genotype missing and aaxab or abxaa genotypes ############
                    if i.split(',')[0] in missingbf1s: 
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
                        
                    ############## below the case with the first F1 genotype missing ############
                    elif i.split(',')[0] in missing1f1s:
                        if i.split(',')[4] == 'aa':
                            if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'aa', then the female got to be 'bb'
                            elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['ab']+i.split(',')[4:])) #given that the male is 'aa', the female has to be 'ab'
                            elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'aa', the only possible model is a female 'bb'
                            else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                                pass
                        if i.split(',')[4] == 'ab':
                            if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['ab']+i.split(',')[4:])) #given that the male is 'ab', then the female got to be 'ab'
                            elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['aa']+i.split(',')[4:])) #given that the male is 'ab', the female has to be 'aa'
                            elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'ab', the female got to be 'bb'
                            else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                                pass
                        if i.split(',')[4] == 'bb':
                            if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['aa']+i.split(',')[4:])) #given that the male is 'bb', then the female got to be 'aa'
                            elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['aa']+i.split(',')[4:])) #given that the male is 'bb', the only possible model is a female 'aa'
                            elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                                lz.append(','.join(i.split(',')[:3]+['ab']+i.split(',')[4:])) #given that the male is 'bb', the only possible model is a female 'ab'
                            else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                                pass
                            
                    ############## below the case with the second F1 genotype missing ############
                    elif i.split(',')[0] in missing2f1s:
                        if i.split(',')[3] == 'aa':
                            if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['bb']+i.split(',')[5:])) #given that the female is 'aa', then the male got to be 'bb'
                            elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['ab']+i.split(',')[5:])) #given that the male is 'aa', the female has to be 'ab'
                            elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['bb']+i.split(',')[5:])) #given that the male is 'aa', the only possible model is a female 'bb'
                            else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                                pass
                        if i.split(',')[3] == 'ab':
                            if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['ab']+i.split(',')[5:])) #given that the male is 'ab', then the female got to be 'ab'
                            elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['aa']+i.split(',')[5:])) #given that the male is 'ab', the female has to be 'aa'
                            elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['bb']+i.split(',')[5:])) #given that the male is 'ab', the female got to be 'bb'
                            else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                                pass
                        if i.split(',')[3] == 'bb':
                            if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['aa']+i.split(',')[5:])) #given that the male is 'bb', then the female got to be 'aa'
                            elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['aa']+i.split(',')[5:])) #given that the male is 'bb', the only possible model is a female 'aa'
                            elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                                lz.append(','.join(i.split(',')[:4]+['ab']+i.split(',')[5:])) #given that the male is 'bb', the only possible model is a female 'ab'
                            else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                                pass
                 
                else: #this is for the markers with low coverage - they won't be used for the analysis
                    pass
            
    
    lw = []
    for i in lz:
        lw.append(i.split(','))
        
    lwt = zip(*lw)
        
    lwt3 = []
    for i in lwt:
        lwt3.append(','.join(i)+'\n')
        
    lwt4 = ','.join(lwt3).replace('\n,', '\n')
    output = '/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/inf'+fl[69:]                  
    z = open(output,'w')
    z.write(lwt4)
    z.close()

# <codecell>

import math
import numpy
import scipy

fam_1dot1 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/inferrednew_fam_7.csv', 'rU').read()
    
ls = []
for i in fam_1dot1.split('\n'):
    ls.append(i.split(','))
    
ls = ls[:-2]
    
lst = zip(*ls) #transpose the matrix and creates a list of tuples
    
lst2 = []
for i in lst:
    if i[0] != '3641': #this marker had 'c' alleles and was messing up with the analysis. I just removed it.
        lst2.append(','.join(i))
        
#    lst3 = []
#    for i in lst2: #originally it was 'for i in lst:'
#        lst3.append(','.join(i)+'\n')
        
#    lst4 = ','.join(lst3).replace('\n,', '\n')
    
missingbf1s = []
missing1f1s = []
missing2f1s = []
notmissingf1s = []
    
for i in lst[10:]:
    if i[3] == '0' and i[4] == '0':  #i.e. both F1 are missing
        missingbf1s.append(i[0])
    elif i[3] == '0' and i[4] != '0': #i.e. the first F1 is missing
        missing1f1s.append(i[0])
    elif i[3] != '0' and i[4] == '0': #i.e. the second F1 is missing
        missing2f1s.append(i[0])
    else:
        notmissingf1s.append(i[0])
          
missingbf1st = ','.join(missingbf1s)
missing1f1st = ','.join(missing1f1s)
missing2f1st = ','.join(missing2f1s)
notmissingf1st = ','.join(notmissingf1s)

lz = lst2[:10]
    
ID = []
p0 = []
f1 = []
f2 = []
p0f1 = []
f1f2 = []
keys = []
aL = []

lw = []
    
for i in lst2[10:]: #only import the array starting from the genotype rows
   
    if i.split(',')[0] in notmissingf1s:  #now we need to check that there are no mis-typed F1s
            
        ID.append(i.split(',')[0])
        p0.append(i.split(',')[1]+i.split(',')[2])
        f1.append(i.split(',')[3]+i.split(',')[4])
        p0f1.append(i.split(',')[1]+i.split(',')[2]+i.split(',')[3]+i.split(',')[4])
        f2.append(','.join(i.split(',')[5:]))
        f1f2.append(','.join(i.split(',')[3:]))
        keys.append(i.split(',')[0]+','+i.split(',')[1]+i.split(',')[2]+','+i.split(',')[3]+','+i.split(',')[4])
        aL.append(','.join(i.split(',')).split(','))
                
        d = dict(zip(keys, f2))
        df2 = dict(zip(ID, f2))
        df1f2 = dict(zip(ID, f1f2))
        df1 = dict(zip(ID, f1))
        daL = dict(zip(ID, aL))
            
        f1aaaa = [ i for i in ID if df1[i] == 'aaaa']
        f1aaab = [ i for i in ID if df1[i] == 'aaab']
        f1abaa = [ i for i in ID if df1[i] == 'abaa']
        f1abbb = [ i for i in ID if df1[i] == 'abbb']
        f1bbbb = [ i for i in ID if df1[i] == 'bbbb']
        f1abab = [ i for i in ID if df1[i] == 'abab']
        
        nac_aaaa = [i for i in f1aaaa if 'ab' in df2[i]]
        nac_aaab = [i for i in f1aaab if 'bb' in df2[i]]
        nac_abaa = [i for i in f1abaa if 'bb' in df2[i]]
        nac_abbb = [i for i in f1abbb if 'aa' in df2[i]]
        nac_bbbb = [i for i in f1aaaa if 'ab' in df2[i]]            
            
        for j in nac_aaab:
            a = ','.join(daL[j]).split(',')[5:].count('ab') + 2*(','.join(daL[j]).split(',')[5:].count('aa'))
            b = ','.join(daL[j]).split(',')[5:].count('ab') +2*(','.join(daL[j]).split(',')[5:].count('bb'))
            if a+b == 0:
                pass
            else:
                freq_a = float(a)/(a+b)
                freq_b = 1-freq_a
                    
                ############ LRT ##############
                            
                MLE_ab = (freq_a**a)*(freq_b**b)
                MLE_05 = (.5**a)*(.5**b) 
                MLE_075 = (.75**a)*(.25**b)
                MLE_025 = (.25**a)*(.75**b)
                            
                LRT_05 = 2*(math.log(MLE_ab)-math.log(MLE_05))
                LRT_075 = 2*(math.log(MLE_ab)-math.log(MLE_075))
                LRT_025 = 2*(math.log(MLE_ab)-math.log(MLE_025))
                
                        ############ Poisson ##############
                            
                lambda_05 = float(0.5*(a+b)) #lambda is the expected number of "a" give each test frequency for a (i.e. 0.5, 0.75, 0.25)
                lambda_075 = float(.75*(a+b))
                lambda_025 = float(.25*(a+b))
                            
                Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
                Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
                Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
                        
                        ############## if i in nac_aaaa ############
                if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                    lw.append(','.join(daL[j][:3]+['ab,ab']+daL[j][5:]))
                elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                    lw.append(','.join(daL[j][:3]+['aa,ab']+daL[j][5:])) #I keep the male F1 as a het
                elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                    lw.append(','.join(daL[j][:3]+['bb,ab']+daL[j][5:])) #I keep the male F1 as a het
                else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                    pass  

                

# <codecell>

lw[3:13]

# <codecell>

len(notmissingf1s)

# <codecell>

notmissingf1s[:10]

# <codecell>


