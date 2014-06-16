
# coding: utf-8

# Goal: to select a set of random markers from all over AAo and Go linkage maps - these markers will be added to the list of probes for the exome sequencing  
# First, I need to start from the AAo y-specific markers

# In[8]:

AAo_sl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo.txt', 'rU').read()
AAofa = ','.join([ '>'+i.split('\t')[1]+'\n'+i.split('\t')[2]+'\n'   for i in AAo_sl.split('\n')[1:-1]  ]).replace('\n,','\n')


# In[10]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo.fa', 'w')
z.write(AAofa)
z.close()


# Now I need to remove the radtags that have more than 2 mismatches and gaps (after blat)

# In[39]:

ls = []
aaops = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo.psl', 'rU').read()
for i in aaops.split('\n')[5:-1]:
    if int(i.split('\t')[0]) == 95 or int(i.split('\t')[0]) == 94:
        if int(i.split('\t')[1]) < 2:
            if int(i.split('\t')[7]) == 0:
                ls.append(i+'\n')
aaopsh = ','.join([i+'\n' for i in aaops.split('\n')[:5]]    ).replace('\n,','\n')
aaopsf = aaopsh+','.join(ls).replace('\n,','\n')

#ls = []
#for i in aaops[5:-1]:
#    if i[:1]=='95' or i[:1] =='94':
#        if i.split('\t')[7]=='0':
#            ls.append(i+'\n')

#body2 = asph + ','.join([ i+'\n'  for i in asp[5:-1] if i[:2]=='95' or i[:2] == '94' or i[:2]=='93']).replace('\n,','\n')
#body2 = asph + ','.join([ i+'\n'  for i in asp[5:-1] if i[:2] == '94']).replace('\n,','\n')
#body = aaopsh + ','.join(ls).replace('\n,','\n')

w = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo_match.psl', 'w')
w.write(aaopsf)
w.close()


# In[34]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo_match.psl', 'w')
z.write(aaopsf)
z.close()


# In[40]:

inp_g = open('/Volumes/group_dv/group/tmp/Nfur_draft_genome_v9Nov2012.fa', 'rU').read()


# In[41]:

inp_scaffs = aaopsf.split('\n')[5:-1]
scaffolds = []
for i in inp_scaffs:
    scaffolds.append('>'+i.split('\t')[13]+'_'+','.join(i.split('\t')[15:17]).replace(',','-')) #this creates a list of scaffolds that have blat hits

scaffoldsj = ','.join(scaffolds).replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo_scaffolds.txt', 'w') #saves the scaffolds list as a string in the current directory
z.write(scaffoldsj)
z.close()


# In[44]:

inp_gs = inp_g.split('\n')[:-1]

keys = inp_gs[:len(inp_gs):2] 
values = inp_gs[1:len(inp_gs):2]

d = dict(zip(keys, values)) 


# In[104]:

lz = [i+'\n'+d[i.split('_')[0]]+'\n' for i in scaffolds if i.split('_')[0] in keys]


#probes = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-40:int(i.split('\n')[0].split('_')[1].split('-')[0])+140] for i in lz] 

probes = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-160:int(i.split('\n')[0].split('_')[1].split('-')[0])+260] for i in lz] 

# In[101]:

probes2 = []
for i in probes:
    if len(i.split('\n')[-1]) >= 240:
        if 'NN' not in i.split('\n')[-1]:
    #    probes2.append(i.split('\n')[0]+'_probe1\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2\n'+i.split('\n')[1][-120:]+'\n')
            probes2.append(i.split('\n')[0]+'_probe1_AAo_yl\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2_AAo_yl\n'+i.split('\n')[1][60:180]+'\n'+i.split('\n')[0]+'_probe3_AAo_yl\n'+i.split('\n')[1][120:240]+'\n'+i.split('\n')[0]+'_probe4_AAo_yl\n'+i.split('\n')[1][180:300]+'\n'+i.split('\n')[0]+'_probe5_AAo_yl\n'+i.split('\n')[1][240:360]+'\n'+i.split('\n')[0]+'_probe6_AAo_yl\n'+i.split('\n')[1][300:420]+'\n')

probes2f = ','.join(probes2).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo_6probes.fa', 'w')
z.write(probes2f)
z.close()


# So we're done with the y-linked ones in both AAo and Go and we need to complete the sqtl-probes

# I will only use the max-lifespan sqtl, and then will add a choice of probes from Go cross and AAo cross

# Starting from Go, I will select 500 radtags

# In[51]:

go = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-Go/NfGo_export_hp.fa', 'rU').read()
gos = go.split('\n')[:-1]


# In[57]:

gokeys = gos[:len(gos):2] 
govalues = gos[1:len(gos):2]
god = dict(zip(gokeys, govalues)) 


# In[61]:

import random
rgod = random.sample(gokeys, 500)
gol = [ i+'\n'+god[i]+'\n' for i in rgod ]
golj = ','.join(gol).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Go_random.fa', 'w')
z.write(golj)
z.close()


# In[64]:

aao = open('/Volumes/group_dv/group/data/sequences/fastafiles/cross-AAo/NfAAo_export_hp.fa', 'rU').read()
aaos = aao.split('\n')[:-1]
aaokeys = aaos[:len(aaos):2] 
aaovalues = aaos[1:len(aaos):2]
aaod = dict(zip(aaokeys, aaovalues)) 
import random
raaod = random.sample(aaokeys, 500)
aaol = [ i+'\n'+aaod[i]+'\n' for i in raaod ]
aaolj = ','.join(aaol).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AAo_random.fa', 'w')
z.write(aaolj)
z.close()


# In[81]:

goPs = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Go_random.psl', 'rU').read()
aaoPs = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AAo_random.psl', 'rU').read()

