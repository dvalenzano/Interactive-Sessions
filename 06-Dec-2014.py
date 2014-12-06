# Goal: to calculate FDR for p-values on LG3 in the random forest analysis using the Benjamini-Hochberg correction for the multiple hypothesis testing
# First, I need to generate a new matrix with the p-values instead of the q-values

ptab = open('/Volumes/group_dv/personal/DValenzano/Dec2014/go-pval.csv', 'rU').read()
qtab = open('/Volumes/group_dv/personal/DValenzano/Jul2014/RF_qtl/go_qval.tsv', 'rU').read()


# In[12]:

len(ptab.split('\n')) == len(qtab.split('\n'))


# In[13]:

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
z = open('/Volumes/group_dv/personal/DValenzano/Dec2014/RF/go_days_pval.csv', 'w')
z.write(pvaldays)
z.close()


# In[72]:

# Now I need to restrict the markers to those on LG3
g_ = open('/Volumes/group_dv/personal/DValenzano/Oct2014/gdays3_tab.csv', 'rU').read()
g_3 =  [g_.split('\n')[0]]+[i for i in g_.split('\n')[:-1] if i.split(',')[1]=='3.0']
g_k = [i.split(',')[0] for i in g_3[1:]]
g_v = [','.join(i.split(',')[1:3]) for i in g_3[1:]]
g_d = dict(zip(g_k, g_v))


# In[73]:

pval_k = [ i.split(',')[0] for i in pvaldays.split('\n')[1:-1] ] 
pval_v = [ i.split(',')[1] for i in pvaldays.split('\n')[1:-1] ] 
pval_d = dict(zip(pval_k, pval_v))


# In[102]:

# Now I need to subset pvaldays to lg3
pvaldays_lg3 = ','.join(g_.split('\n')[0].split(',')[:3]) +',pval\n'+   ','.join(sorted([ i+','+g_d[i]+','+pval_d[i]+'\n'  for i in g_k ], key=lambda x: float(x.split(',')[2])) ).replace('\n,','\n')


# In[103]:

z = open('/Volumes/group_dv/personal/DValenzano/Dec2014/RF/go_dayslg3_pval.csv', 'w')
z.write(pvaldays_lg3)
z.close()

