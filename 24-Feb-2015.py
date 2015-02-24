
# coding: utf-8

# Goal: to run 10,000 boostraps on surival between males and females in the F2 of cross 1

# In[1]:

inp = open('/Volumes/group_dv/personal/DValenzano/Feb2015/top-sqtl_mf.csv', 'rU').read()


# In[82]:

inp2 = inp.replace('\t',',')
inp3 = [i+',1' for i in inp2.split('\n') if i.split(',')[-1] != '0']


# In[84]:

m0 = [i for i in inp3 if i.split(',')[0]=='1' ]
f0 = [i for i in inp3 if i.split(',')[0]=='2' ]


# In[85]:

len(f0)


# In[86]:

import math
import random

def bs(inp, size, cycles): #this function does the bootstrapping job
  inp = inp[1:-1]
  ls = []
  for i in range(cycles):
    ls.append(random.sample(inp, size))
#  return ls
  ls2 = [j+f0 for j in ls]
  return ls2


# In[87]:

bs10k= bs(m0, 51, 10000)


# In[144]:

rn = range(len(bs10k))
ls = []
#for i in bs10k:
#    for j in rn:
#        for k in i:
#            ls.append(k+','+j)
for i in rn:
    ls.append([j+','+str(i)+'\n' for j in  bs10k[i]])


# In[145]:

fin = [','.join(i).replace('\n,','\n') for i in ls]


# In[146]:

fin1 = 'sex,days,genot,status,group\n' +','.join(fin).replace('\n,','\n')


# In[147]:

z = open('/Volumes/group_dv/personal/DValenzano/Feb2015/list_46347.csv','w')
z.write(fin1)
z.close()


# Goal: to generate an R input file for the p-value calculation for the Logrank test on 10000 bootstraps with equal numbers of males and females

# In[181]:

rng = range(10000)
rng2 = [str(i) for i in rng]
rng3 = ['=='+i for i in rng2]


# In[189]:

cell = ['prova <- subset(list2, list2$group==)\na <- survdiff(Surv(days, status) ~ genot, data=prova)\nb <- c(1-pchisq(a$chisq, length(a$n)-1), b)']
cell10k = cell*10000


# In[190]:

prova = [ cell[0].replace('==', i) for i in rng3]


# In[191]:

prova2 = ','.join([i+'\n' for i in prova ]).replace('\n,','\n')


# In[192]:

z = open('/Volumes/group_dv/personal/DValenzano/Feb2015/run-on-R.csv','w')
z.write(prova2)
z.close()


# In[ ]:



