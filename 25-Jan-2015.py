# Goal: to generate a new file for cross AAo and Go with the corrected p-values based on min FDR
# The generated file has corrected p values genome-wide and linkage group by linkage group


# In[1]:

ptab = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aao-pval.csv', 'rU').read()
qtab = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/aao_qval.tsv', 'rU').read()


# In[2]:

len(ptab.split('\n')) == len(qtab.split('\n'))


# In[3]:

ptab.split('\n')[0]


# In[14]:

qtab.split('\n')[0]


# In[17]:

markers = [ i.split('\t')[0].replace('X', '') for i in qtab.split('\n')[1:-1] ]


# In[35]:

pvalmatrix = ['"marker",'+ptab.split('\n')[0]+'\n'] + [ markers[i]+','+','.join(ptab.split('\n')[1:-1][i].split()[1:])+'\n'  for i in range(len(ptab.split('\n')[1:-1]))]


# In[46]:

pvaldays = 'marker,pval\n'+','.join([ i.split(',')[0]+','+i.split(',')[2]+'\n' for i in pvalmatrix[1:] ]).replace('\n,','\n')


# In[48]:

# pvaldays has the p values for all the markers analyzed with the RF method
z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aao_days_pval.csv', 'w')
z.write(pvaldays)
z.close()


# In[47]:

aao = open('/Volumes/group_dv/personal/DValenzano/Jan2015/AAo_qvals_survall.csv', 'rU').read()
aao_adj = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aao_days_padj.csv', 'rU').read()


# In[51]:

aaok = [i.split(',')[0] for i in aao.split('\n')[1:-1]]
aaov = [i.split(',')[1:-1] for i in aao.split('\n')[1:-1]]
aaod = dict(zip(aaok, aaov))

aao_adjk = [i.split()[1] for i in aao_adj.split('\n')[1:-1]]
aao_adjv = [i.split()[2:] for i in aao_adj.split('\n')[1:-1]]
aao_adjd = dict(zip(aao_adjk,aao_adjv))


# In[52]:

len(aaok) == len(aao_adjk)


# In[55]:

aao_new = [[i] + aaod[i] + aao_adjd[i] for i in aaok]


# In[56]:

aao_new2 = 'maker,LG,cM,pval,p.adj\n'+','.join([','.join(i)+'\n' for i in aao_new]).replace('\n,','\n')


# In[57]:

z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/aao_pq.csv', 'w')
z.write(aao_new2)
z.close()


# In[90]:

# Now same as above, for cross Go
go = open('/Volumes/group_dv/personal/DValenzano/May2014/go32014_all_pos.csv', 'rU').read()
gos = go.split('\n')[:-1]
gos2 = [i.replace('"','')   for i in gos if i.split(',')[0] != '""' ]

goss = sorted(gos2, key=lambda x: ( float(x.split(',')[1]), float(x.split(',')[2])))
#go = sorted(aa0_sorted, key= lambda x: (x[1], x[2]))


# In[96]:

gossk = [ i.split(',')[0] for i in goss]
gossv = [ i.split(',')[1:] for i in goss]
gossd = dict(zip(gossk, gossv))


# In[97]:

go_adj = open('/Volumes/group_dv/personal/DValenzano/Jan2015/go_days_padj.csv', 'rU').read()


# In[98]:

go_adjk = [i.split()[1] for i in go_adj.split('\n')[1:-1]]
go_adjv = [i.split()[2:] for i in go_adj.split('\n')[1:-1]]
go_adjd = dict(zip(go_adjk,go_adjv))


# In[108]:

from sets import Set
goset =  Set(gossk) & Set(go_adjk) 
gos = list(goset)


# In[109]:

go_new = [[i] + gossd[i] + go_adjd[i] for i in gos]
go_new2 = 'maker,LG,cM,pval,p.adj\n'+','.join([','.join(i)+'\n' for i in go_new]).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Jan2015/go_pq.csv', 'w')
z.write(go_new2)
z.close()


# In[ ]:



