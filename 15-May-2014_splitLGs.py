
# coding: utf-8

# First, family 1m

# In[47]:

allm = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/fam_1m_sqtl.assoc.linear', 'rU').read()
LGs = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LGs.txt', 'rU').read()


# In[48]:

LGss = [ i for i in LGs[:-1].split('\n\n')]

mcm = [ [ i.split()[1:3] for i in LGss[j].split('\n') ] for j in range(len(LGss))]

keys = [ i.split()[1] for i in allm.split('\n')[1:-1]]
values = [ i.split()[-1] for i in allm.split('\n')[1:-1]]
d = dict(zip(keys, values))


# In[49]:

allLGs = [','.join([','.join(mcm[j][i]+[d[mcm[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm[j])) ]).replace('\n,','\n') for j in range(len(mcm))]


# In[50]:

LG1 = allLGs[0]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG1', 'w')
z.write(LG1)

LG2 = allLGs[1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG2', 'w')
z.write(LG2)

LG3 = allLGs[2]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG3', 'w')
z.write(LG3)

LG4 = allLGs[3]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG4', 'w')
z.write(LG4)

LG5 = allLGs[4]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG5', 'w')
z.write(LG5)

LG6 = allLGs[5]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG6', 'w')
z.write(LG6)

LG7 = allLGs[6]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG7', 'w')
z.write(LG7)

LG8 = allLGs[7]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG8', 'w')
z.write(LG8)

LG9 = allLGs[8]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG9', 'w')
z.write(LG9)

LG10 = allLGs[9]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG10', 'w')
z.write(LG10)

LG11 = allLGs[10]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG11', 'w')
z.write(LG11)

LG12 = allLGs[11]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG12', 'w')
z.write(LG12)

LG13 = allLGs[12]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG13', 'w')
z.write(LG13)

LG14 = allLGs[13]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG14', 'w')
z.write(LG14)

LG15 = allLGs[14]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG15', 'w')
z.write(LG15)

LG16 = allLGs[15]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG16', 'w')
z.write(LG16)

LG17 = allLGs[16]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG17', 'w')
z.write(LG17)

LG18 = allLGs[17]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG18', 'w')
z.write(LG18)

LG19 = allLGs[18]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG19', 'w')
z.write(LG19)

LG20 = allLGs[19]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG20', 'w')
z.write(LG20)

LG21 = allLGs[20]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG21', 'w')
z.write(LG21)

LG22 = allLGs[21]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG22', 'w')
z.write(LG22)

LG23 = allLGs[22]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG23', 'w')
z.write(LG23)

LG24 = allLGs[23]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG24', 'w')
z.write(LG24)

LG25 = allLGs[24]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG25', 'w')
z.write(LG25)

LG26 = allLGs[25]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG26', 'w')
z.write(LG26)

LG27 = allLGs[26]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG27', 'w')
z.write(LG27)

LG28 = allLGs[27]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG28', 'w')
z.write(LG28)

LG29 = allLGs[28]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG29', 'w')
z.write(LG29)

LG30 = allLGs[29]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG30', 'w')
z.write(LG30)

LG31 = allLGs[30]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG31', 'w')
z.write(LG31)

LG32 = allLGs[31]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG32', 'w')
z.write(LG32)

LG33 = allLGs[32]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG33', 'w')
z.write(LG33)

LG34 = allLGs[33]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG34', 'w')
z.write(LG34)

LG35 = allLGs[34]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG35', 'w')
z.write(LG35)

LG36 = allLGs[35]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG36', 'w')
z.write(LG36)

LG37 = allLGs[36]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG37', 'w')
z.write(LG37)

LG38 = allLGs[37]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG38', 'w')
z.write(LG38)

LG39 = allLGs[38]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG39', 'w')
z.write(LG39)

LG40 = allLGs[39]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG40', 'w')
z.write(LG40)

LG41 = allLGs[40]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG41', 'w')
z.write(LG41)

LG42 = allLGs[41]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG42', 'w')
z.write(LG42)

LG43 = allLGs[42]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG43', 'w')
z.write(LG43)

LG44 = allLGs[43]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG44', 'w')
z.write(LG44)

LG45 = allLGs[44]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG45', 'w')
z.write(LG45)

LG46 = allLGs[45]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG46', 'w')
z.write(LG46)

LG47 = allLGs[46]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG47', 'w')
z.write(LG47)

LG48 = allLGs[47]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG48', 'w')
z.write(LG48)

LG49 = allLGs[48]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG49', 'w')
z.write(LG49)

LG50 = allLGs[49]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG50', 'w')
z.write(LG50)

LG51 = allLGs[50]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_1m_LG51', 'w')
z.write(LG51)


# Then, family 3m

# In[30]:

all3m = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/fam_3m_sqtl.assoc.linear', 'rU').read()
LGs_3m = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LGs.txt', 'rU').read()
LGss_3m = [ i for i in LGs_3m[:-1].split('\n\n')]

mcm_3m = [ [ i.split()[1:3] for i in LGss_3m[j].split('\n') ] for j in range(len(LGss_3m))]

keys_3m = [ i.split()[1] for i in all3m.split('\n')[1:-1]]
values_3m = [ i.split()[-1] for i in all3m.split('\n')[1:-1]]
d_3m = dict(zip(keys_3m, values_3m))
allLGs_3m = [','.join([','.join(mcm_3m[j][i]+[d[mcm_3m[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm_3m[j])) ]).replace('\n,','\n') for j in range(len(mcm_3m))]


# In[31]:

LG1 = allLGs_3m[0]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG1', 'w')
z.write(LG1)

LG2 = allLGs_3m[1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG2', 'w')
z.write(LG2)

LG3 = allLGs_3m[2]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG3', 'w')
z.write(LG3)

LG4 = allLGs_3m[3]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG4', 'w')
z.write(LG4)

LG5 = allLGs_3m[4]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG5', 'w')
z.write(LG5)

LG6 = allLGs_3m[5]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG6', 'w')
z.write(LG6)

LG7 = allLGs_3m[6]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG7', 'w')
z.write(LG7)

LG8 = allLGs_3m[7]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG8', 'w')
z.write(LG8)

LG9 = allLGs_3m[8]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG9', 'w')
z.write(LG9)

LG10 = allLGs_3m[9]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG10', 'w')
z.write(LG10)

LG11 = allLGs_3m[10]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG11', 'w')
z.write(LG11)

LG12 = allLGs_3m[11]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG12', 'w')
z.write(LG12)

LG13 = allLGs_3m[12]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG13', 'w')
z.write(LG13)

LG14 = allLGs_3m[13]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG14', 'w')
z.write(LG14)

LG15 = allLGs_3m[14]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG15', 'w')
z.write(LG15)

LG16 = allLGs_3m[15]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG16', 'w')
z.write(LG16)

LG17 = allLGs_3m[16]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG17', 'w')
z.write(LG17)

LG18 = allLGs_3m[17]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG18', 'w')
z.write(LG18)

LG19 = allLGs_3m[18]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG19', 'w')
z.write(LG19)

LG20 = allLGs_3m[19]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG20', 'w')
z.write(LG20)

LG21 = allLGs_3m[20]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG21', 'w')
z.write(LG21)

LG22 = allLGs_3m[21]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG22', 'w')
z.write(LG22)

LG23 = allLGs_3m[22]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG23', 'w')
z.write(LG23)

LG24 = allLGs_3m[23]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG24', 'w')
z.write(LG24)

LG25 = allLGs_3m[24]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG25', 'w')
z.write(LG25)

LG26 = allLGs_3m[25]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG26', 'w')
z.write(LG26)

LG27 = allLGs_3m[26]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG27', 'w')
z.write(LG27)

LG28 = allLGs_3m[27]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG28', 'w')
z.write(LG28)

LG29 = allLGs_3m[28]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG29', 'w')
z.write(LG29)

LG30 = allLGs_3m[29]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG30', 'w')
z.write(LG30)

LG31 = allLGs_3m[30]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG31', 'w')
z.write(LG31)

LG32 = allLGs_3m[31]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG32', 'w')
z.write(LG32)

LG33 = allLGs_3m[32]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG33', 'w')
z.write(LG33)

LG34 = allLGs_3m[33]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG34', 'w')
z.write(LG34)

LG35 = allLGs_3m[34]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG35', 'w')
z.write(LG35)

LG36 = allLGs_3m[35]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG36', 'w')
z.write(LG36)

LG37 = allLGs_3m[36]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG37', 'w')
z.write(LG37)

LG38 = allLGs_3m[37]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG38', 'w')
z.write(LG38)

LG39 = allLGs_3m[38]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG39', 'w')
z.write(LG39)

LG40 = allLGs_3m[39]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG40', 'w')
z.write(LG40)

LG41 = allLGs_3m[40]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG41', 'w')
z.write(LG41)

LG42 = allLGs_3m[41]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG42', 'w')
z.write(LG42)

LG43 = allLGs_3m[42]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG43', 'w')
z.write(LG43)

LG44 = allLGs_3m[43]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG44', 'w')
z.write(LG44)

LG45 = allLGs_3m[44]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG45', 'w')
z.write(LG45)

LG46 = allLGs_3m[45]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG46', 'w')
z.write(LG46)

LG47 = allLGs_3m[46]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG47', 'w')
z.write(LG47)

LG48 = allLGs_3m[47]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG48', 'w')
z.write(LG48)

LG49 = allLGs_3m[48]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/mal/AAo_3m_LG49', 'w')
z.write(LG49)


# And eventually family 1m

# In[52]:

all1f = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/fam_1f_sqtl.assoc.linear', 'rU').read()
LGs_1f = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LGs.txt', 'rU').read()
LGss_1f = [ i for i in LGs_1f[:-1].split('\n\n')]

mcm_1f = [ [ i.split()[1:3] for i in LGss_1f[j].split('\n') ] for j in range(len(LGss_1f))]

keys_1f = [ i.split()[1] for i in all1f.split('\n')[1:-1]]
values_1f = [ i.split()[-1] for i in all1f.split('\n')[1:-1]]
d_1f = dict(zip(keys_1f, values_1f))


# In[53]:

allLGs_1f = [','.join([','.join(mcm_1f[j][i]+[d[mcm_1f[j][i][0]]] +['\n']).replace(',\n','\n') for i in range(len(mcm_1f[j])) ]).replace('\n,','\n') for j in range(len(mcm_1f))]


# In[55]:

LG1 = allLGs_1f[0]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG1', 'w')
z.write(LG1)

LG2 = allLGs_1f[1]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG2', 'w')
z.write(LG2)

LG3 = allLGs_1f[2]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG3', 'w')
z.write(LG3)

LG4 = allLGs_1f[3]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG4', 'w')
z.write(LG4)

LG5 = allLGs_1f[4]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG5', 'w')
z.write(LG5)

LG6 = allLGs_1f[5]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG6', 'w')
z.write(LG6)

LG7 = allLGs_1f[6]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG7', 'w')
z.write(LG7)

LG8 = allLGs_1f[7]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG8', 'w')
z.write(LG8)

LG9 = allLGs_1f[8]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG9', 'w')
z.write(LG9)

LG10 = allLGs_1f[9]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG10', 'w')
z.write(LG10)

LG11 = allLGs_1f[10]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG11', 'w')
z.write(LG11)

LG12 = allLGs_1f[11]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG12', 'w')
z.write(LG12)

LG13 = allLGs_1f[12]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG13', 'w')
z.write(LG13)

LG14 = allLGs_1f[13]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG14', 'w')
z.write(LG14)

LG15 = allLGs_1f[14]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG15', 'w')
z.write(LG15)

LG16 = allLGs_1f[15]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG16', 'w')
z.write(LG16)

LG17 = allLGs_1f[16]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG17', 'w')
z.write(LG17)

LG18 = allLGs_1f[17]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG18', 'w')
z.write(LG18)

LG19 = allLGs_1f[18]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG19', 'w')
z.write(LG19)

LG20 = allLGs_1f[19]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG20', 'w')
z.write(LG20)

LG21 = allLGs_1f[20]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG21', 'w')
z.write(LG21)

LG22 = allLGs_1f[21]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG22', 'w')
z.write(LG22)

LG23 = allLGs_1f[22]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG23', 'w')
z.write(LG23)

LG24 = allLGs_1f[23]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG24', 'w')
z.write(LG24)

LG25 = allLGs_1f[24]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG25', 'w')
z.write(LG25)

LG26 = allLGs_1f[25]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG26', 'w')
z.write(LG26)

LG27 = allLGs_1f[26]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG27', 'w')
z.write(LG27)

LG28 = allLGs_1f[27]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG28', 'w')
z.write(LG28)

LG29 = allLGs_1f[28]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG29', 'w')
z.write(LG29)

LG30 = allLGs_1f[29]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG30', 'w')
z.write(LG30)

LG31 = allLGs_1f[30]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG31', 'w')
z.write(LG31)

LG32 = allLGs_1f[31]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG32', 'w')
z.write(LG32)

LG33 = allLGs_1f[32]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG33', 'w')
z.write(LG33)

LG34 = allLGs_1f[33]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG34', 'w')
z.write(LG34)

LG35 = allLGs_1f[34]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG35', 'w')
z.write(LG35)

LG36 = allLGs_1f[35]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG36', 'w')
z.write(LG36)

LG37 = allLGs_1f[36]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG37', 'w')
z.write(LG37)

LG38 = allLGs_1f[37]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG38', 'w')
z.write(LG38)

LG39 = allLGs_1f[38]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG39', 'w')
z.write(LG39)

LG40 = allLGs_1f[39]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG40', 'w')
z.write(LG40)

LG41 = allLGs_1f[40]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG41', 'w')
z.write(LG41)

LG42 = allLGs_1f[41]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG42', 'w')
z.write(LG42)

LG43 = allLGs_1f[42]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG43', 'w')
z.write(LG43)

LG44 = allLGs_1f[43]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG44', 'w')
z.write(LG44)

LG45 = allLGs_1f[44]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG45', 'w')
z.write(LG45)

LG46 = allLGs_1f[45]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG46', 'w')
z.write(LG46)

LG47 = allLGs_1f[46]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG47', 'w')
z.write(LG47)

LG48 = allLGs_1f[47]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG48', 'w')
z.write(LG48)

LG49 = allLGs_1f[48]
z = open('/Volumes/group_dv/personal/DValenzano/May2014/AAo/fem/AAo_1f_LG49', 'w')
z.write(LG49)


# In[ ]:



