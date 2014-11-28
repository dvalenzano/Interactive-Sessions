
# coding: utf-8

# Goal: to plot p-values calculated with plink on LG3 (rqtl map) with a manhattan plot on R

# In[8]:

gfile = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/mal/fam_7m_sqtl.assoc.linear', 'rU').read()
lmap = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read().replace('"','')


# In[9]:

sig7m = [ i.split()[1]+','+i.split()[-1] for i in gfile.split('\n')[:-1] ]


# In[23]:

lmap.split('\n')[:15]
lmk = [i.split(',')[0] for i in lmap.split('\n')[1:-1] ]
lmv = [i.split(',')[1:] for i in lmap.split('\n')[1:-1] ]
ld = dict(zip(lmk, lmv))

sig7mk = [i.split(',')[0] for i in sig7m[1:] ]
sig7mv = [i.split(',')[1] for i in sig7m[1:] ]
sig7md = dict(zip(sig7mk, sig7mv))


# In[24]:

from sets import Set
shared = Set(lmk) & Set(sig7mk)


# In[46]:

fin = [ [i]+ld[i]+[sig7md[i]+'\n'] for i in shared ]
fins = sorted(fin, key=lambda x: (int(x[1]), (float(x[2]))))


# In[58]:

finsj = 'SNP,chr,pos,p-val\n'+','.join([','.join(i) for i in fins ]).replace('\n,','\n')


# In[59]:

z = open('/Volumes/group_dv/personal/DValenzano/Nov2014/G-cross/om_manhplot_in.csv','w')
z.write(finsj)
z.close()


# In[ ]:



