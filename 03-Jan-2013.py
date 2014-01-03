# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# First import the two files with the homozygous markers

# <codecell>

goh = open('/Volumes/group_dv/personal/DValenzano/Jan2014/NfGo_hom_geno.csv', 'rU').read()
aaoh = open('/Volumes/group_dv/personal/DValenzano/Jan2014/NfAAo_hom_geno.csv', 'rU').read()

gp = open('/Volumes/group_dv/personal/DValenzano/Nov2013/go_phen.csv', 'rU').read()
aap = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aao_phen.csv', 'rU').read()

gps = gp.split('\n')
aaps = aap.split('\n')

# <markdowncell>

# I need to check if the IDs are in the same order for both goh and gp, and for aaoh and aap

# <codecell>

goh_ID = goh.split('\n')[0].split(',')[5:]
aaoh_ID = aaoh.split('\n')[0].split(',')[5:]
gp_ID = [ i.split(',')[0] for i in gp.split('\n')[2:]]
aap_ID = [ i.split(',')[0] for i in aap.split('\n')[2:]]

# <codecell>

g = [i for i in range(len(goh_ID)) if goh_ID[i] == gp_ID[i]]
aa = [i for i in range(len(aaoh_ID)) if aaoh_ID[i] == aap_ID[i]]

# <markdowncell>

# or, alternatively, using zip:

# <codecell>

gn = [ i for i in zip(goh_ID, gp_ID) if i[0] != i[1] ]
aan = [ i for i in zip(aaoh_ID, aap_ID) if i[0] != i[1] ]

# <markdowncell>

# Both g and aa have the same order of IDs in the phenotype file and in the genotype file. I can therefore add the phenotypes without hesitation to the genotype table.   
# First, I need to transpose them both the genotype matrices:

# <codecell>

goht = zip(*[ i.split(',') for i in goh.split('\n')])
aaoht = zip(*[ i.split(',') for i in aaoh.split('\n')])

# <codecell>

gohn = [list(goht[0])]+[ list(i) for i in goht[4:]]
aaohn = [list(aaoht[0])]+[ list(i) for i in aaoht[4:]]

# <codecell>

#aaz = zip(*[ aaps[i].split(',')[:10]+aaohn[i][1:] for i in range(len(aaohn))])
aaz = ','.join([ ','.join(aaps[i].split(',')[:10]+aaohn[i][1:])+'\n' for i in range(len(aaohn))]).replace('\n,','\n')
gz = ','.join([ ','.join(gps[i].split(',')[:10]+gohn[i][1:])+'\n' for i in range(len(gohn))]).replace('\n,','\n')

# <codecell>

#aazj = ','.join([','.join(i)+'\n' for i in aaz ]).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/NfAAo_pg.csv', 'w')
z.write(aaz)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/Jan2014/NfGo_pg.csv', 'w')
z.write(gz)
z.close()

# <codecell>


