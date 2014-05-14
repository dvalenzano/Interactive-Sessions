
# coding: utf-8

# In[3]:

tab1fas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_1f_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab1fas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]

# <markdowncell>

# The list comprehension above corresponds to the following loop:

# <codecell>

low2 = []
for i in tab1fas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05:
        low2.append(i+'\n')

# <codecell>

lowz = tab1fas.split('\n')[0] + '\n'+','.join(low2).replace('\n,','\n')

# <codecell>

low3 = []
for i in tab1fas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.01:
        low3.append(i+'\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_1f_sqtl_sig', 'w')
z.write(lowz)
z.close()


# In[4]:

tab1mas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_1m_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab1mas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]

# <markdowncell>

# The list comprehension above corresponds to the following loop:

# <codecell>

low2 = []
for i in tab1mas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05:
        low2.append(i+'\n')

# <codecell>

lowz = tab1mas.split('\n')[0] + '\n'+','.join(low2).replace('\n,','\n')

# <codecell>

low3 = []
for i in tab1mas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.01:
        low3.append(i+'\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_1m_sqtl_sig', 'w')
z.write(lowz)
z.close()


# In[6]:

tab3fas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_1f_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab3fas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]

# <markdowncell>

# The list comprehension above corresponds to the following loop:

# <codecell>

low2 = []
for i in tab3fas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05:
        low2.append(i+'\n')

# <codecell>

lowz = tab3fas.split('\n')[0] + '\n'+','.join(low2).replace('\n,','\n')

# <codecell>

low3 = []
for i in tab3fas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.01:
        low3.append(i+'\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/fem/fam_3f_sqtl_sig', 'w')
z.write(lowz)
z.close()

tab3mas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_3m_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab3mas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]

# <markdowncell>

# The list comprehension above corresponds to the following loop:

# <codecell>

low2 = []
for i in tab3mas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05:
        low2.append(i+'\n')

# <codecell>

lowz = tab3mas.split('\n')[0] + '\n'+','.join(low2).replace('\n,','\n')

# <codecell>

low3 = []
for i in tab3mas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.01:
        low3.append(i+'\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/AAo/mal/fam_3m_sqtl_sig', 'w')
z.write(lowz)
z.close()


# In[ ]:



