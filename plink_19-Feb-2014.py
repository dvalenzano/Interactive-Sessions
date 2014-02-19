import sys
inp = raw_input('What family would you like to analyze?\n')
inp2 = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_%s.csv' % inp
fam = open(inp2, 'rU').read()
famt = zip(*[i.split(',') for i in fam.split('\n')[:-1]])
famt2 = famt[:2]+famt[4:]
head = ','.join([','.join(list(j)+['\n'])  for j in zip(*[list(i) for i in famt2[:8]])[1:]]).replace(',\n','\n').replace('\n,','\n').replace(',','\t')
z0 = '/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_%scov.txt' % inp
z = open(z0, 'w')
z.write(head)
z.close()
