# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

gonj = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/goped7.csv', 'rU').read()


gonj = gonj.replace('Ffam', 'F_f').replace('Mfam', 'M_f') #I needed to add this line because splitting by "fam" was not giving the expected result - check out the F1 Catalog-IDs for this matrix and you'll understand the problem
gos = gonj.split('fam')
keys = gos[0].split(',')[10:]
keys= keys[:-1]+[keys[-1][:-1]] #the last element had a \n attached to it!!

values = []

for i in range(10, len(gos[0].split(','))):
               values.append(gos[1].split('\n')[0].split(',')[i]+gos[1].split('\n')[1].split(',')[i])
d = dict(zip(keys, values)) # A dictionary that goes like this: { '8563': 'aabb', '63406': 'aabb', ...}

#lst = []

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

#  f1f = [] #this returns the F1 female values
#  for i in keys:
#    if df1f[i] == '0':
#      if d[i] == 'aabb': 
#        f1f.append('ab')
#      else:
#        f1f.append(df1f[i])
#    else:
#      f1f.append(df1f[i])
        
#  f1m = [] #this returns the F1 male values
#  for i in keys:
#    if df1m[i] == '0':
#      if d[i] == 'aabb': 
#        f1m.append('ab')
#      else:
#        f1m.append(df1m[i])
#    else:
#      f1m.append(df1m[i])

  f1f = [] #this returns the F1 female values
  f1m = [] #this returns the F1 male values
  for i in keys:
#    if df1m[i] == '0':
     if d[i] == 'aabb': 
        f1m.append('ab')
        f1f.append('ab')
#      else:
#        f1m.append(df1m[i])
#    else:
#      f1m.append(df1m[i])
     else:
        f1m.append(df1m[i])
        f1f.append(df1f[i])    #I fixed the wrong code from 16-Jan-2013



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

  currentfamily = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/inferrednew_fam_%s.csv' % gos[f].split('\n')[0].split(',')[0]
  z = open(currentfamily, 'w') 
  z.write(lsj)
  z.close()

# <codecell>

import math
import numpy
import scipy

