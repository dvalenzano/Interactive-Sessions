
# coding: utf-8

# In[1]:

m7 = open('/Users/dvalenzano/Downloads/Fam14and7chr9union/fam_7m_chr9_new.rcd.csv', 'rU').read()
m14 = open('/Users/dvalenzano/Downloads/Fam14and7chr9union/fam_14m_chr9_new.rcd.csv', 'rU').read()
m7om = open('/Users/dvalenzano/Downloads/Fam14and7chr9union/fam_7m_OneMap.txt', 'rU').read()
m14om = open('/Users/dvalenzano/Downloads/Fam14and7chr9union/fam_14m_OneMap.txt', 'rU').read()


# In[4]:

mar7 = [i.split(',')[0] for i in m7.split('\n')[1:]]
mar14 = [i.split(',')[0] for i in m14.split('\n')[1:]]


# In[9]:

from sets import Set
mar7s = Set(mar7)
mar14s = Set(mar14)

marU = mar7s | mar14s #union of the markers in fam 7 and 14


# In[12]:

marUl = list(marU)


# In[20]:

m7om_sigov = [i+'\n' for i in m7om.split('\n') if i.split('\t')[0][1:] in marUl ]


# In[31]:

m7om_sigovj = str(len(m7om_sigov[0].split('\t')[-1].split(',')))+' '+str(len(m7om_sigov))+'\n'+','.join(m7om_sigov).replace('\n,','\n')


# In[36]:

m14om_sigov = [i+'\n' for i in m14om.split('\n') if i.split('\t')[0][1:] in marUl ]


# In[37]:

m14om_sigovj = str(len(m14om_sigov[0].split('\t')[-1].split(',')))+' '+str(len(m14om_sigov))+'\n'+','.join(m14om_sigov).replace('\n,','\n')


# In[39]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/f7om_LG9_consolid.csv', 'w')
z.write(m7om_sigovj)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/f14om_LG9_consolid.csv', 'w')
z.write(m14om_sigovj)
z.close()


# In[ ]:



