import sys

tr = raw_input('What is the genome or transcriptome file to use for your analysis?\n')

blatout = raw_input('What is the blat output that you need to process?\n') #i.e the output file of a blat search

inp_tr = open(tr, 'rU').read()

if not inp_tr:
    print 'There is no such file, please check the spelling or location and try again'
    pass

inp_scaff = open(blatout, 'rU').read()

if not inp_scaff:
    print 'There is no such file, please check the spelling or location and try again'
    pass

inp_scaffs = inp_scaff.split('\n')[5:-1]

scaffolds = []

for i in inp_scaffs:
    scaffolds.append('>'+i.split('\t')[13]+'_'+','.join(i.split('\t')[15:17]).replace(',','-')) #this creates a list of scaffolds that have blat hits

scaffoldsj = ','.join(scaffolds).replace(',','\n')

z = open('scaffolds.txt', 'w') #saves the scaffolds list as a string in the current directory
z.write(scaffoldsj)
z.close()

inp_trs = inp_tr.split('\n')[:-1]

keys = inp_trs[:len(inp_trs):2] 
values = inp_trs[1:len(inp_trs):2]

d = dict(zip(keys, values)) #this is a dictionary that contains scaffold names as keys and corresponding sequences as values

ls = []
for i in scaffolds:
    if ','.join(scaffolds[0].split('_')[:-1]).replace(',','_') in d.keys():
        ls.append(','.join(scaffolds[0].split('_')[:-1]).replace(',','_') + '\n' + d[','.join(scaffolds[0].split('_')[:-1]).replace(',','_')]+'\n')
        
lsj = ','.join(ls).replace('\n,','\n')

output = blatout[:-4]+'_btf.fa'

z = open(output, 'w')
z.write(lsj)
z.close()
