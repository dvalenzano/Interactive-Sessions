
# coding: utf-8

# In[30]:

f_pop = open('/Volumes/group_dv/group/data/sex_determination/Wild_population_work/may2014/Sex_linked_markers/pop_female_tpf.csv', 'rU').read()
m_pop = open('/Volumes/group_dv/group/data/sex_determination/Wild_population_work/may2014/Sex_linked_markers/pop_male_tpm.csv', 'rU').read()


# In[53]:

f= ','.join([','.join(i.split(',')[1:]).replace(' ','')+'\n' for i in f_pop.split('\n')[4:-1]]).replace('\n,','\n')
m= ','.join([','.join(i.split(',')[1:]).replace(' ','')+'\n' for i in m_pop.split('\n')[4:-1]]).replace('\n,','\n')


# In[70]:

import math  
#def out(minput, finput):  

mk = [ i.split(',')[0]    for i in m.split('\n')[:-1]]
fk = [ i.split(',')[0]    for i in f.split('\n')[:-1]]
mv = [ i.split(',')[1:]    for i in m.split('\n')[:-1]]
fv = [ i.split(',')[1:]    for i in f.split('\n')[:-1]]
dm = dict(zip(mk, mv))
df = dict(zip(fk, fv))

ls = [] 
lz = []

for i in mk:  

    mab = dm[i].count('ab')  
    mn = dm[i].count('-')
    mln = len(dm[i])
    mnab = mln-mab-mn
    if mln-mn == 0:
        pass
    else:
        freq_mab = float(mab)/(mln-mn)  
        freq_mnab = 1-freq_mab  
   
    
    fab = df[i].count('ab')  
    fn = df[i].count('-')
    fln = len(df[i])
    fnab = fln-fab-fn
    if fln-fn == 0:
        pass
    else:
        freq_fab = float(fab)/(fln-fn)  
        freq_fnab = 1-freq_fab 
    
#    if mab == 0 and fab == 0:
#        pass
#    elif mab != 0 and fab == 0:
#        lz.append(i+':\t-\tinf\t0.00\n')
    if fab == 0:
        if mab == 0:
            pass
        
###################The next two lines of code were added on 19 May, 2014 ###############

        elif fln-fn < 6: 
            pass

########################################################################################

#        else:
#            lz.append(i+':\t-\t40\t0.00\n')
    elif freq_fab == 1:
        pass
    else:
        MLE_mab = (freq_mab**mab)*(freq_mnab**mnab)  
        MLE_fab = (freq_fab**mab)*(freq_fnab**mnab)
#        if MLE_fab == 0:
#            pass
#        else:
        LRT = 2*(math.log(MLE_mab)-math.log(MLE_fab))  
        LOD = math.log10(MLE_mab/MLE_fab)  
        p_val = 1.0/(10**(LOD))  
        out = i.split(',')[0]+':\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'  
        ls.append(out)  

lso = 'Marker'+'\tLRT\tLOD\tp_val\n'+','.join(ls)[:-1].replace('\n,','\n')+','.join(lz)[:-1].replace('\n,','\n')


# In[78]:

qspop = lso.split('\n')
hLODpop = [ i  for i in qspop[1:] if float(i.split('\t')[2])>4] #only picks markers that have LOD score higher than 15

# hLODpop2 = [  i  for i in hLODpop if i.split('\t')[2] != '40']

len(hLODpop)


# In[96]:

qtlIDpop = [ i.split('\t')[0][:-1].replace(' ','') for i in hLODpop ]


# <codecell>

z = open('/Volumes/group_dv/group/data/sex_determination/Wild_population_work/may2014/Sex_linked_markers/pop_slrt.csv', 'w')
z.write(','.join(qtlIDpop))
z.close()

z = open('/Volumes/group_dv/group/data/sex_determination/Wild_population_work/may2014/Sex_linked_markers/pop_lrt.csv', 'w')
z.write(lso)
z.close()

