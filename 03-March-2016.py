
# coding: utf-8

# Inputs files process through QIIME via python

get_ipython().system(u'/macqiime/anaconda/bin/normalize_table.py -i /Volumes/group_dv/personal/DValenzano/papers/uBiome0/16wk_table_5509.biom -a CSS -o /Volumes/group_dv/personal/DValenzano/papers/uBiome0/16wk_table_5509n.biom')


# In[8]:

get_ipython().system(u'biom convert -i /Volumes/group_dv/personal/DValenzano/papers/uBiome0/16wk_table_5509n.biom -o /Volumes/group_dv/personal/DValenzano/papers/uBiome0/16wk_table_5509n.txt --to-tsv')


# In[9]:

t = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/16wk_table_5509n.txt', 'rU').read()


# In[12]:

t = t.replace('\t',',')
z = open('/Volumes/group_dv/personal/DValenzano/papers/uBiome0/16wk_table_5509n.csv', 'w')
z.write(t)
z.close()


# In[ ]:



