
# coding: utf-8

# Goal1: open data file and save it as 'p_red'

# In[12]:

p_red = open('/Users/dvalenzano/Desktop/Pisa_2015/Pisa0red.csv', 'rU').read()


# Goal2: replace ';' in ',' and split the string in a list

# In[16]:

p_red= p_red.replace(';',',')
p_rl = p_red.split('\n')


# Example 1: select only individuals that have phenotype col=1 (we use list comprehension)  
# In this way we are building sub-matrices

# In[25]:

color_1 = [i for i in p_rl if i.split(',')[3]=='1']
# Now we have a submatrix with only col=1 (yellow)
color_2 = [i for i in p_rl if i.split(',')[3]=='2']
# Now we have a submatrix with only col=2 (red)


# Example 2: subset the matrix in a male-only or female-only matrix

# In[30]:

sex_1 = [i for i in p_rl if i.split(',')[1]=='1']
# Now we have a submatrix with only sex=1 (males)
sex_2 = [i for i in p_rl if i.split(',')[1]=='2']
# Now we have a submatrix with only sex=2 (females)


# Analysis: for each marker, calculate the occurrences and frequencies of 'a' and 'b' alleles

# In[41]:

# First: transpose matrix
p_rlt = zip(*[i.split(',') for i in p_rl])
# the previous function saves the new matrix as a tuple
# let's turn the tuple into a list of lists (i.e. an array)
p_rltl = [list(i) for i in p_rlt]


# In[88]:

#Example: marker 43975 corresponds to the 6th column in the initial matrix  
#    which, for python, corresponds to the 5th column (it starts from 0)
ma = [2*p_rltl[5].count('aa')+p_rltl[5].count('ab')] #count of 'a'
mb = [2*p_rltl[5].count('bb')+p_rltl[5].count('ab')] #count of 'b'
fa = float(ma[0])/float(ma[0]+mb[0]) #frequency of 'a'
fb = 1.0-fa #frequency of 'b'
import math
MLE = (fa**float(ma[0]))*(fb**float(mb[0]))
ML0 = 0.5**(float(ma[0])+float(mb[0]))
LRT = 2.0*(math.log(MLE)-math.log(ML0))
LOD = LRT/4.6


# In[105]:

# More in general:
def LOD(inp): #inp is a given marker full genotype
    ma = [2*inp.count('aa')+inp.count('ab')] #count of 'a'
    mb = [2*inp.count('bb')+inp.count('ab')] #count of 'b'
    fa = float(ma[0])/float(ma[0]+mb[0]) #frequency of 'a'
    fb = 1.0-fa #frequency of 'b'
    import math
    MLE = (fa**float(ma[0]))*(fb**float(mb[0]))
    ML0 = 0.5**(float(ma[0])+float(mb[0]))
    LRT = 2.0*(math.log(MLE)-math.log(ML0))
    LOD = LRT/4.6
    return str(LOD)


# In[119]:

# Below I use the p_rltl matrix, which is the transposed big matrix we started with. 
# For the analyses on color and sex you will need to use as an input the sex or col matrices. 

lods = [ LOD(i) for i in p_rltl[5:]] #lod scores for all the markers
markers = [ i[0] for i in p_rltl[5:]] #list of markers
lodtab = ['marker,LODscore\n']+[ ','.join(list(i))+'\n' for i in zip(markers, lods) ] 


# In[121]:

tab = ','.join(lodtab).replace('\n,','\n') #this table shows the lod score for each marker


# In[ ]:

z = open('/Users/dvalenzano/Desktop/Pisa_2015/lodtab.csv', 'w') 
#here you can write whichever path for the file you want/need to save
z.write(tab)
z.close()

