
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


# In[46]:

lz = [i+'\n'+d[i.split('_')[0]]+'\n' for i in scaffolds if i.split('_')[0] in keys]


#probes = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-40:int(i.split('\n')[0].split('_')[1].split('-')[0])+140] for i in lz] 

probes = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-160:int(i.split('\n')[0].split('_')[1].split('-')[0])+260] for i in lz] 

# In[101]:

probes2 = []
for i in probes:
#    probes2.append(i.split('\n')[0]+'_probe1\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2\n'+i.split('\n')[1][-120:]+'\n')
    probes2.append(i.split('\n')[0]+'_probe1_AAo_yl\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2_AAo_yl\n'+i.split('\n')[1][60:180]+'\n'+i.split('\n')[0]+'_probe3_AAo_yl\n'+i.split('\n')[1][120:240]+'\n'+i.split('\n')[0]+'_probe4_AAo_yl\n'+i.split('\n')[1][180:300]+'\n'+i.split('\n')[0]+'_probe5_AAo_yl\n'+i.split('\n')[1][240:360]+'\n'+i.split('\n')[0]+'_probe6_AAo_yl\n'+i.split('\n')[1][300:420]+'\n')


# In[102]:

# lz[0].split('\n')[0]+'\n'+lz[0].split('\n')[1][int(lz[0].split('\n')[0].split('_')[1].split('-')[0])-40:int(lz[0].split('\n')[0].split('_')[1].split('-')[0])+140]


# In[105]:

probes2f = ','.join(probes2).replace('\n,','\n')


# In[12]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_AAo_6probes.fa', 'w')
z.write(probes2f)
z.close()


# So we're done with the y-linked ones in both AAo and Go

# In[ ]:



