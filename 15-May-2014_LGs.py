
# coding: utf-8

# In[1]:

f = raw_input("what is the linkage file that you want to trim?")
fin = 'AAo_%s' %str(f)
inp = open(fin, 'rU').read()


# In[4]:

inps = inp.split('\n\n\n')


# In[22]:

def trim(inp):
    ls = []
    for i in inp.split('\n'):
        if i[-2:]=='b ':
            ls.append(i+'\n')
        elif i[-2:]=='a ':
            ls.append(i+'\n')
    return ','.join(ls)+'\n'


# In[24]:

lz = []
for i in inps:
    lz.append(trim(i))


# In[27]:

lzf = ','.join(lz).replace('\n,','\n')


# In[28]:

out = fin+'_LGs.txt'
z = open(out, 'w')
z.write(lzf)
z.close()


# In[ ]:



