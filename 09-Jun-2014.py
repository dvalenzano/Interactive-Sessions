
# coding: utf-8

# First, we select the scaffolds with better match: 0 or one mismatches in 95 base pairs

# In[42]:

a = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_Go.psl', 'rU').read()
asp = a.split('\n')
asph = ','.join([i+'\n' for i in asp[:5]]).replace('\n,','\n')
#body = asph + ','.join([ i+'\n'  for i in asp[5:-1] if i[:2]=='95']).replace('\n,','\n')

ls = []
for i in asp[5:-1]:
    if i[:2]=='95' or i[:2] =='94':
        if i.split('\t')[7]=='0':
            ls.append(i+'\n')

#body2 = asph + ','.join([ i+'\n'  for i in asp[5:-1] if i[:2]=='95' or i[:2] == '94' or i[:2]=='93']).replace('\n,','\n')
#body2 = asph + ','.join([ i+'\n'  for i in asp[5:-1] if i[:2] == '94']).replace('\n,','\n')
body = asph + ','.join(ls).replace('\n,','\n')

w = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_Go_match.psl', 'w')
w.write(body)
w.close()


# In[43]:

inp_tr = open('/Volumes/group_dv/group/tmp/Nfur_draft_genome_v9Nov2012.fa', 'rU').read()
inp_scaff = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_Go_match.psl', 'rU').read()


# In[48]:

inp_scaffs = inp_scaff.split('\n')[5:-1]
scaffolds = []
for i in inp_scaffs:
    scaffolds.append('>'+i.split('\t')[13]+'_'+','.join(i.split('\t')[15:17]).replace(',','-')) #this creates a list of scaffolds that have blat hits

scaffoldsj = ','.join(scaffolds).replace(',','\n')

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/scaffolds.txt', 'w') #saves the scaffolds list as a string in the current directory
z.write(scaffoldsj)
z.close()


# In[46]:

inp_trs = inp_tr.split('\n')[:-1]

keys = inp_trs[:len(inp_trs):2] 
values = inp_trs[1:len(inp_trs):2]

d = dict(zip(keys, values)) #this is a dictionary that contains scaffold names as keys and corresponding sequences as values


# In[82]:

ls = [i+'\n'+d[i.split('_')[0]]+'\n' for i in scaffolds if i.split('_')[0] in keys]
lsj = ','.join([i+'\n'+d[i.split('_')[0]]+'\n' for i in scaffolds if i.split('_')[0] in keys]).replace('\n,','\n')


# In[80]:

out=  '/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_Go_match_btf.fa'
z = open(out, 'w')
z.write(lsj)
z.close()


# Now, we need to design the probes around the target sequences - the target sequences are 95 bp long - so we will extract a sequence  
# that starts 40 bp earlier and ends 45 bp after the last bp. From this fragments, we will extract two fragments of 120 bp each, which  
# overlap by 60 bp - position infor is in the header of each file

# In[96]:

probes = [i.split('\n')[0]+'\n'+i.split('\n')[1][int(i.split('\n')[0].split('_')[1].split('-')[0])-40:int(i.split('\n')[0].split('_')[1].split('-')[0])+140] for i in ls] 


# In[101]:

probes2 = []
for i in probes:
    probes2.append(i.split('\n')[0]+'_probe1\n'+i.split('\n')[1][:120]+'\n'+i.split('\n')[0]+'_probe2\n'+i.split('\n')[1][-120:]+'\n')


# In[102]:

# ls[0].split('\n')[0]+'\n'+ls[0].split('\n')[1][int(ls[0].split('\n')[0].split('_')[1].split('-')[0])-40:int(ls[0].split('\n')[0].split('_')[1].split('-')[0])+140]


# In[105]:

probes2f = ','.join(probes2).replace('\n,','\n')


# In[108]:

z = open('/Volumes/group_dv/personal/DValenzano/Jun2014/y-markers_Go_probes.fa', 'w')
z.write(probes2f)
z.close()


# In[ ]:



