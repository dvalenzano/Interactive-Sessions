
# coding: utf-8

### Sorted p-value matrix for cross 1, for all the phenotypes, sorted by linkage group and position

# In[1]:

go = open('/Volumes/group_dv/personal/DValenzano/month-by-month/May2014/go32014_all_pos.csv', 'rU').read()


# In[2]:

gos = go.split('\n')[:-1]
gos2 = [i.replace('"','')   for i in gos if i.split(',')[0] != '""' ]


# In[8]:

go_p = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Jan2015/cross1_pvals.csv', 'rU').read()
go_adj = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Jan2015/go_days_padj.csv', 'rU').read()


# In[12]:

go_pk = [i.split(',')[0] for i in go_p.split('\n')[1:-1]]
go_pv = [i.split(',')[1:] for i in go_p.split('\n')[1:-1]]
go_pd = dict(zip(go_pk,go_pv))


# In[14]:

from sets import Set
goset =  Set([i.split(',')[0] for i in gos2]) & Set(go_pk) 
gos = list(goset)


# In[17]:

gos3 = [ i  for i in gos2 if i.split(',')[0] in gos]
goss = sorted(gos3, key=lambda x: ( float(x.split(',')[1]), float(x.split(',')[2])))

gossk = [ i.split(',')[0] for i in goss]
gossv = [ i.split(',')[1:] for i in goss]
gossd = dict(zip(gossk, gossv))


# In[19]:

go_new = [[i] + gossd[i] + go_pd[i] for i in gossk]
go_new2 = 'marker,LG,cM,sex,days,col,bl,weight,melanoma,weightM,weightF,weightRes,daysM,daysF,daysRes\n'+','.join([','.join(i)+'\n' for i in go_new]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/May2015/go_p_sorted.csv', 'w')
z.write(go_new2)
z.close()


# In[ ]:



