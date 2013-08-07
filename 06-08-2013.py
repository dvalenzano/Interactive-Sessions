# Goal: to infer F1 genotypes based on F2 genotypes



import math
import numpy
import scipy



fam_1dot1 = open('/Users/DValenzano/Dropbox/tmp/inferrednew_fam_1.1.csv', 'rU').read()



ls = []
for i in fam_1dot1.split('\n'):
    ls.append(i.split(','))

ls = ls[:-2]

lst = zip(*ls) #transpose the matrix and creates a list of tuples

lst2 = []
for i in lst:
   lst2.append(','.join(i))
    
lst3 = []
for i in lst:
    lst3.append(','.join(i)+'\n')
    
lst4 = ','.join(lst3).replace('\n,', '\n')



# We need a *list of marker names where both the F1 genotypes are missing*. Unless these same markers are sex linked in some of the families where the F1 genotypes are not missing, these markers won't be used to calculate sex-specific linkage since the F1 genotype attribution is arbitrary.  



missingf1s = []
for i in lst[9:]:
  if i[3] and i[4] == '0':
        missingf1s.append(i[0])
missingf1st = ','.join(missingf1s)



# **Now F1 genotype inference**:
# If both F1 are missing and the grandparents are aaxab or abxaa:
# The rationale here is that if the frequency of "a" and "b" in the F2 is the same, then both F1 are "ab". 
# Whereas, if the frequency of "a" is 3 times "b", then the F1 genotypes are "ab" and "aa", or "aa" and "ab". To resolve this problem we call het the male F1 subject.
# To tell if the freq of "a" is the same as the freq of "b" we'll use the **likelihood ratio test** (LRT) and the Poisson method together. 
# If it's not possible to assess F1 genotypes, then we leave the marker out. This will happen mostly in families with low number of F2 individuals, where LRT will fail. 
# Arbitrarily, I will not consider F2 genotypes with genotyping coverage below 10 genotypes (i.e. 20 alleles). 



#calculation frame

lz = lst2[:9]
for i in lst2[9:]: #only import the array starting from the genotype rows

    if i.split(',')[0] not in missingf1s: #exclude from the analysis the individuals that have at least one genotype available for the F1
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
            
        lambda_05 = float(0.5*(a+b))
        lambda_075 = float(.75*(a+b))
        lambda_025 = float(.25*(a+b))
            
        Poi_05 = ((lambda_05**a)*(math.exp(-(lambda_05))))/math.factorial(a)
        Poi_075 = ((lambda_075**a)*(math.exp(-(lambda_075))))/math.factorial(a)
        Poi_025 = ((lambda_025**a)*(math.exp(-(lambda_025))))/math.factorial(a)
            
        ############## F1 inference #################
            
        if a+b >15: #i.e. if there are enough genotypes to run the analysis - this line of code drops a lot of markers
                
            if LRT_05 is min(LRT_05, LRT_075, LRT_025) and LRT_05 < 3.841 and Poi_05 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = freq_b model is the most likely
                lz.append(','.join(i.split(',')[:3]+['ab,ab']+i.split(',')[5:]))
            elif LRT_075 is min(LRT_05, LRT_075, LRT_025) and LRT_075 < 3.841 and Poi_075 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 0.75 model is the most likely
                lz.append(','.join(i.split(',')[:3]+['aa,ab']+i.split(',')[5:])) #I keep the male F1 as a het
            elif LRT_025 is min(LRT_05, LRT_075, LRT_025) and LRT_025 < 3.841 and Poi_025 is max(Poi_05, Poi_075, Poi_025): #if the freq_a = 25 model is the most likely
                lz.append(','.join(i.split(',')[:3]+['bb,ab']+i.split(',')[5:])) #I keep the male F1 as a het
            else: #this includes the possibility of aaxaa F1, which are useless from a linkage standpoint, and therefore removed from the analysis
                pass
        else:
            pass
                
#    LOD = math.log10(MLE_ab/MLE_05)
#    p_val = 1.0/(10**(LOD))
#    out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
#    ls.append(out)
#  return 'Marker'+'\tLRT\tLOD\tp_val\n'+','.join(ls)[:-1].replace('\n,','\n')


print 'lst2\'s length is: %s lines\nlz\'s length is: %s lines'  %(len(lst2), len(lz))


# Then it's the case where only one F1 genotype is missing. 
# 
# **WE NEED TO FIND A WAY TO STORE THE INFO OF THE NAMES OF THE MARKERS FOR WHICH THE GENOTYPE HAS BEEN INFERRED** 
# 
# this is the string *missingf1st*




