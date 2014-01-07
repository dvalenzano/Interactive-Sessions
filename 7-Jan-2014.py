# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: to calculate the amount of homozygous markers and non-homozygous markers in the P0 for both AAo and Go

# <codecell>

go_7 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/Go_families/Go_inf-fam/inf_fam_7.csv', 'rU').read()
aao_1 = open('/Volumes/group_dv/personal/DValenzano/Dec2013/F1-inference/AAo_families/AAo_inf/fam-1.csv', 'rU').read()

# <markdowncell>

# Now, transpose the matrices

# <codecell>

go_7t = zip(*[ i.split(',') for i in go_7.split('\n')[:-1] ])
aao_1t = zip(*[ i.split(',') for i in aao_1.split('\n')[:-1] ])

# <codecell>

gp0gen = [ ','.join(list(i)[1:3]).replace(',','')   for i in go_7t[10:]]
aap0gen = [ ','.join(list(i)[1:3]).replace(',','')   for i in aao_1t[10:]]

# <codecell>

p0g_aabb = float(gp0gen.count('aabb'))/len(p0gen)
p0aa_aabb = float(aap0gen.count('aabb'))/len(p0gen)

print 'in cross Go\nhomozygous markers: %d\nhomozygous ratio: %.2f\n\nin cross AAo\nhomozygous markers: %d\nhomozygous ratio: %.2f' % (gp0gen.count('aabb'), p0g_aabb, aap0gen.count('aabb'), p0aa_aabb)

# <codecell>


# <codecell>


