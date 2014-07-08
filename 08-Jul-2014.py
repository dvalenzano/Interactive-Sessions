
# coding: utf-8

#### Goal: to find sQTl not necessarily present on the rqtl LM

# First, I need to sort grqtl.csv and aarqt.csv based on all the columns except the rqtl one

# In[178]:

g = open('/Volumes/group_dv/personal/DValenzano/Jul2014/gQTL.csv', 'rU').read()
aa = open('/Volumes/group_dv/personal/DValenzano/Jul2014/aaQTL.csv', 'rU').read()

gpval = open('/Volumes/group_dv/personal/DValenzano/Jun2014/G_sqtl_chisqpval_2.csv', 'rU').read().replace('nan','1')
aapval = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AA_sqtl_chisqpval.csv', 'rU').read().replace('nan','1')


# I will be using as template the class written on 02-Jul-2014, with some new additions:  
# self.srtzip, which allows to save only the submatrix relative to the chosen column and  

# In[40]:

#class sortColumn(object):
#    def __init__(self, inp, col):
#        self.inp = [i.split(',') for i in inp.replace('-','0_0').split('\n')[:-1]]
#        self.col = self.inp[0].index(col)
#        self.srt = sorted(self.inp[1:], key=lambda row: (int(row[self.col].split('_')[0]), float(row[self.col].split('_')[1])))
#        self.srtzip = [i for i in self.srt if i[self.col]!='0_0'] 
#        self.tosave = (','.join(self.inp[0])+'\n'+','.join([','.join(i)+'\n' for i in self.srtzip ])).replace('\n,','\n').replace('0_0','-')


# In[41]:

glist = ['g7m', 'ge7m', 'g7f', 'ge7f', 'g14m', 'ge14m', 'g14f', 'ge14f', 'g8m', 'ge8m', 'g8f', 'ge8f', 'g1_1m']


# In[42]:

#for i in glist:
#    ls = '/Volumes/group_dv/personal/DValenzano/Jul2014/gsort_%s.csv' % i
#    p = sortColumn(g, i)
#    z = open(ls, 'w')
#    z.write(p.tosave)
#    z.close() #this way I can save several files at once


# Now I need to add the p-value to each marker and an additional column with a flag if the marker is present in the  
# random forest analysis and in the rqtl linkage map

# Below the R input for manhattan plot

# In[204]:

class sortColumn2(object):

    def __init__(self, inp, pval, col):
        self.inp = [i.split(',') for i in inp.replace('-','0_0').split('\n')[:-1]]
        self.pval = pval # this is the file with the pvalues for each marker
        self.col = self.inp[0].index(col) #this is the column to select
        self.srt = sorted(self.inp[1:], key=lambda row: (int(row[self.col].split('_')[0]), float(row[self.col].split('_')[1])))
        self.srtzip = [i for i in self.srt if i[self.col]!='0_0'] 
        self.tosave = (','.join(self.inp[0])+'\n'+','.join([','.join(i)+'\n' for i in self.srtzip ])).replace('\n,','\n').replace('0_0','-').replace('-.','0_0.')
        self.kg = [ i.split(',')[0] for i in self.pval.split('\n')[1:-2] ]
        self.kv = [ i.split(',')[-1] for i in self.pval.split('\n')[1:-2] ]
        self.kd = dict(zip(self.kg, self.kv))
        self.t = self.tosave.split('\n')
        self.t2 = [','.join([i.split(',')[0]]+i.split(',')[1].split('_')[:2]+[kd[i.split(',')[0]]]) for i in self.t[1:-1]]
        self.t3 = [j.split(',')[0] for j in [i for i in self.t[1:-1] if i.split(',')[15]!= ''] if sum(map(float, j.split(',')[15:]))<4] 
        self.t4 = [k.split(',')[0] for k in  [j for j in [i for i in self.t[1:-1] if i.split(',')[15]!= ''] if sum(map(float, j.split(',')[15:]))<4] if k.split(',')[14]=='-' ]
        self.ls = []
    
    def rinput(self, inp):        
        for i in inp: 
            if i.split(',')[0] in self.t3:
                if i.split(',')[0] in self.t4:
                    self.ls.append(i+',rf\n')
                else:    
                    self.ls.append(i+',rf_rqtl\n')                    
            else:
                self.ls.append(i+',na\n')
        return 'SNP,CHR,BP,P,GROUP\n'+','.join(self.ls).replace('\n,','\n')


# In[205]:

for i in glist:
    ls = '/Volumes/group_dv/personal/DValenzano/Jul2014/gsort_%s.csv' % i
    p = sortColumn2(g, gpval, i)
    z = open(ls, 'w')
    z.write(p.tosave)
    z.close() #this way I can save several files at once
    lz = '/Volumes/group_dv/personal/DValenzano/Jul2014/rinput_%s.csv' % i
    z = open(lz, 'w')
    z.write(p.rinput(p.t2))
    z.close()


# In[ ]:



