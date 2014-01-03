import sys
input=raw_input('what is the file that you want to convert to fasta?\n')
inp = open(input, 'rU').read()
h = inp.split('\n\n')[0]
fasta = ','.join([ '>'+i.split('\t')[0]+'\n'+i.split('\t')[4]+'\n'for i in h.split('\n')[1:]]).replace(',','')
fa = '%s.fa' % input[:-4]
z = open(fa, 'w')
z.write(fasta)
z.close()
