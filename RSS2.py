# This script finds heptamer - nonamer clusters in any fasta file 
# This version is open to any combination of two sequences separated by a variable size of spacer sequence

import sys
inp_ut = raw_input('What is the scaffold where you want to find the RSS?\n')
inp = open(inp_ut, 'rU').read()

#a = open('/Volumes/group_dv/group/Ig_Asya/IgD_scaffold.fa', 'rU').read()
string = inp.split('\n')[0]+'\n'+','.join(inp.split('\n')[1:]).replace(',','')

heptamer = raw_input('Please type the fist sequence (heptamer)\n')
nonamer = raw_input('Please type the second sequence (nonamer)\n')
gap = raw_input('Please type the number of bp between the two sequences?\n')

import re
#inp1 = heptamer+'\w'*12+nonamer
#inp = heptamer+'\w'*25+nonamer
inp = heptamer+'\w'*int(gap)+nonamer

#hep_non12 = re.findall(inp1, string)
#heno12 = [re.search(i,string) for i in hep_non12 ]
#hen12 = [list(j) for j in zip(hep_non12, [i.span() for i in heno12])]
#line12 = 'Sequence,start,end\n'+','.join([i[0] + ','+','.join([str(x) for x in i[1]])+'\n' for i in hen12 ] ).replace('\n,','\n')

#hn12 = ','.join([ i+'\n' for i in hep_non12 ])

hep_non23 = re.findall(inp, string)
heno23 = [re.search(i,string) for i in hep_non23 ]
hen23 = [list(j) for j in zip(hep_non23, [i.span() for i in heno23])]
line23 = 'Sequence,start,end\n'+','.join([i[0] + ','+','.join([str(x) for x in i[1]])+'\n' for i in hen23 ] ).replace('\n,','\n')

#hn23 = ','.join([ i+'\n' for i in hep_non23 ])

#out12 = inp_ut[:-3]+'_12.txt'
out23 = inp_ut[:-3]+'_out.txt'

#z = open(out12, 'w')
#z.write(hn12.replace('\n,','\n'))
#z.write(line12)
#z.close()

z = open(out23, 'w')
#z.write(hn23.replace('\n,','\n'))
z.write(line23)
z.close()
