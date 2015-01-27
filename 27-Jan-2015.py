
# Goal: to generate two tables - one for cross 1 and one for cross 2 - with marker name, p value and q value in days (all)

c1q = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/go_qval.tsv', 'rU').read()
c2q = open('/Volumes/group_dv/personal/DValenzano/Sep2014/qtl-direction-analysis/aao_qval.tsv', 'rU').read()


# In[6]:

c1p = open('/Volumes/group_dv/personal/DValenzano/Dec2014/go-pval.csv', 'rU').read()
c2p = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aao-pval.csv', 'rU').read()


# In[10]:

c1m = [i.split()[0][1:] for i in c1q.split('\n')[1:-1] ]
c2m = [i.split()[0][1:] for i in c2q.split('\n')[1:-1] ]


# In[12]:

c1pv = [i.split()[2] for i in c1p.split('\n')[1:-1]]
c1qv = [i.split()[2] for i in c1q.split('\n')[1:-1]]

c2pv = [i.split()[2] for i in c2p.split('\n')[1:-1]]
c2qv = [i.split()[2] for i in c2q.split('\n')[1:-1]]


# In[17]:

c1 = 'marker,p-val,qval\n'+','.join([c1m[i]+','+c1pv[i] +','+c1qv[i]+'\n' for i in range(len(c1m)) ]).replace('\n,','\n')
c2 = 'marker,p-val,qval\n'+','.join([c2m[i]+','+c2pv[i] +','+c2qv[i]+'\n' for i in range(len(c2m)) ]).replace('\n,','\n')


# In[20]:

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/c1_mpq_ecdf.csv', 'w')
z.write(c1)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/c2_mpq_ecdf.csv', 'w')
z.write(c2)
z.close()


# In[ ]:



