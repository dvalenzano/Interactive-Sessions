barcodes = open('/Users/DValenzano/Dropbox/tmp/barcodes_plate5.txt', 'rU').read()
ls = []
for i in barcodes.split('\n')[:-1]:
    ls.append('mv $src/samples/plate5/sample_'+i.split('\t')[0]+' '+'$src/samples/plate5/'+i.split('\t')[1]+'.fq\n')

lsj = ','.join(ls).replace('\n,','\n')    
z = open('/Users/DValenzano/Dropbox/tmp/file5', 'w')
z.write(lsj)
z.close()
