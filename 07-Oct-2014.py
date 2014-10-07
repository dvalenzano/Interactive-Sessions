
# coding: utf-8

# In[1]:

# First, I need to find the q values for sex in all the markers
rfgo = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/go_qval.tsv', 'rU').read()
rfaao = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/aao_qval.tsv', 'rU').read()


# In[12]:

import math
str((-1)*math.log(float(i[2])))
gk = [ i.split()[0][1:] for i in rfgo.split('\n')[1:-1]]
gv = [ str((-1)*math.log(float(i.split()[1]))).replace('-0.0','0.0') for i in rfgo.split('\n')[1:-1]]
gd = dict(zip(gk, gv))

aak = [ i.split()[0][1:] for i in rfaao.split('\n')[1:-1]]
aav = [ str((-1)*math.log(float(i.split()[1]))).replace('-0.0','0.0') for i in rfaao.split('\n')[1:-1]]
aad = dict(zip(aak, aav))


# In[4]:

# Then, I need to add this column to the r input files
gr = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/ReAutoReqtlresults/gdays2_tab.csv', 'rU').read()
aar = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aadays2_tab.csv', 'rU').read()


# In[20]:

gdk = [i.split(',')[0] for i in gr.split('\n')[1:-1]]
gdv = [','.join(i.split(',')[1:]) for i in gr.split('\n')[1:-1]]
gdd = dict(zip(gdk, gdv))

aadk = [i.split(',')[0] for i in aar.split('\n')[1:-1]]
aadv = [','.join(i.split(',')[1:]) for i in aar.split('\n')[1:-1]]
aadd = dict(zip(aadk, aadv))


# In[23]:

gdays3 = [gr.split('\n')[0]+',neg_log(qval)_sex\n']+[i.split(',')[0]+','+gdd[i.split(',')[0]]+','+gd[i.split(',')[0]]+'\n' for i in gr.split('\n')[1:-1]]
aadays3_0 = [aar.split('\n')[0]+',neg_log(qval)_sex\n']+[i.split(',')[0]+','+aadd[i.split(',')[0]]+','+aad[i.split(',')[0]]+'\n' for i in aar.split('\n')[1:-1]]


# In[24]:

gdays3 = ','.join(gdays3_0).replace('\n,','\n')
aadays3 = ','.join(aadays3_0).replace('\n,','\n')


# In[28]:

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/gdays3_tab.csv', 'w')
z.write(gdays3)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Oct2014/aadays3_tab.csv', 'w')
z.write(aadays3)
z.close()


# In[ ]:



