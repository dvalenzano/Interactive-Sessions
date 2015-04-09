# GOAL: to generate a matrix that has 190 markers from the initial G cross panel for practice in Pisa during hands on session
gogen = open('/Volumes/group_dv/personal/DValenzano/Nov2013/goped7.csv', 'rU').read()


# In[30]:

mrks0 = gogen.split('\n')[0].split(',')[10:]
P01g = gogen.split('\n')[1].split(',')[10:]
P02g = gogen.split('\n')[2].split(',')[10:]


# In[40]:

gen0 = zip(P01g, P02g)


# In[47]:

gen1 = [','.join(list(i)) for i in gen0]


# In[48]:

d = dict(zip(mrks0, gen1))


# In[50]:

hmz = [i for i in mrks0 if d[i]=='aa,bb'] #this way I only select the markers that are homoz in both P0


# In[52]:

len(hmz)


# In[ ]:

g = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read() #all the markers sorted in LG
g = g.replace('"', '')
g = g.split('\n')[1:-1]


# In[58]:

gk = [i.split(',')[0] for i in g ]
gv = [i.split(',')[1:] for i in g ]
gd = dict(zip(gk, gv))


# In[60]:

from sets import Set
hom = Set(gm) & Set(gk)


# In[73]:

hom_2 = list(hom)[1:]
homg = [i+','+','.join(gd[i]) for i in hom2 ]


# In[74]:

import random
g2 = random.sample(homg, 190)
g2s = sorted(g2, key=lambda row: (int(row.split(',')[1]), float(row.split(',')[2])))


# In[114]:

g2sm = [i.split(',')[0] for i in g2s ] #these are the markers corresponding to the selected markers


# In[78]:

gnew = open('/Volumes/group_dv/personal/DValenzano/Apr2015/goped7_2.csv', 'rU').read()


# In[85]:

len(gnew.split('\n')[0].split(';'))


# In[92]:

gnew2 = [gnew.split('\n')[0]] + [i for i in gnew.split('\n')[1:] if float(i.split(';')[9:].count('0'))/8408 <= 0.5 ] #select the individuals with more genotypes


# In[93]:

gnew3 = [i.split(';') for i in gnew2 ]


# In[96]:

gnew4 = zip(*gnew3)


# In[99]:

gnew5 = [ list(i) for i in gnew4 ]


# In[100]:

len(gnew5[0])


# In[102]:

gnew6 = [i  for i in gnew5 if float(i.count('0'))/176 <= 0.5 ]


# In[104]:

gnew7 = zip(*gnew6)


# In[105]:

gnew8 = [','.join(list(i))+'\n' for i in gnew7]


# In[111]:

gnew9 = ','.join(gnew8).replace('\n,','\n') #this is the big genotype file without worse genotypes and individuals - still, contains a lot of markers


# In[110]:

z = open('/Volumes/group_dv/personal/DValenzano/Apr2015/Pisa0.csv','w')
z.write(gnew9)
z.close()


# In[128]:

#Now I select a submatrix with only 190 markers, randomly chosen above
gnew6red = gnew6[:8]+[i for i in gnew6 if i[0] in g2sm ]
gnew6red = [i for i in gnew6red if i[0] != 'bl']
gnew6red = [i for i in gnew6red if i[0] != 'mother']
gnew6red = [i for i in gnew6red if i[0] != 'father']


# In[129]:

gnew7red = zip(*gnew6red)
gnew8red = [','.join(list(i))+'\n' for i in gnew7red]
gnew9red = ','.join(gnew8red).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Apr2015/Pisa0red.csv','w')
z.write(gnew9red)
z.close()


# In[ ]:



