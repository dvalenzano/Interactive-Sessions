
# coding: utf-8

# In[55]:

sig = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/fam_7m_sqtl_sig', 'rU').read()
allm = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/fam_7m_sqtl.assoc.linear', 'rU').read()
LGs = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/f7m_LGs.dat', 'rU').read()


# In[56]:

LGss = [ i for i in LGs.split('\n\n')]


# mcm has marker name and position in cM, LG by LGs

# In[57]:

mcm = [ [ i.split()[1:3] for i in LGss[j].split('\n') ] for j in range(len(LGss))]


# keys = [ i.split()[1] for i in sig.split('\n')[1:-1]]
# values = [ i.split()[-1] for i in sig.split('\n')[1:-1]]
# d = dict(zip(keys, values))

# In[58]:

keys = [ i.split()[1] for i in allm.split('\n')[1:-1]]
values = [ i.split()[-1] for i in allm.split('\n')[1:-1]]
d = dict(zip(keys, values))


# prova = [[','.join(mcm[j][i]+[d[mcm[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm[j])) ] for j in range(len(mcm))]

# In[75]:

allLGs = [','.join([','.join(mcm[j][i]+[d[mcm[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm[j])) ])[:-1].replace('\n,','\n') for j in range(len(mcm))]


# In[77]:

LG1 = allLGs[0]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG1', 'w')
z.write(LG1)

LG2 = allLGs[1]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG2', 'w')
z.write(LG2)

LG3 = allLGs[2]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG3', 'w')
z.write(LG3)

LG4 = allLGs[3]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG4', 'w')
z.write(LG4)

LG5 = allLGs[4]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG5', 'w')
z.write(LG5)

LG6 = allLGs[5]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG6', 'w')
z.write(LG6)

LG7 = allLGs[6]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG7', 'w')
z.write(LG7)

LG8 = allLGs[7]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG8', 'w')
z.write(LG8)

LG9 = allLGs[8]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG9', 'w')
z.write(LG9)

LG10 = allLGs[9]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG10', 'w')
z.write(LG10)

LG11 = allLGs[10]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG11', 'w')
z.write(LG11)

LG12 = allLGs[11]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG12', 'w')
z.write(LG12)

LG13 = allLGs[12]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG13', 'w')
z.write(LG13)

LG14 = allLGs[13]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG14', 'w')
z.write(LG14)

LG15 = allLGs[14]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG15', 'w')
z.write(LG15)

LG16 = allLGs[15]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG16', 'w')
z.write(LG16)

LG17 = allLGs[16]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG17', 'w')
z.write(LG17)

LG18 = allLGs[17]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG18', 'w')
z.write(LG18)

LG19 = allLGs[18]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG19', 'w')
z.write(LG19)

LG20 = allLGs[19]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG20', 'w')
z.write(LG20)

LG21 = allLGs[20]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG21', 'w')
z.write(LG21)

LG22 = allLGs[21]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG22', 'w')
z.write(LG22)

LG23 = allLGs[22]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG23', 'w')
z.write(LG23)

LG24 = allLGs[23]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG24', 'w')
z.write(LG24)

LG25 = allLGs[24]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG25', 'w')
z.write(LG25)

LG26 = allLGs[25]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG26', 'w')
z.write(LG26)

LG27 = allLGs[26]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG27', 'w')
z.write(LG27)


# In[79]:

LG27 = allLGs[26]
z = open('/Users/dvalenzano/Dropbox/tmp/15-Apr-14/LG27', 'w')
z.write(LG27)


# In[ ]:



