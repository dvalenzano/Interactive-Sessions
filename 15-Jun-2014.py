
# coding: utf-8

# In[6]:

inp_tr = open('/Volumes/group_dv/group/tmp/Nfur_draft_genome_v9Nov2012.fa', 'rU').read()
inp_scaff = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_Go_match.psl', 'rU').read()


# In[11]:


# In[48]:

inp_scaffs = inp_scaff.split('\n')[5:-1]
scaffolds = []
for i in inp_scaffs:
    scaffolds.append('>'+i.split('\t')[13]+'_'+','.join(i.split('\t')[15:17]).replace(',','-')) #this creates a list of scaffolds that have blat hits

scaffoldsj = ','.join(scaffolds).replace(',','\n')

#z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/scaffolds.txt', 'w') #saves the scaffolds list as a string in the current directory
#z.write(scaffoldsj)
#z.close()


# In[46]:

inp_trs = inp_tr.split('\n')[:-1]

keys = inp_trs[:len(inp_trs):2] 
values = inp_trs[1:len(inp_trs):2]

d = dict(zip(keys, values)) #this is a dictionary that contains scaffold names as keys and corresponding sequences as values


# In[82]:

ls = [i+'\n'+d[i.split('_')[0]]+'\n' for i in scaffolds if i.split('_')[0] in keys]


#probes = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-40:int(i.split('\n')[0].split('_')[1].split('-')[0])+140] for i in ls] 

probes = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-160:int(i.split('\n')[0].split('_')[1].split('-')[0])+260] for i in ls] 

# In[101]:

probes2 = []
for i in probes:
#    probes2.append(i.split('\n')[0]+'_probe1\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2\n'+i.split('\n')[1][-120:]+'\n')
    probes2.append(i.split('\n')[0]+'_probe1\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2\n'+i.split('\n')[1][60:180]+'\n'+i.split('\n')[0]+'_probe3\n'+i.split('\n')[1][120:240]+'\n'+i.split('\n')[0]+'_probe4\n'+i.split('\n')[1][180:300]+'\n'+i.split('\n')[0]+'_probe5\n'+i.split('\n')[1][240:360]+'\n'+i.split('\n')[0]+'_probe6\n'+i.split('\n')[1][300:420]+'\n')


# In[102]:

# ls[0].split('\n')[0]+'\n'+ls[0].split('\n')[1][int(ls[0].split('\n')[0].split('_')[1].split('-')[0])-40:int(ls[0].split('\n')[0].split('_')[1].split('-')[0])+140]


# In[105]:

probes2f = ','.join(probes2).replace('\n,','\n')


# In[12]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_Go_probes_2.fa', 'w')
z.write(probes2f)
z.close()


# In[ ]:



