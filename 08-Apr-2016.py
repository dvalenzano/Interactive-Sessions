
# coding: utf-8

# **Goal: To call transcripts based on OTU abundance, based on the transcriptome/OTU data**  
# First, I extract all the significanly different OTUs between the various classes

# In[1]:

yo = open('/beegfs/group_dv/home/PSmith/LEfSe/6wk_vs_16wk_lefse_result.txt', 'rU').read()
yol = [ i.split('\t') for i in yo.split('\n') ]
yo_s = sorted(yol, key=lambda x:(x[-1]), reverse=True)
yo_f = [i for i in yo_s if i[-1] != '-']


# In[2]:

yyt_ost = open('/beegfs/group_dv/home/PSmith/LEfSe/lefse_result_even_5509_6wk_ymt_vs_16wk_smt.txt', 'rU').read()
yyt_ostl = [ i.split('\t') for i in yyt_ost.split('\n') ]
yyt_ost_s = sorted(yyt_ostl, key=lambda x:(x[-1]), reverse=True)
yyt_ost_f = [i for i in yyt_ost_s if i[-1] != '-']

y_yt = open('/beegfs/group_dv/home/PSmith/LEfSe/lefse_results_6wk_v_ymt.txt', 'rU').read()
y_ytl = [ i.split('\t') for i in y_yt.split('\n') ][:-1]
y_yt_s = sorted(y_ytl, key=lambda x:(x[-1]), reverse=True)
y_yt_f = [i for i in y_yt_s if i[-1] != '-']


# Now I will build a dictionary that matches all bacterial names to indexes

# In[122]:

ind = open('/beegfs/group_dv/home/PSmith/LEfSe/otu_table_mc5_w_tax_no_pynast_failures.txt', 'rU').read()
ind = ind.replace(']', '').replace('[', '')
ind_l = [ i.split('\t') for i in ind.split('\n')[2:-1] ]
ind_otu = [ i[0]+','+i[-1] for i in ind_l ]

inds = [ i.split(',')[0] for i in ind_otu]
otus = [ i.split(',')[1] for i in ind_otu]

from sets import Set

ind_s = Set(inds)
otu_s = Set(otus)


# In[155]:

LS = []
for k in otu_s:
    for i,x in enumerate(otus):
        if x == k:
            LS.append(k +',' +str(i))

LSS = ','.join(LS)
            
LQ = []
LP = []
for k in list(otu_s):
    ST = '%s,\d+' % k
    match = re.findall(ST, LSS)
    LQ.append(match)
LP = [ ','.join([i[0].split(',')[0]] + [j.split(',')[1] for j in i]) for i in LQ if i!= [] ]
lp = ','.join([i+'\n' for i in LP ]).replace('\n,','\n')


# "lp" is a collection of OTUs with their respective indexes matching the otu and ind lists 

# In[ ]:



