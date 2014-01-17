# -*- coding: utf-8 -*-

# The goal of this script is to generate a new exome file that contains - in the header - 
# the size of the exon itself. That's all. The only problem is that this requires to open 
# the whole file first, which can be huge. That's why I started developing a slightly different 
# code in the beginning of the file, which does not require the big exome file to be read by the 
# read() function. This is now commented out, but should work as well so do not discard. 

# <nbformat>3.0</nbformat>

# <codecell>

#exome = '/Volumes/group_dv/group/data/WES/Nfur_exon_sequences.fa'
#w = open('/Volumes/group_dv/group/data/WES/Nfur_exon_Yumi.fa', 'w')

#for i in open(exome):
#    lz = []
#    ls = []
#    lz.append(i)
#    if i[0] == '>':
#        ls.append(i+'length: '+str(len(lz.index[i]+1)))
#    else:
#        ls.append(i)
#w.close()

# <codecell>

#ex = open('/Volumes/group_dv/group/data/WES/Nfur_exon_sequences.fa', 'rU').read()
short_ex = open('/Volumes/group_dv/group/data/WES/Nfur_exon_sequences_short.fa', 'rU').read()

# <codecell>

#exs = ex.split('\n')[:-1]
short_exs = short_ex.split('\n')[:-1]

# <codecell>

def addlength(inp):
    ls = []
    for i in inp:
        if i[0] == '>':
            ls.append(i+'length:'+ str(len(inp[inp.index(i)+1]))+'\n')
        else:
            ls.append(i+'\n')
    return ','.join(ls).replace('\n,','\n')

# <codecell>

shout = addlength(short_exs)
#bigout = addlength(exs)

# <codecell>

z = open('/Volumes/group_dv/group/data/WES/Nfur_exon_Yumi_short.fa','w')
z.write(shout)
z.close()

# <codecell>

length = [len(i) for i in short_ex.split('\n')[:-1] if i[0] != '>' ] #You can use this to plot the density of exon sizes

# <codecell>

#z = open('/Volumes/group_dv/group/data/WES/Nfur_exon_sequences_withlength.fa','w')
#z.write(bigout)
#z.close()

