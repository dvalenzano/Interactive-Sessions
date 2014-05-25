
# coding: utf-8

# In[28]:

Go_m7e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m7e.csv', 'rU').read()


# In[30]:

Go_m7eL = [i.split(',') for i in Go_m7e.split('\n')[:-1]]


# In[39]:

ls = []
for i in Go_m7eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))


# In[84]:

lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')


# In[85]:

lsf2 = ','.join(Go_m7eL[0])+'\n'+lsf


# In[86]:

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m7e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[88]:

Go_m14e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m14e.csv', 'rU').read()

Go_m14eL = [i.split(',') for i in Go_m14e.split('\n')[:-1]]

ls = []

for i in Go_m14eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(Go_m14eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m14e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[89]:

Go_m8e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m8e.csv', 'rU').read()

Go_m8eL = [i.split(',') for i in Go_m8e.split('\n')[:-1]]

ls = []

for i in Go_m8eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(Go_m8eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_m8e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[90]:

Go_f7e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f7e.csv', 'rU').read()

Go_f7eL = [i.split(',') for i in Go_f7e.split('\n')[:-1]]

ls = []

for i in Go_f7eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(Go_f7eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f7e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[91]:

Go_f14e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f14e.csv', 'rU').read()

Go_f14eL = [i.split(',') for i in Go_f14e.split('\n')[:-1]]

ls = []

for i in Go_f14eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(Go_f14eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f14e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[92]:

Go_f8e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f8e.csv', 'rU').read()

Go_f8eL = [i.split(',') for i in Go_f8e.split('\n')[:-1]]

ls = []

for i in Go_f8eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(Go_f8eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/Go_f8e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[94]:

AAo_m1e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m1e.csv', 'rU').read()

AAo_m1eL = [i.split(',') for i in AAo_m1e.split('\n')[:-1]]

ls = []

for i in AAo_m1eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(AAo_m1eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m1e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[95]:

AAo_m1e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m1e.csv', 'rU').read()

AAo_m1eL = [i.split(',') for i in AAo_m1e.split('\n')[:-1]]

ls = []

for i in AAo_m1eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(AAo_m1eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m1e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[96]:

AAo_m3e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m3e.csv', 'rU').read()

AAo_m3eL = [i.split(',') for i in AAo_m3e.split('\n')[:-1]]

ls = []

for i in AAo_m3eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(AAo_m3eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_m3e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[97]:

AAo_f1e = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_f1e.csv', 'rU').read()

AAo_f1eL = [i.split(',') for i in AAo_f1e.split('\n')[:-1]]

ls = []

for i in AAo_f1eL[1:]:
    if float(i[1]) < float(i[6]):
        ls.append(','.join(i))
    elif float(i[1]) > float(i[6]):
        ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
    elif float(i[1]) == float(i[6]):
        if float(i[2]) < float(i[7]):
            ls.append(','.join(i))
        elif float(i[2]) > float(i[7]):
            ls.append(','.join(i[5:-1]+i[:5]+[i[-1]]))
        else:
            ls.append(','.join(i))
            
lss = [i.split(',') for i in ls]
lsS = sorted(lss, key= lambda row: int(row[1])) #might be the first time I use the lambda function
lsf = ','.join([','.join(i)+'\n' for i in lsS ]).replace('\n,','\n')
lsf2 = ','.join(AAo_f1eL[0])+'\n'+lsf

z = open('/Volumes/group_dv/personal/DValenzano/May2014/epi-sqtl/AAo_f1e_sorted.csv', 'w')
z.write(lsf2)
z.close()


# In[ ]:



