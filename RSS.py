# This script finds heptamer - nonamer clusters in any fasta file 
import sys
inp_ut = raw_input('What is the scaffold where you want to find the RSS?\n')
inp = open(inp_ut, 'rU').read()

#a = open('/Volumes/group_dv/group/Ig_Asya/IgD_scaffold.fa', 'rU').read()
string = inp.split('\n')[0]+'\n'+','.join(inp.split('\n')[1:]).replace(',','')

heptamer = raw_input('Please type the heptamer sequence\n')
nonamer = raw_input('Please type the nonamer sequence\n')

import re
inp1 = heptamer+'\w'*12+nonamer
inp2 = heptamer+'\w'*23+nonamer

hep_non12 = re.findall(inp1, string)
heno12 = [re.search(i,string) for i in hep_non12 ]
hen12 = [list(j) for j in zip(hep_non12, [i.span() for i in heno12])]
line12 = 'Sequence,start,end\n'+','.join([i[0] + ','+','.join([str(x) for x in i[1]])+'\n' for i in hen12 ] ).replace('\n,','\n')

#hn12 = ','.join([ i+'\n' for i in hep_non12 ])

hep_non23 = re.findall(inp2, string)
heno23 = [re.search(i,string) for i in hep_non23 ]
hen23 = [list(j) for j in zip(hep_non23, [i.span() for i in heno23])]
line23 = 'Sequence,start,end\n'+','.join([i[0] + ','+','.join([str(x) for x in i[1]])+'\n' for i in hen23 ] ).replace('\n,','\n')

#hn23 = ','.join([ i+'\n' for i in hep_non23 ])

out12 = inp_ut[:-3]+'_12.txt'
out23 = inp_ut[:-3]+'_23.txt'

z = open(out12, 'w')
#z.write(hn12.replace('\n,','\n'))
z.write(line12)
z.close()

z = open(out23, 'w')
#z.write(hn23.replace('\n,','\n'))
z.write(line23)
z.close()

#class Find_RSS(object):
#    "in each scaffold, searches for heptamers and nonamers and saves them"
#    def __init__(self, filein):
#        self.filein = filein
#        self.header = self.filein.split('\n')[0]
#        self.body = self.filein.split('\n')[1]
#        
#        self.hep_non12 = re.findall(inp1, self.body)
#        self.heno12 = [re.search(i,self.body) for i in self.hep_non12 ]
#        self.hen12 = [list(j) for j in zip(self.hep_non12, [i.span() for i in self.heno12])]
#        self.line12 = self.header+',Sequence,start,end\n'+','.join([i[0] + ','+','.join([str(x) for x in i[1]])+'\n' for i in self.hen12 ] ).replace('\n,','\n')
    
#        self.hep_non23 = re.findall(inp1, self.body)
#        self.heno23 = [re.search(i,self.body) for i in self.hep_non23 ]
#        self.hen23 = [list(j) for j in zip(self.hep_non23, [i.span() for i in self.heno23])]
#        self.line23 = self.header+',Sequence,start,end\n'+','.join([i[0] + ','+','.join([str(x) for x in i[1]])+'\n' for i in self.hen23 ] ).replace('\n,','\n')
   