input = open('/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/inferred-list.txt', 'rU').read() #inferred-list.txt is a file that contains all the paths to the inferred files:

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
                
                
    missingbf1s = []
    missing1f1s = []
    missing2f1s = []
    notmissingf1s = []
    
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
            
    lw = []
                      
    ID = []
    p0 = []
    f1 = []
    f2 = []
    p0f1 = []
    f1f2 = []
    keys = []
    aL = []
    
    for i in lst2[10:]: #only import the array starting from the genotype rows
        
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
                if i.split(',')[0] in missingbf1s: 
                    if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                    elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                        lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                    elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
    #                    lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                        if ','.join(i.split(',')[1:3])=='ab,ab':
                            lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #here I am reverting bbab into aaab
    #                        lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'aa', the only possible model is a female 'bb'
                        else:
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab'       
                            
                    else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                        pass
                            
                        ############## below the case with the first F1 genotype missing ############
                elif i.split(',')[0] in missing1f1s:
                    if i.split(',')[4] == 'aa':
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'aa', then the female got to be 'bb'
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #I am imposing the F1 genotypes
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab'])+','+i.split(',')[4]+','+','.join(i.split(',')[5:]).replace('bb','ab')) #given that the male is 'aa', the female has to be 'ab'
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                             if ','.join(i.split(',')[1:3])=='ab,ab':
                                 lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #here I am reverting a '
    #                        lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'aa', the only possible model is a female 'bb'
                             else:
                                 lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab'                        
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
                    elif i.split(',')[4] == 'ab':
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab']+i.split(',')[4:])) #given that the male is 'ab', then the female got to be 'ab'
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['aa'])+','+i.split(',')[4]+','+','.join(i.split(',')[5:]).replace('bb','ab')) #given that the male is 'ab', the female has to be 'aa'
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'ab', the female got to be 'bb'
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                 lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
    #                       lz.append(','.join(i.split(',')[:3]+['bb']+i.split(',')[4:])) #given that the male is 'ab', the female got to be 'bb'                        
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
                    elif i.split(',')[4] == 'bb':
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['aa']+i.split(',')[4:])) #given that the male is 'bb', then the female got to be 'aa'
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force 'abab' F1 model
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['aa']+i.split(',')[4:])) #given that the male is 'bb', the only possible model is a female 'aa'
                            lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','ab')) #force F1 'aaab' model
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['ab']+i.split(',')[4:])) #given that the male is 'bb', the only possible model is a female 'ab'
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                 lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
                                
                        ############## below the case with the second F1 genotype missing ############
                elif i.split(',')[0] in missing2f1s:
                    if i.split(',')[3] == 'aa':
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
    #                        lz.append(','.join(i.split(',')[:4]+['bb']+i.split(',')[5:])) #given that the female is 'aa', then the male got to be 'bb'
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the F1 'abab' model                    
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')[:4]+['ab']+i.split(',')[5:])) #given that the male is 'aa', the female has to be 'ab'
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                 lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
    #                        lz.append(','.join(i.split(',')[:4]+['bb']+i.split(',')[5:])) #given that the male is 'aa', the only possible model is a female 'bb'
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
                    elif i.split(',')[3] == 'ab':
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:4]+['ab']+i.split(',')[5:])) #given that the male is 'ab', then the female got to be 'ab'
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')[:4]+['aa']+i.split(',')[5:])) #given that the male is 'ab', the female has to be 'aa'
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                 lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
    #                        lz.append(','.join(i.split(',')[:4]+['bb']+i.split(',')[5:])) #given that the male is 'ab', the female got to be 'bb'
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
                    elif i.split(',')[3] == 'bb':
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #forcing the F1 'abab' model                        
    #                        lz.append(','.join(i.split(',')[:4]+['aa']+i.split(',')[5:])) #given that the male is 'bb', then the female got to be 'aa'
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,aa']+i.split(',')[5:])) #forcing the F1 'abaa' model        
    #                        lz.append(','.join(i.split(',')[:4]+['aa']+i.split(',')[5:])) #given that the male is 'bb', the only possible model is a female 'aa'
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
    #                        lz.append(','.join(i.split(',')[:4]+['ab']+i.split(',')[5:])) #given that the male is 'bb', the only possible model is a female 'ab'
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                 lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
            
            
                elif i.split(',')[0] in notmissingf1s:  #now we need to check that there are no mis-typed F1s
                
     
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
                                   
                    f1aaaa = [ j for j in ID if df1[j] == 'aaaa']
                    f1aaab = [ j for j in ID if df1[j] == 'aaab']
                    f1aabb = [ j for j in ID if df1[j] == 'aabb'] #new
                    f1abaa = [ j for j in ID if df1[j] == 'abaa']
                    f1abbb = [ j for j in ID if df1[j] == 'abbb']
                    f1bbaa = [ j for j in ID if df1[j] == 'bbaa']
                    f1bbbb = [ j for j in ID if df1[j] == 'bbbb']
                    f1abab = [ j for j in ID if df1[j] == 'abab']
                    f1bbab = [ j for j in ID if df1[j] == 'bbab']
                
                    nac_aaaa = []
                    ac_aaaa = []
                    for j in f1aaaa:
                        if 'ab' in df2[j]:
                            nac_aaaa.append(j)
                        elif 'bb' in df2[j]:
                            nac_aaaa.append(j)
                        else:
                            ac_aaaa.append(j)
            
                    nac_aaab = []
                    ac_aaab = []
                    for j in f1aaab:
                        if 'bb' in df2[j]:
                            nac_aaab.append(j)
                        else:
                            ac_aaab.append(j)        
                            
                    nac_aabb = []
                    ac_aabb = []
                    for j in f1aabb:
                        if 'bb' in df2[j]:
                            nac_aabb.append(j)
                        elif 'aa' in df2[j]:
                            nac_aabb.append(j)
                        else:
                            ac_aabb.append(j)  
                                
                    nac_abaa = []
                    ac_abaa = []
                    for j in f1abaa:
                        if 'bb' in df2[j]:
                            nac_abaa.append(j)    
                        else:
                            ac_abaa.append(j)        
                                
                    nac_abbb = []
                    ac_abbb = []
                    for j in f1abbb:
                        if 'aa' in df2[j]:
                            nac_abbb.append(j) 
                        else:
                            ac_abbb.append(j)
                                
                    nac_bbbb = []
                    ac_bbbb = []
                    for j in f1bbbb:
                        if 'aa' in df2[j]:
                            nac_bbbb.append(j) 
                        elif 'ab' in df2[j]:
                            nac_bbbb.append(j)
                        else:
                            ac_bbbb.append(j)
                            
                    nac_bbaa = []
                    ac_bbaa = []
                    for j in f1bbaa:
                        if 'aa' in df2[j]:
                            nac_bbaa.append(j) 
                        elif 'bb' in df2[j]:
                            nac_bbaa.append(j)
                        else:
                            ac_bbaa.append(j)
                            
                            
                    nac_bbab = []
                    ac_bbab = []
                    for j in f1bbab:
                        if 'aa' in df2[j]:
                            nac_bbab.append(j) 
                        else:
                            ac_bbab.append(j)
                      
                            
                    #                     ############## if i in nac_aaaa ############
    
                    if i.split(',')[0] in nac_aaaa:
                                                      
                       if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                           lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))#','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                       elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                           lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','ab')) #lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:]))
                       elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                           if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                           else:
                                 lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab'             
    #                       lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:]))#lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:]))  #I keep the male F1 as a het
                       else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                           pass  
                                                    
                    elif i.split(',')[0] in ac_aaaa:
                        pass #lz.append(i)
                    
                    
                                         ############## if i in nac_aaab ############
    
                    elif i.split(',')[0] in nac_aaab:#elif i.split(',')[0] in nac_aaab:
                               
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                           #  lz.append(','.join(daL[j][:3]+['ab,ab']+daL[j][5:]))
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            lz.append(','.join(i.split(',')[:5])+','+','.join(i.split(',')[5:]).replace('bb','aa'))
    #                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
    #                                    lz.append(','.join(daL[j][:3]+['bb,ab']+daL[j][5:]))
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass  
                
                    elif i.split(',')[0] in ac_aaab:  #elif i.split(',')[0] in ac_aaab:  
                        lz.append(i) #or maybe pass?
                        
                        
                        
                                         ############## if i in nac_aabb ############
    
                    elif i.split(',')[0] in nac_aabb:#elif i.split(',')[0] in nac_aabb:
                               
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                           #  lz.append(','.join(daL[j][:3]+['ab,ab']+daL[j][5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                           lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','ab')) #lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:]))
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa'))
    #                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
    #                                    lz.append(','.join(daL[j][:3]+['bb,ab']+daL[j][5:]))
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass  
                
                    elif i.split(',')[0] in ac_aabb:  #elif i.split(',')[0] in ac_aaab:  
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                           #  lz.append(','.join(daL[j][:3]+['ab,ab']+daL[j][5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                           lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','ab')) #lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:]))
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['aa,ab'])+','+','.join(i.split(',')[5:]).replace('bb','aa'))
    #                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
    #                                    lz.append(','.join(daL[j][:3]+['bb,ab']+daL[j][5:]))
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass  
                        
                   # else:
                   #     pass # lz.append(i) #or maybe pass?
                   
                        
                                        ############## if i in nac_abaa ############
                
                    elif i.split(',')[0] in nac_abaa:
                
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                            lz.append(','.join(i.split(',')[:3]+['ab,ab'])+','+','.join(i.split(',')[5:]).replace('bb','ab'))
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                            lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #I keep the male F1 as a het
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass  
        
                    elif i.split(',')[0] in ac_abaa:     
                        lz.append(i) #or perhaps pass?
                            
                            
                             
                                    ############## if i in nac_abbb ############
                        
                    elif i.split(',')[0] in nac_abbb:
                        
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')+['ab,ab']+i.split(',')[5:]))
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:]))#I keep the male F1 as a het
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
                            
                    elif i.split(',')[0] in ac_abbb:
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                        else:
                            pass #lz.append(i) #or pass?
                
                
                                     ############## if i in nac_bbbb ############
                    elif i.split(',')[0] in nac_bbbb:
                    
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')+['ab,ab']+i.split(',')[5:]))
    #                    elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
            #                        lz.append(','.join(i.spli(',')[:3]+['bb,ab']+i.split(','))) #I keep the male F1 as a het
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
    
                    elif i.split(',')[0] in ac_bbbb:         
                        pass #lz.append(i) #or pass?
                
                                    ############## if i in nac_bbaa ############
                
                    elif i.split(',')[0] in nac_bbaa:#elif i.split(',')[0] in nac_aabb:
                               
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                           #  lz.append(','.join(daL[j][:3]+['ab,ab']+daL[j][5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                           lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','ab')) #lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:]))
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','aa'))
    #                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
    #                                    lz.append(','.join(daL[j][:3]+['bb,ab']+daL[j][5:]))
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass  
                
                    elif i.split(',')[0] in ac_bbaa:  #elif i.split(',')[0] in ac_aaab:  
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                           #  lz.append(','.join(daL[j][:3]+['ab,ab']+daL[j][5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                           lz.append(','.join(i.split(',')[:3]+['ab,ab'])+','+','.join(i.split(',')[5:]).replace('bb','ab')) #lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:]))
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','aa'))
    #                        lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
    #                                    lz.append(','.join(daL[j][:3]+['bb,ab']+daL[j][5:]))
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass 
                
                        
                        
                                     ############## if i in nac_bbab ############
                    elif i.split(',')[0] in nac_bbab:
                    
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                        elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
    #                    elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
    #                        lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
                        elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                            if ','.join(i.split(',')[1:3])=='ab,ab':
                                lz.append(','.join(i.split(',')[:3]+['ab,aa'])+','+','.join(i.split(',')[5:]).replace('bb','aa')) #bbab becomes aaab if P0 are abxab
                            else:
                                lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:])) #force the model to become 'ab,ab' 
            #                        lz.append(','.join(i.spli(',')[:3]+['bb,ab']+i.split(','))) #I keep the male F1 as a het
                        else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                            pass
    
                    elif i.split(',')[0] in ac_bbab:         
                        if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                            lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
                        else:
                            pass
    #                    lz.append(i) #or pass?
                
                    else:
                        lz.append(i)

    lw = []
    for i in lz:
        lw.append(i.split(','))
        
    lwt = zip(*lw)
        
    lwt3 = []
    for i in lwt:
        lwt3.append(','.join(i)+'\n')
        
    lwt4 = ','.join(lwt3).replace('\n,', '\n')
    f2 = str(fl).split('new_')[1]
    output = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-'+f2 #fl[84:]                  
    z = open(output,'w')
    z.write(lwt4)
    z.close()

# <codecell>


# <codecell>