lsGoPs = []
lsAAoPs = []

for i in aaoPs.split('\n')[5:-1]:
    if int(i.split('\t')[0]) == 95 or int(i.split('\t')[0]) == 94:
        if int(i.split('\t')[1]) < 2:
            if int(i.split('\t')[7]) == 0:
                lsAAoPs.append(i+'\n')
aaoPsh = ','.join([i+'\n' for i in aaoPs.split('\n')[:5]]    ).replace('\n,','\n')
aaoPsf = aaoPsh+','.join(lsAAoPs).replace('\n,','\n')

for i in goPs.split('\n')[5:-1]:
    if int(i.split('\t')[0]) == 95 or int(i.split('\t')[0]) == 94:
        if int(i.split('\t')[1]) < 2:
            if int(i.split('\t')[7]) == 0:
                lsGoPs.append(i+'\n')
goPsh = ','.join([i+'\n' for i in goPs.split('\n')[:5]]    ).replace('\n,','\n')
goPsf = goPsh+','.join(lsGoPs).replace('\n,','\n')

w = open('/Volumes/group_dv/personal/DValenzano/Jun2014/AAo_random_match.psl', 'w')
w.write(aaoPsf)
w.close()

w = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Go_random_match.psl', 'w')
w.write(goPsf)
w.close()


# Now I will only select markers from cross Go 

# In[82]:

iscG = goPsf.split('\n')[5:-1]
scG = []
for i in iscG:
    scG.append('>'+i.split('\t')[13]+'_'+','.join(i.split('\t')[15:17]).replace(',','-')) #this creates a list of scaffolds that have blat hits

scGj = ','.join(scG).replace(',','\n')

inp_gs = inp_g.split('\n')[:-1]

scG_keys = inp_gs[:len(inp_gs):2] 
scG_values = inp_gs[1:len(inp_gs):2]

scG_d = dict(zip(scG_keys, scG_values)) 


# In[88]:

lZ = [i+'\n'+scG_d[i.split('_')[0]]+'\n' for i in scG if i.split('_')[0] in scG_keys]

probs = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-160:int(i.split('\n')[0].split('_')[1].split('-')[0])+260] for i in lZ] 

probes2 = []

for i in probs:
    if len(i.split('\n')[-1])== 420:
        if 'NN' not in i.split('\n')[-1]:
            probes2.append(i.split('\n')[0]+'_probe1_Go_rm\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2_Go_rm\n'+i.split('\n')[1][60:180]+'\n'+i.split('\n')[0]+'_probe3_Go_rm\n'+i.split('\n')[1][120:240]+'\n'+i.split('\n')[0]+'_probe4_Go_rm\n'+i.split('\n')[1][180:300]+'\n'+i.split('\n')[0]+'_probe5_Go_rm\n'+i.split('\n')[1][240:360]+'\n'+i.split('\n')[0]+'_probe6_Go_rm\n'+i.split('\n')[1][300:420]+'\n')
            
probes3 = random.sample(probes2, 100)
            
probes2f = ','.join(probes3).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Go_100random_probes.fa', 'w')
z.write(probes2f)
z.close()


# And lastly the sqt

# In[89]:

sqtl = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Go_sqtl_ml.psl', 'rU').read()

qls = []

for i in sqtl.split('\n')[5:-1]:
    if int(i.split('\t')[0]) == 95 or int(i.split('\t')[0]) == 94:
        if int(i.split('\t')[1]) < 2:
            if int(i.split('\t')[7]) == 0:
                qls.append(i+'\n')
sqtlh = ','.join([i+'\n' for i in sqtl.split('\n')[:5]]    ).replace('\n,','\n')
sqtlf = sqtlh+','.join(qls).replace('\n,','\n')

w = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Go_sqtl_ml_match.psl', 'w')
w.write(sqtlf)
w.close()


# In[91]:

imlG = sqtlf.split('\n')[5:-1]


# In[93]:

mlG = []
for i in imlG:
    mlG.append('>'+i.split('\t')[13]+'_'+','.join(i.split('\t')[15:17]).replace(',','-')) #this creates a list of scaffolds that have blat hits


# In[96]:

inp_gs = inp_g.split('\n')[:-1]

mlG_keys = inp_gs[:len(inp_gs):2] 
mlG_values = inp_gs[1:len(inp_gs):2]

mlG_d = dict(zip(mlG_keys, mlG_values)) 


# In[97]:

lsq = [i+'\n'+mlG_d[i.split('_')[0]]+'\n' for i in mlG if i.split('_')[0] in mlG_keys]


# In[102]:

mlprobs = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-160:int(i.split('\n')[0].split('_')[1].split('-')[0])+260] for i in lsq] 

mlprobes2 = []

for i in mlprobs:
    if len(i.split('\n')[-1])== 420:
        if 'NN' not in i.split('\n')[-1]:
            mlprobes2.append(i.split('\n')[0]+'_probe1_Go_sqtl_ml\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2_Go_sqtl_ml\n'+i.split('\n')[1][60:180]+'\n'+i.split('\n')[0]+'_probe3_Go_sqtl_ml\n'+i.split('\n')[1][120:240]+'\n'+i.split('\n')[0]+'_probe4_Go_sqtl_ml\n'+i.split('\n')[1][180:300]+'\n'+i.split('\n')[0]+'_probe5_Go_sqtl_ml\n'+i.split('\n')[1][240:360]+'\n'+i.split('\n')[0]+'_probe6_Go_sqtl_ml\n'+i.split('\n')[1][300:420]+'\n')           
            
mlprobes2f = ','.join(mlprobes2).replace('\n,','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/Go_sqtl_ml_probes.fa', 'w')
z.write(mlprobes2f)
z.close()


# In[ ]:



