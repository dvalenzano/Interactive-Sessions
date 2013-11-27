# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Goal: to infer all the F1 genotypes following the 08-Aug-2013 ipython session

# <codecell>

import math
import numpy
import scipy

fam_1dot1 = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferrednew_fam_1.1.csv', 'rU').read()

ls = []
for i in fam_1dot1.split('\n'):
    ls.append(i.split(','))

ls = ls[:-2]

lst = zip(*ls) #transpose the matrix and creates a list of tuples

lst2 = []
for i in lst:
    if i[0] != '3641': #this marker had 'c' alleles and was messing up with the analysis. I just removed it.
        lst2.append(','.join(i))
    
lst3 = []
for i in lst:
    lst3.append(','.join(i)+'\n')
    
lst4 = ','.join(lst3).replace('\n,', '\n')

missingbf1s = []
missing1f1s = []
missing2f1s = []
notmissingf1s = []

for i in lst[10:]:
  if i[3] == '0' and i[4] == '0':
        missingbf1s.append(i[0])
  elif i[3] == '0' and i[4] != '0':
        missing1f1s.append(i[0])
  elif i[3] != '0' and i[4] == '0':
        missing2f1s.append(i[0])
  else:
        notmissingf1s.append(i[0])

missingbf1st = ','.join(missingbf1s)
missing1f1st = ','.join(missing1f1s)
missing2f1st = ','.join(missing2f1s)
notmissingf1st = ','.join(notmissingf1s)

# <codecell>

print 'missingbf1s\'s length is: %s lines\nmissing1f1s\'s length is: %s lines\nmissing2f1s\'s length is: %s lines\nnotmissingf1s\'s length is: %s'  %(len(missingbf1s), len(missing1f1s), len(missing2f1s), len(notmissingf1s))

# <codecell>

lz = lst2[:10]
for i in lst2[10:]: #only import the array starting from the genotype rows

    if i.split(',')[0] in notmissingf1s: #exclude from the analysis the individuals that have at least one genotype available for the F1
        lz.append(i)
    
    else:
        a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
        b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
            
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

z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/F1inf_fam_1.1.csv','w')
z.write(lwt4)
z.close()

# <headingcell level=2>

# Here below I will do the analysis in iteration over all the input files like 'inferrednew_fam*.csv' - in progress!!

# <codecell>

import math
import numpy
import scipy

input = open('/Volumes/group_dv/personal/DValenzano/Nov2013/Go_families/inferred-list.txt', 'rU').read()
files = input.split('\n')

for file in files:
    fam_1dot1 = open(file, 'rU').read()
    
    ls = []
    for i in fam_1dot1.split('\n'):
        ls.append(i.split(','))
    
    ls = ls[:-2]
    
    lst = zip(*ls) #transpose the matrix and creates a list of tuples
    
    lst2 = []
    for i in lst:
        if i[0] != '3641': #this marker had 'c' alleles and was messing up with the analysis. I just removed it.
            lst2.append(','.join(i))
        
    lst3 = []
    for i in lst:
        lst3.append(','.join(i)+'\n')
        
    lst4 = ','.join(lst3).replace('\n,', '\n')
    
    missingbf1s = []
    missing1f1s = []
    missing2f1s = []
    notmissingf1s = []
    
    for i in lst[10:]:
      if i[3] == '0' and i[4] == '0':
            missingbf1s.append(i[0])
      elif i[3] == '0' and i[4] != '0':
            missing1f1s.append(i[0])
      elif i[3] != '0' and i[4] == '0':
            missing2f1s.append(i[0])
      else:
            notmissingf1s.append(i[0])
    
    missingbf1st = ','.join(missingbf1s)
    missing1f1st = ','.join(missing1f1s)
    missing2f1st = ','.join(missing2f1s)
    notmissingf1st = ','.join(notmissingf1s)
    lz = lst2[:10]
    for i in lst2[10:]: #only import the array starting from the genotype rows
    
        if i.split(',')[0] in notmissingf1s: #exclude from the analysis the individuals that have at least one genotype available for the F1
            lz.append(i)
        
        else:
            a = i.split(',')[5:].count('ab') + 2*(i.split(',')[5:].count('aa'))
            b = i.split(',')[5:].count('ab') +2*(i.split(',')[5:].count('bb'))
                
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
    output = 'inf'+file[-11:]                  
    z = open(output,'w')
    z.write(lwt4)
    z.close()



