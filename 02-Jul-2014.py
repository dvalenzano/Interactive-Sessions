
# coding: utf-8

# In[1]:

aaqtl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AA_qtl_1.csv', 'rU').read()
gqtl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_qtl_1.csv', 'rU').read()


# In[72]:

class sortColumn(object):
    def __init__(self, inp, col):
        self.inp = [i.split(',') for i in inp.replace('-','0_0').split('\n')[:-1]]
        self.col = self.inp[0].index(col)
        self.srt = sorted(self.inp[1:], key=lambda row: (int(row[self.col].split('_')[0]), float(row[self.col].split('_')[1])))
        self.tosave = (','.join(self.inp[0])+'\n'+','.join([','.join(i)+'\n' for i in self.srt ])).replace('\n,','\n').replace('0_0','-')


# In[15]:

#prova = sorted([i.split(',') for i in aaqtl.replace('-','0_0').split('\n')[1:-1]], key=lambda row: (int(row[-1].split('_')[0]), float(row[-1].split('_')[1])))


# In[73]:

aaq_rqtl = sortColumn(aaqtl, 'rqtl')
gq_rqtl = sortColumn(gqtl, 'rqtl')

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aarqtl.csv', 'w')
z.write(aaq_rqtl.tosave)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jul2014/grqtl.csv', 'w')
z.write(gq_rqtl.tosave)
z.close()


# In[73]:




# In[ ]:



