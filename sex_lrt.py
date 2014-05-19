
# coding: utf-8

# Goal: to modify the LRT script to identify sex-linked markers

# In[22]:

#minp = raw_input('what is the male input file?\n')
#finp = raw_input('what is the female input file?\n')
#m = open(minp, 'rU').read()
#f = open(finp, 'rU').read()

m= open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/Go_male_3.csv','rU').read() 
f= open('/Volumes/group_dv/personal/DValenzano/May2014/sex-linked/Go_female_3.csv','rU').read()


# In[ ]:

import math  
#def out(minput, finput):  

mk = [ i.split(',')[0]    for i in m.split('\n')[2:-1]]
fk = [ i.split(',')[0]    for i in f.split('\n')[2:-1]]
mv = [ i.split(',')[1:]    for i in m.split('\n')[2:-1]]
fv = [ i.split(',')[1:]    for i in f.split('\n')[2:-1]]
dm = dict(zip(mk, mv))
df = dict(zip(fk, fv))

ls = [] 
lz = []

for i in mk:  

    mab = dm[i].count('ab')  
    mn = dm[i].count('-')
    mln = len(dm[i])
    mnab = mln-mab-mn
    freq_mab = float(mab)/(mln-mn)  
    freq_mnab = 1-freq_mab  

    fab = df[i].count('ab')  
    fn = df[i].count('-')
    fln = len(df[i])
    fnab = fln-fab-fn
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

        elif fnab < 7: 
            pass

########################################################################################

        else:
            lz.append(i+':\t-\t40\t0.00\n')
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


# In[ ]:

out = minp.split('_')[0]+'_lrt.csv'
z = open(out, 'w')
z.write(lso)
z.close()

