# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: To create a new sub-file with significant markers from plink analysis to OneMap analysis

# <codecell>

tab7fas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/fem/fam_7f_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab7fas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]

# <markdowncell>

# The list comprehension above corresponds to the following loop:

# <codecell>

low2 = []
for i in tab7fas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05:
        low2.append(i+'\n')

# <codecell>

lowz = tab7fas.split('\n')[0] + '\n'+','.join(low2).replace('\n,','\n')

# <codecell>

low3 = []
for i in tab7fas.split('\n')[1:-1]:
    if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.01:
        low3.append(i+'\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/fem/fam_7f_sqtl_sig', 'w')
z.write(lowz)
z.close()

# <codecell>

len(low2)

# <markdowncell>

# Below the same, for the sqtl in male f7

# <codecell>

tab7mas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/mal/fam_7m_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab7mas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]
lowz = tab7mas.split('\n')[0] + '\n'+','.join(low1).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/mal/fam_7m_sqtl_sig', 'w')
z.write(lowz)
z.close()

# <markdowncell>

# Then the same for family 14 as well

# <codecell>

tab14mas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/mal/fam_14m_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab14mas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]
lowz = tab14mas.split('\n')[0] + '\n'+','.join(low1).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/mal/fam_14m_sqtl_sig', 'w')
z.write(lowz)
z.close()

tab14fas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/fem/fam_14f_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab14fas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]
lowz = tab14fas.split('\n')[0] + '\n'+','.join(low1).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/fem/fam_14f_sqtl_sig', 'w')
z.write(lowz)
z.close()

# <markdowncell>

# Then family 8

# <codecell>

#tab8mas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/mal/fam_14m_sqtl.assoc.linear', 'rU').read()
tab8mas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/mal/fam_8m_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab8mas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]
lowz = tab8mas.split('\n')[0] + '\n'+','.join(low1).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/mal/fam_8m_sqtl_sig', 'w')
z.write(lowz)
z.close()

#tab8fas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_14/fem/fam_14f_sqtl.assoc.linear', 'rU').read()
tab8fas = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/fem/fam_8f_sqtl.assoc.linear', 'rU').read()
low1 = [ i+'\n' for i in tab8fas.split('\n')[1:-1] if i.split()[-1] != 'NA' and float(i.split()[-1]) < 0.05]
lowz = tab8fas.split('\n')[0] + '\n'+','.join(low1).replace('\n,','\n')
z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_8/fem/fam_8f_sqtl_sig', 'w')
z.write(lowz)
z.close()

# <codecell>


