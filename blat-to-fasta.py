import sys

genome = raw_input('What is the genome file to use for your analysis?\n')

blatout = raw_input('What is the blat output that you need to process?\n') #i.e the output file of a blat search

inp_gen = open(genome, 'rU').read()
if not inp_gen:
    print 'There is no such file, please check the spelling or location and try again'
inp_scaff = open(blatout, 'rU').read()
if not inp_scaff:
    print 'There is no such file, please check the spelling or location and try again'

inp_scaffs = inp_scaff.split('\n')[5:-1]
scaffolds = []
for i in inp_scaffs:
    scaffolds.append('>'+i.split('\t')[13]) #this creates a list of scaffolds that have blat hits

scaffoldsj = ','.join(scaffolds).replace(',','\n')
z = open('scaffolds.txt', 'w') #saves the scaffolds list as a string in the current directory
z.write(scaffoldsj)
z.close()

inp_gens = inp_gen.split('\n')[:-1]

keys = inp_gens[:len(inp_gens):2] 
values = inp_gens[1:len(inp_gens):2]

d = dict(zip(keys, values)) #this is a dictionary that contains scaffold names as keys and corresponding sequences as values

ls = []
for i in scaffolds:
    if i in d.keys():
        ls.append(i + '\n' + d[i]+'\n')
        
lsj = ','.join(ls).replace('\n,','\n')

z = open('output.fa', 'w')
z.write(lsj)
z.close()

