
# coding: utf-8

# In[1]:

f1mom = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/fam_1m_OneMap.txt', 'rU').read()


# In[7]:

from sets import Set

mar = float(f1mom.split('\n')[0].split()[1])
qtlepi = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/fam_1m.epi.qt', 'rU').read()


# In[34]:

prova1 = ','.join([i.split()[1]+'\n'+i.split()[3]+'\n' for i in qtlepi.split('\n')[1:-1]]).replace('\n,','\n')[:-1]


# In[37]:

len(Set(prova1.split('\n')))


# In[43]:

pvals = [i.split()[-1] for i in qtlepi.split('\n')[1:-1]]


# In[52]:

pvalsf = map(float, pvals)
import numpy


# In[83]:

numpy.percentile(pvalsf, 1)


# 4.730000000000002e-08 is the p-value of 0.05

# In[8]:

qtlepi2 = qtlepi.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepi.split('\n')[1:-1] if float(i.split()[6]) < 0.01/mar ]).replace('\n,','\n')              


# In[20]:

inpl = ','.join([ i.split()[1] +'\n'+i.split()[3]+'\n' for i in qtlepi2.split('\n')[1:-1]]).replace('\n,','\n')


# In[23]:

new_ominpe = str(len(qtlepi2.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(inpl.split('\n')[:-1])))+'\n'+','.join([ i+'\n' for i in f1mom.split('\n')[1:] if i.split('\t')[0][1:] in Set(inpl.split('\n')[:-1])]).replace('\n,','\n')


# In[84]:

qtlepi3 = qtlepi.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepi.split('\n')[1:-1] if float(i.split()[6]) < 4.1717200000000004e-10 ]).replace('\n,','\n')           
inpl3 = ','.join([ i.split()[1] +'\n'+i.split()[3]+'\n' for i in qtlepi3.split('\n')[1:-1]]).replace('\n,','\n')
new_ominpe3 = str(len(f1mom.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(inpl3.split('\n')[:-1])))+'\n'+','.join([ i+'\n' for i in f1mom.split('\n')[1:] if i.split('\t')[0][1:] in Set(inpl3.split('\n')[:-1])]).replace('\n,','\n')


# In[ ]:

import sys
from sets import Set
import numpy

inp = raw_input('What family would you like to analyze?\n')
inpg = raw_input('What gender would you like to analyze? [mal, fem]\n')
inpgi = inpg[0]

omfam = '/Volumes/group_dv/personal/DValenzano/May2014/AAo/%s/fam_%s%s_OneMap.txt' % (inpg, inp, inpgi)

ominp = open(omfam, 'rU').read()
mar = float(ominp.split('\n')[0].split()[1])

qtlepi = '/Volumes/group_dv/personal/DValenzano/May2014/AAo/%s/fam_%s%s.epi.qt' % (inpg, inp, inpgi)               
qtlepiinp = open(qtlepi, 'rU').read()                                                                                                                                                  
pvals = [i.split()[-1] for i in qtlepiinp.split('\n')[1:-1]]
pvalsf = map(float, pvals)
thr = numpy.percentile(pvalsf, 1)

#qtlepiinp2 = qtlepiinp.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepiinp.split('\n')[1:-1] if float(i.split()[6]) < 0.01/mar ]).replace('\n,','\n')                            
#inpl = ','.join([ i.split()[1] +'\n'+i.split()[3]+'\n' for i in qtlepiinp2.split('\n')[1:-1]]).replace('\n,','\n')
#new_ominpe = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(inpl.split('\n')[:-1])))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in Set(inpl.split('\n')[:-1])]).replace('\n,','\n')

qtlepi3 = qtlepiinp.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepiinp.split('\n')[1:-1] if float(i.split()[6]) < 0.01*thr ]).replace('\n,','\n')           
inpl3 = ','.join([ i.split()[1] +'\n'+i.split()[3]+'\n' for i in qtlepi3.split('\n')[1:-1]]).replace('\n,','\n')
new_ominpe3 = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(inpl3.split('\n')[:-1])))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in Set(inpl3.split('\n')[:-1])]).replace('\n,','\n')

out = '/Volumes/group_dv/personal/DValenzano/May2014/AAo/%s/f%s_om%s_epi.txt' % (inpg, inp, inpgi)

z = open(out, 'w')                                                                                                                                                                                      
z.write(new_ominpe3)                                                                                                                                                                                     
z.close()    

